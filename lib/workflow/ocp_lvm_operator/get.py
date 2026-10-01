import copy
from lib.k8s import output as k8s_output
from lib.linux import output as linux_output
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_lvm_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state', 'res', 'lvm'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def collect_pvc_info(params, my_output):
    params['dv'] = None
    params['pv'] = None
    params['snapshot'] = None
    params['pvc'] = None
    params['storage_class'] = None

    my_output.debug('- storage class')
    storage_class = params['k8s_handler'].get_storage_class_lvm(cache_enabled=False)
    if storage_class is None:
        return params
    params['storage_class'] = [storage_class]

    my_output.debug('- pvc')
    params['pvc'] = params['k8s_handler'].get_pvcs(
        object_filter=['sc:%s' % (params['storage_class'][0]['name'])],
        usage_info=True,
        exclude_pods=True,
        cache_enabled=False
    )

    if params['pvc'] is None:
        return params
    
    pvc_list = []
    for pvc in params['pvc']:
        pvc_list.append(pvc['namespace_name'])

    my_output.debug('- dv')
    params['dv'] = params['k8s_handler'].get_data_volumes(
        object_filter=['pvcs:%s' % (','.join(pvc_list))],
        cache_enabled=False
    )

    my_output.debug('- pv')
    params['pv'] = params['k8s_handler'].get_pvs(
        object_filter=['pvcs:%s' % (','.join(pvc_list))],
        cache_enabled=False
    )

    my_output.debug('- snapshot')
    params['snapshot'] = params['k8s_handler'].get_volume_snapshots(
        object_filter=['pvcs:%s' % (','.join(pvc_list))],
        cache_enabled=False
    )

    return params


def collect_lvm_info(params, my_output, log_id):
    if 'lvm' not in params['view']:
        return params
    
    if params['ssh_handler'] is None:
        return params

    params['linux_lvm'] = local_common.get_linux_lvm(
        params['cluster'],
        params['k8s_handler'],
        my_output,
        log_id=log_id
    )

    return params


def collect_state_info(params, my_output, log_id):
    my_output.debug('- lvmc')
    params['lvmc'] = params['k8s_handler'].get_lvm_cluster(cache_enabled=False)
    if params['lvmc'] is None:
        return params
    
    params = collect_pvc_info(params, my_output)
    params = collect_lvm_info(params, my_output, log_id)

    params['summary']['resources'] = {}
    for key in ['storage_class', 'pvc', 'dv', 'pv', 'snapshot']:
        params['summary']['resources'][key] = '---'
        if key not in params:
            continue

        if params[key] is None:
            continue

        params['summary']['resources'][key] = len(params[key])

    return params


def run(mparams, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    linux_output_handler = linux_output.LinuxOutput(log_id=log_id)

    mparams, error = validate(mparams)
    if error is not None:
        my_output.error(error)
        return False
    
    for cluster in mparams['cluster']:
        params = copy.deepcopy(mparams)
        params['cluster'] = cluster

        ocp_common.print_title(params, my_output, 'Get Information')
        params = ocp_common.workflow_init(params, my_output, log_id, ssh_optional=True)
        if params is None:
            continue

        params = ocp_common.get_operator(params, my_output, csv=True)
        if params['subscription'] is None:
            continue

        params = collect_state_info(params, my_output, log_id)

        if 'state' in params['view']:
            my_output.dictionary_ng(
                'Operator',
                params['summary'],
                [
                    ['package', 'package'],
                    ['csv', 'csv'],
                    ['resources', 'readyTick']
                ],
                underline=True
            )

            if params['lvmc'] is None:
                my_output.default('LVM Cluster instance %s' % (my_output.add_color('not found', 'Red')))       
            else:
                k8s_output_handler.print_lvm_cluster(
                    params['lvmc'],
                    show_device_class=False
                )

                my_output.dictionary_ng(
                    'LVM Related Resources',
                    params['summary']['resources'],
                    [
                        ['storage class', 'storage_class'],
                        ['pvc', 'pvc'],
                        ['dv', 'dv'],
                        ['pv', 'pv'],
                        ['snapshot', 'snapshot']
                    ]
                )

        if 'res' in params['view']:
            if params['lvmc'] is None:
                my_output.default('LVM Cluster instance %s' % (my_output.add_color('not found', 'Red')))       
            else:
                k8s_output_handler.print_lvm_cluster(
                    params['lvmc']
                )

                my_output.dictionary_ng(
                    'LVM Related Resources',
                    params['summary']['resources'],
                    [
                        ['storage class', 'storage_class'],
                        ['pvc', 'pvc'],
                        ['dv', 'dv'],
                        ['pv', 'pv'],
                        ['snapshot', 'snapshot']
                    ]
                )
                
                if params['storage_class'] is None:
                    my_output.default('LVM storage class %s' % (my_output.add_color('not found', 'Red')))
                else:
                    k8s_output_handler.print_storage_classes(params['storage_class'])

                if params['pvc'] is not None and len(params['pvc']):
                    k8s_output_handler.print_pvcs(params['pvc'])

                if params['pv'] is not None and len(params['pv']):
                    k8s_output_handler.print_pvs(params['pvc'])

                if params['dv'] is not None and len(params['dv']):
                    k8s_output_handler.print_data_volumes(params['dv'])

                if params['snapshot'] is not None and len(params['snapshot']):
                    k8s_output_handler.print_volume_snapshots(params['snapshot'])

        if 'lvm' in params['view']:
            if params['ssh_handler'] is not None:
                local_common.print_linux_lvm(
                    params['linux_lvm'],
                    linux_output_handler
                )

    return True