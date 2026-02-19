import json
from lib.k8s import output as k8s_output
from lib.linux import output as linux_output
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_lvm_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'ssh-check' not in params:
        params['ssh-check'] = True

    if not isinstance(params['ssh-check'], bool):
        return None, 'ssh-check params must be true or false'

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'check-verbose',
        'verbose',
        'ssh-check'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    linux_output_handler = linux_output.LinuxOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - LVM Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, ssh_check=True)
    if params is None:
        return False

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Operator not found: %s' % (params['name']))
        return True
    
    my_output.default('Operator', underline=True)
    my_output.default('- subscription: %s' % (subscription['namespace_name']))
    my_output.default('- csv: %s' % (subscription['installed_csv']))
    
    csv = params['k8s_handler'].get_cluster_service_version(
        subscription['namespace'],
        subscription['installed_csv'],
        return_mo=False,
        cache_enabled=False
    )
    if csv is None:
        my_output.debug('[WARNING] CSV not found: %s/%s' % (subscription['namespace'], subscription['installed_csv']))
    
    lvmc = params['k8s_handler'].get_lvm_cluster(cache_enabled=False)
    if lvmc is None:
        my_output.default('- LVM Cluster instance not found')
        return False
    
    k8s_output_handler.print_lvm_cluster(
        lvmc
    )
    
    storage_class = params['k8s_handler'].get_storage_class_lvm(cache_enabled=False)
    if storage_class is None:
        my_output.error('LVM storage class not found')
    else:
        my_output.default('LVM storage class', underline=True, before_newline=True)
        k8s_output_handler.print_storage_classes([storage_class])

    pvcs = None
    pvcs_ready = False
    pvcs_used = False
    if storage_class is not None:
        pvcs_ready = True
        pvcs = params['k8s_handler'].get_pvcs(
            object_filter=['sc:%s' % (storage_class['name'])],
            usage_info=True,
            cache_enabled=False
        )
        if pvcs is None:
            my_output.error('Failed to get pvc information')
            return False
        
        pvcs_list = []
        for pvc in pvcs:
            pvcs_ready = pvcs_ready and pvc['ready']
            pvcs_used = pvcs_used or pvc['used']
            pvcs_list.append(pvc['namespace_name'])
        
        dvs = params['k8s_handler'].get_data_volumes(
            object_filter=['pvcs:%s' % (','.join(pvcs_list))],
            cache_enabled=False
        )
        if dvs is not None and len(dvs) > 0:
            my_output.default('Data Volumes', underline=True, before_newline=True)
            k8s_output_handler.print_data_volumes(dvs)
        
        my_output.default('Perstistent Volume Claims', underline=True, before_newline=True)
        k8s_output_handler.print_pvcs(pvcs)

        if len(pvcs) > 0:
            pvs = params['k8s_handler'].get_pvs(
                object_filter=['pvcs:%s' % (','.join(pvcs_list))],
                cache_enabled=False
            )

            k8s_output_handler.print_pvs(pvs)

            snapshots = params['k8s_handler'].get_volume_snapshots(
                object_filter=['pvcs:%s' % (','.join(pvcs_list))],
                cache_enabled=False
            )
            if snapshots is not None and len(snapshots) > 0:
                my_output.default('Volume Snapshots', underline=True, before_newline=True)
                k8s_output_handler.print_volume_snapshots(snapshots, title=False)

    server_info = False
    if params['ssh-ready']:
        server_info = True
        linux_lvm_info = local_common.get_linux_lvm(
            params['cluster'],
            params['k8s_handler'],
            my_output,
            log_id=log_id
        )

        local_common.print_linux_lvm(
            linux_lvm_info,
            linux_output_handler
        )

    my_output.default('Summary', before_newline=True, underline=True)
    my_output.default('- operator: %s' % (subscription['installed_csv']))
    if lvmc['info']['ready']:
        my_output.default('- lvm cluster: %s [%s]' % (lvmc['namespace_name'], my_output.add_color(lvmc['info']['state'], 'Green')))
    else:
        my_output.default('- lvm cluster: %s [%s]' % (lvmc['namespace_name'], my_output.add_color(lvmc['info']['state'], 'Red')))

    if storage_class is None:
        my_output.default(my_output.add_color('- no storage class found', 'Red'))
    
    if storage_class is not None:
        if storage_class['default']:
            my_output.default('- default storage class: %s' % (storage_class['name']))
        else:
            my_output.default('- storage class [%s]: %s' % (my_output.add_color('not default', 'Red'), storage_class['name']))

        if pvcs is None:
            my_output.default(my_output.add_color('- no pvc info collected', 'Red'))
        
        if pvcs is not None:
            if len(pvcs) == 0:
                my_output.default('- no persistent volume claims')
            else:
                if pvcs_ready:
                    my_output.default('- persistent volume claims [%s]: %s' % (my_output.add_color('all bound', 'Green'), len(pvcs)))
                else:
                    my_output.default('- persistent volume claims [%s]: %s' % (my_output.add_color('not all bound', 'Red'), len(pvcs)))

                if pvcs_used:
                    my_output.default('- some pvcs used (pod/vm)')
                else:
                    my_output.default('- no pvcs used (pod/vm)')

    if not server_info:
        my_output.default(my_output.add_color('- server info not collected <=> configure ssh access to cluster nodes', 'Red'))
    else:
        if linux_lvm_info['collected']:
            my_output.default('- server lvm info fully collected')
        else:
            my_output.default(my_output.add_color('- server lvm info fully collected', 'Red'))

        if linux_lvm_info['orphan']:
            my_output.default(my_output.add_color('- some logical volumes not backed by kube resources', 'Red'))
        else:
            my_output.default('- all logical volumes back by kube resources')

    return True
