import json
import copy
from lib.workflow import ocp_common
from lib.workflow.ocp_access import check as ocp_check


def initialize(params, my_output, log_id, ssh_check=False, ssh_required=False):
    params = augment_params(params)

    if params['verbose']:
        my_output.default('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        if 'instance' in display_params and display_params['instance'] is not None:
            display_params['instance'] = 'user-defined'
        my_output.default(json.dumps(display_params, indent=4), after_newline=True)
    else:
        my_output.debug('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.debug(json.dumps(display_params, indent=4), after_newline=True)
        
    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['ssh-check'] = ssh_check
    ocp_check_params['ssh-required'] = ssh_required
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler

    params['ssh-ready'] = False
    if 'ssh_public_key' in ocp_check_params['data']:
        params['ssh-ready'] = True

    return params


def get_default_params():
    params = {}
    params['namespace'] = 'openshift-storage'
    params['name'] = 'lvms-operator'
    params['operator-group-name'] = 'lvm-operator-group'
    params['delete-namespace'] = True
    return params


def augment_params(params):
    defaults = get_default_params()
    for key in defaults:
        params[key] = defaults[key]
    return params


def sanitize_params(params, allowed_keys):
    new_params = {}
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params


def is_lvm_ready(params, my_output, check_lvm_cluster=True, instance_allowed=True, instance_required=True, ready_required=True, storage_class_required=False):
    my_output.default('LVM Operator', underline=True, before_newline=True)

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.error('Operator not found: %s' % (params['name']))
        return False
    
    my_output.default(
        'LVM Operator [%s] with csv [%s]' % (
            subscription['namespace_name'],
            subscription['installed_csv']
        )
    )

    csv = params['k8s_handler'].get_cluster_service_version(
        subscription['namespace'],
        subscription['installed_csv'],
        return_mo=False,
        cache_enabled=False
    )
    if csv is None:
        my_output.error('CSV not found: %s/%s' % (subscription['namespace'], subscription['installed_csv']))
        return False
    
    if instance_required and ready_required and not params['k8s_handler'].is_subscription_lvm_ready():
        my_output.error('LVM subscription is not fully deployed')
        return False
    
    my_output.default('LVM Subscription resources deployed')
    
    if not check_lvm_cluster:
        return True
    
    lvmc = params['k8s_handler'].get_lvm_cluster(cache_enabled=False)
    if lvmc is None:
        if instance_required:
            my_output.error('LVM Cluster instance not found')
            return False

        my_output.default('LVM Cluster instance not found')
        return True
    else:
        if not instance_allowed:
            my_output.error('LVM Cluster instance found and not expected')
            return False

    my_output.default('LVM Cluster instance: %s' % (lvmc['namespace_name']))
    if not lvmc['info']['ready']:
        if ready_required:
            my_output.error('LVM Cluster instance not ready')
            return False

        my_output.default('LVM Cluster instance not ready: %s' % (my_output.add_color(lvmc['info']['state'], 'Red')))
    else:
        my_output.default('LVM Cluster instance: %s' % (my_output.add_color('ready', 'Green')))

    storage_class = params['k8s_handler'].get_storage_class_lvm(cache_enabled=False)
    if storage_class is None:
        if storage_class_required:
            my_output.error('LVM storage class not found')
            return False
            
        my_output.default('%s storage class not found' % (my_output.add_color('[WARNING]', 'Red')))
    else:
        my_output.default('Storage class: %s' % (storage_class['name']))

    return True    


def get_lvm_resources(params, my_output, title=None, pvc=False, pv=False, snapshot=False, k8s_output_handler=None):
    if title is not None:
        my_output.default(title, before_newline=True, underline=True)

    info = {}
    info['used'] = False

    if pv:
        pvc = True

    storage_class = params['k8s_handler'].get_storage_class_lvm(cache_enabled=False)
    if storage_class is None:
        my_output.default('No storage class associated with LVM - there should be no pv/pvc related with LVM')
        return info

    if pvc:
        pvcs = params['k8s_handler'].get_pvcs(
            object_filter=['sc:%s' % (storage_class['name'])],
            usage_info=True,
            cache_enabled=False
        )
        if pvcs is None:
            my_output.error('Failed to get pvc information')
            return None

        if k8s_output_handler is not None:
            my_output.default('Perstistent Volume Claims', before_newline=True)
            k8s_output_handler.print_pvcs(pvcs)
            
        info['pvc'] = pvcs
        if len(pvcs) > 0:
            info['used'] = True

    if pv:
        pvcs_list = []
        for pvc in pvcs:
            pvcs_list.append(pvc['namespace_name'])
        
        pvs = params['k8s_handler'].get_pvs(
            object_filter=['pvcs:%s' % (','.join(pvcs_list))],
            cache_enabled=False
        )

        if k8s_output_handler is not None:
            k8s_output_handler.print_pvs(pvs)

    if snapshot:
        snapshots = params['k8s_handler'].get_volume_snapshots(
            object_filter=['sc:%s' % (storage_class['name'])],
            cache_enabled=False
        )
        if snapshots is None:
            my_output.error('Failed to get snapshot information')
            return None

        if k8s_output_handler is not None:
            my_output.default('Volume Snapshots', before_newline=True)
            k8s_output_handler.print_volume_snapshots(snapshots, title=False)
        info['snapshot'] = snapshots
        if len(snapshots) > 0:
            info['used'] = True

    return info


def get_linux_lsblk(cluster_name, k8s_handler, my_output, log_id=None, device_names=None, include_disk_paths=False):
    my_output.default(
        'Collect linux level lsblk per node...',
        before_newline=True
    )

    linux_handlers = ocp_common.get_nodes_linux_handler(
        cluster_name,
        k8s_handler,
        log_id=log_id
    )
    
    node_names = k8s_handler.get_worker_nodes_name()
    lsblk = {}

    for node_name in node_names:
        lsblk[node_name] = linux_handlers[node_name].get_lsblks(
            device_names=device_names, 
            include_disk_paths=include_disk_paths,
            cache_enabled=False
        )

    return lsblk


def get_linux_lv(cluster_name, k8s_handler, my_output, log_id=None, lv_names=None, include_snap=False):
    my_output.default(
        'Collect linux level lv state...',
        before_newline=True
    )

    linux_handlers = ocp_common.get_nodes_linux_handler(
        cluster_name,
        k8s_handler,
        log_id=log_id
    )
    
    node_names = k8s_handler.get_worker_nodes_name()
    lvs = {}

    for node_name in node_names:
        lvs[node_name] = linux_handlers[node_name].get_lvs(include_pvc=True, name_filter=lv_names, include_snap=include_snap)

    return lvs


def get_linux_lvm(cluster_name, k8s_handler, my_output, log_id=None, cache_enabled=True):
    my_output.default(
        'Collect linux level lvm state...',
        before_newline=True
    )

    linux_handlers = ocp_common.get_nodes_linux_handler(
        cluster_name,
        k8s_handler,
        log_id=log_id
    )
    
    lvm_info_collected = True
    orphan = False
    node_names = k8s_handler.get_worker_nodes_name()

    blks = {}
    lvs = {}
    vgs = {}
    pvs = {}

    for node_name in node_names:
        node_ok = []
        node_nok = []
        blks[node_name] = linux_handlers[node_name].get_lsblks(cache_enabled=cache_enabled)
        if blks[node_name] is None:
            lvm_info_collected = False
            node_nok.append('blks')
        else:
            node_ok.append('blks')

        lvs[node_name] = linux_handlers[node_name].get_lvs(include_pvc=True, cache_enabled=cache_enabled)
        if lvs[node_name] is None:
            lvm_info_collected = False
            node_nok.append('lvs')
        else:
            node_ok.append('lvs')
            for item in lvs[node_name]:
                if not item['is_pool'] and item['orphan']:
                    orphan = True

        vgs[node_name] = linux_handlers[node_name].get_vgs(cache_enabled=cache_enabled)
        if vgs[node_name] is None:
            node_nok.append('vgs')
            lvm_info_collected = False
        else:
            node_ok.append('vgs')

        pvs[node_name] = linux_handlers[node_name].get_pvs(cache_enabled=cache_enabled)
        if pvs[node_name] is None:
            node_nok.append('pvs')
            lvm_info_collected = False
        else:
            node_ok.append('pvs')

        if len(node_nok) > 0:
            my_output.default(
                '- %s: collected [%s], missing [%s]' % (
                    node_name,
                    ', '.join(node_ok),
                    ', '.join(node_nok)
                )
            )
        else:
            my_output.default(
                '- %s: collected [%s]' % (
                    node_name,
                    ', '.join(node_ok)
                )
            )

    info = {}
    info['blks'] = blks
    info['lvs'] = lvs
    info['vgs'] = vgs
    info['pvs'] = pvs
    info['collected'] = lvm_info_collected
    info['orphan'] = orphan
    info['handlers'] = linux_handlers
    return info


def wipe_linux_lvm(cluster_name, k8s_handler, my_output, log_id=None, cache_enabled=True):
    my_output.default(
        'Collect linux level lvm state...',
        before_newline=True
    )

    linux_handlers = ocp_common.get_nodes_linux_handler(
        cluster_name,
        k8s_handler,
        log_id=log_id
    )
    
    node_names = k8s_handler.get_worker_nodes_name()
    blks = {}
    lvs = {}
    vgs = {}
    pvs = {}

    for node_name in node_names:
        blks[node_name] = linux_handlers[node_name].get_lsblks(cache_enabled=cache_enabled)
        lvs[node_name] = linux_handlers[node_name].get_lvs(include_pvc=True, cache_enabled=cache_enabled)
        vgs[node_name] = linux_handlers[node_name].get_vgs(cache_enabled=cache_enabled)
        pvs[node_name] = linux_handlers[node_name].get_pvs(cache_enabled=cache_enabled)

    success = True

    for node_name in node_names:
        my_output.default('Node [%s]' % (node_name), before_newline=True, underline=True)
        if lvs[node_name] is None:
            success = False
            my_output.error('No lvs information collected')
        else:
            for item in lvs[node_name]:
                if not item['is_pool']:
                    my_output.default('- delete lvs: %s' % (item['lv_path']))
                    lv_removed, cmd_output = linux_handlers[node_name].delete_lv_cmd(item['lv_path'])
                    my_output.default(cmd_output)
                    if not lv_removed:
                        my_output.error('Logical volume delete failed')
                        success = False

            for item in lvs[node_name]:
                if item['is_pool']:
                    my_output.default('- delete lv pool: %s' % (item['lv_dm_path']))
                    lv_removed, cmd_output = linux_handlers[node_name].delete_lv_cmd(item['lv_dm_path'])
                    my_output.default(cmd_output)
                    if not lv_removed:
                        my_output.error('Logical volume pool delete failed')
                        success = False

        if vgs[node_name] is None:
            success = False
            my_output.error('No vgs information collected')
        else:
            for item in vgs[node_name]:
                my_output.default('- deactivate vg: %s' % (item['vg_name']))
                vg_deactivated, cmd_output = linux_handlers[node_name].deactivate_vg_cmd(item['vg_name'])
                my_output.default(cmd_output)
                if not vg_deactivated:
                    my_output.error('Volume group deactive failed')
                    success = False
                    continue

                my_output.default('- delete vg: %s' % (item['vg_name']))
                vg_deleted, cmd_output = linux_handlers[node_name].delete_vg_cmd(item['vg_name'])
                my_output.default(cmd_output)
                if not vg_deleted:
                    my_output.error('Volume group delete failed')
                    success = False

        if pvs[node_name] is None:
            success = False
            my_output.error('No pv information collected')
        else:
            for item in pvs[node_name]:
                my_output.default('- delete pv: %s' % (item['pv_name']))
                pv_deleted, cmd_output = linux_handlers[node_name].delete_pv_cmd(item['pv_name'])
                my_output.default(cmd_output)
                if not pv_deleted:
                    my_output.error('Physical volume delete failed')
                    success = False

    return success


def print_linux_lvm(info, linux_output_handler):
    for node_name in info['blks']:
        if info['blks'][node_name] is not None:
            linux_output_handler.print_linux_lsblk(
                info['blks'][node_name],
                title=True,
                server=node_name
            )

        if info['pvs'][node_name] is not None:
            linux_output_handler.print_linux_pv(
                info['pvs'][node_name],
                title=True,
                server=node_name
            )

        if info['vgs'][node_name] is not None:
            linux_output_handler.print_linux_vg(
                info['vgs'][node_name],
                title=True,
                server=node_name
            )
        
        if info['lvs'][node_name] is not None:
            linux_output_handler.print_linux_lv(
                info['lvs'][node_name],
                title=True,
                server=node_name
            )

def get_devices_path(cluster_name, k8s_handler, devices, linux_output_handler, my_output, log_id=None):
    devices_paths = []
    device_names = []

    for device in devices:
        if device.startswith('pci-'):
            devices_paths.append('/dev/disk/by-path/%s' % (device))
            continue

        if device.startswith('/dev/'):
            device_names.append(device)
            continue

        device_names.append('/dev/%s' % (device))

    if len(device_names) == 0 and len(devices_paths) == 0:
        my_output.error('Unexpected number of target devices (0)')
        return None
    
    if len(device_names) == 0:
        return devices_paths
    
    my_output.default('Target block devices')
    for device_name in device_names:
        my_output.default('- %s' % (device_name))
    my_output.default('')

    lsblk = get_linux_lsblk(
        cluster_name, 
        k8s_handler, 
        my_output, 
        log_id=log_id, 
        device_names=device_names,
        include_disk_paths=True
    )
    if lsblk is None:
        return None
    
    for node_name in lsblk:
        if lsblk[node_name] is None:
            my_output.error('Failed to get lsblk on node [%s]' % (node_name))
            return None
        
        linux_output_handler.print_linux_lsblk(
            lsblk[node_name],
            title=True,
            server=node_name
        )
        if len(lsblk[node_name]) != len(device_names):
            my_output.error('Not all devices found')
            return None
        
        for device in lsblk[node_name]:
            if device['boot']:
                my_output.error('Boot device selected: %s' % (device['path']))
                return None

            if 'disk-path' not in device:
                my_output.error('Disk path not detected for: %s' % (device['path']))
                return None

    first_node = True
    for node_name in lsblk:
        if first_node:
            for device in lsblk[node_name]:
                devices_paths.append(
                    device['disk-path']
                )
            first_node = False
            continue

        for device in lsblk[node_name]:
            if device['disk-path'] not in devices_paths:
                my_output.error('Device paths are not the same across cluster nodes')
                return None

    return devices_paths
