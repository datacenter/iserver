from lib import output_helper
from lib import ip_helper
from lib.workflow import ocp_common as global_common
from lib.k8s import output as k8s_output
from lib.workflow.ocp_local_storage_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    params['ssh-required'] = True

    if 'device' not in params:
        params['device'] = []

    if not isinstance(params['device'], list):
        return None, 'device param must list of strings'

    for item in params['device']:
        if not isinstance(item, str):
            return None, 'device param must list of strings'

        if len(item.split(':')) > 1:
            device_name = ':'.join(item.split(':')[1:])
            if not device_name.startswith('wwn-') and not device_name.startswith('nvme-'):
                return None, 'node device should be in wwn- or nvme- format'
            
    if 'sc' not in params:
        params['sc'] = 'local-sc'

    if not isinstance(params['sc'], str):
        return None, 'sc param must be string'
    
    if 'volume' not in params:
        params['volume'] = 'block'

    if not isinstance(params['volume'], str):
        return None, 'volume param must be string'

    if params['volume'] not in ['block', 'fs']:
        return None, 'volume param must be one of block and fs values'

    if 'fstype' not in params:
        params['fstype'] = 'ext4'

    if not isinstance(params['fstype'], str):
        return None, 'fstype param must be string'

    if 'max' not in params:
        params['max'] = -1

    if not isinstance(params['max'], int):
        return None, 'max param must be int'

    if params['max'] == 0:
        return None, 'max param must be -1 or positive'

    if params['max'] < -1:
        return None, 'max param must be -1 or positive'

    if 'limit' not in params:
        params['limit'] = []

    if not isinstance(params['limit'], list):
        return None, 'limit param must list of strings'

    for item in params['limit']:
        if len(item.split(':')) != 2:
            return None, 'limit items must be in key:value format'
        
        limit_key = item.split(':')[0]
        limit_value = item.split(':')[1]

        if limit_key not in ['type', 'mechanical', 'minsize', 'maxsize', 'model', 'vendor']:
            return None, 'supported limit item key: type, mechanical, minsize, maxsize, model, vendor'
        
        if limit_key == 'type':
            if limit_value not in ['disk', 'part']:
                return None, 'supported limit values for key type: disk, part'
            
        if limit_key == 'mechanical':
            if limit_value not in ['rotational', 'nonrotational']:
                return None, 'supported limit values for key mechinical: rotational, nonrotational'
            
    if 'confirmation' not in params:
        params['confirmation'] = False

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
    
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
        'ssh-required',
        'device',
        'sc',
        'volume',
        'fstype',
        'max',
        'limit',
        'confirmation',
        'verbose',
        'check-verbose'
    ]  
    return local_common.sanitize_params(params, allowed_keys), None


def validate_values(params, my_output, log_id):
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('Collect cluster state and validate input values', before_newline=True, underline=True)

    my_output.default('- get kubernetes node names')
    node_names = params['k8s_handler'].get_nodes_name()
    if node_names is None:
        my_output.error('Failed to get node names')
        return None
    
    if len(node_names) == 0:
        my_output.error('Unexpected no nodes found')
        return None
    
    my_output.default('- get linux level block devices for all nodes')
    params['lsblk'] = global_common.get_linux_lsblk(
        params['cluster'],
        params['k8s_handler'],
        log_id=log_id,
        include_disk_paths=True
    )
    if params['lsblk'] is None:
        my_output.error('Failed to get node block devices information')
        return None

    my_output.default('- get local volumes')
    params['local_volume'] = params['k8s_handler'].get_local_volumes(cache_enabled=False)
    if params['local_volume'] is None:
        my_output.error('Unexpected error in getting information')
        return None
    
    my_output.default('- get local volume sets')
    params['local_volume_set'] = params['k8s_handler'].get_local_volume_sets(pv_info=True, cache_enabled=False)
    if params['local_volume_set'] is None:
        my_output.error('Unexpected error in getting information')
        return None

    my_output.default('- get local volume discovery')
    params['local_volume_discovery'] = params['k8s_handler'].get_local_volume_discoveries(cache_enabled=False)
    if params['local_volume_discovery'] is None:
        my_output.error('Unexpected error in getting information')
        return None

    if len(params['device']) == 0:
        params['volume-mode'] = 'discovery-all'
        params['discovery-nodes'] = node_names
        my_output.default('- detected volume create mode: %s' % (my_output.add_color(params['volume-mode'], 'Blue')))

        if len(params['local_volume']) > 0:
            my_output.default('Local Volume already defined', before_newline=True)
            k8s_output_handler.print_local_volumes(params['local_volume'])
            return None
    
        if len(params['local_volume_discovery']) > 0:
            my_output.default('Local Volume Discovery already defined', before_newline=True)
            k8s_output_handler.print_local_volume_discoveries(params['local_volume_discovery'])

        if len(params['local_volume_set']) > 0:
            my_output.default('Local Volume Set already defined', before_newline=True)
            k8s_output_handler.print_local_volume_sets(params['local_volume_set'])

            for lvs in params['local_volume_set']:
                if lvs['pv'] is not None and len(lvs['pv']) > 0:
                    k8s_output_handler.print_pvs(lvs['pv'])
        
        my_output.default('- state and values verified')
        return params
    
    volume_mode = None

    params['discovery-nodes'] = []
    params['explicit-nodes'] = []
    params['explicit-devices'] = {}
    for device in params['device']:
        node_name = None
        device_name = None
        if len(device.split(':')) == 1:
            volume_mode = 'discovery-node'
            node_name = device
            if volume_mode is not None and volume_mode != 'discovery-node':
                my_output.error('Consistency required in volume mode selection')
                return None
            
            params['discovery-nodes'].append(node_name)
        else:
            volume_mode = 'explicit'
            node_name = device.split(':')[0]
            device_name = ':'.join(device.split(':')[1:])
            if volume_mode is not None and volume_mode != 'explicit':
                my_output.error('Consistency required in volume mode selection')
                return None
            
            found = False
            for local_volume in params['local_volume']:
                if node_name in local_volume['node']:
                    if device_name in local_volume['device_path']:
                        my_output.default(
                            'Device [%s] on node [%s] already defined in local volume [%s]' % (
                                device_name,
                                node_name,
                                local_volume['name']
                            )
                        )
                        found = True

            if found:
                continue

            if node_name not in params['explicit-nodes']:
                params['explicit-nodes'].append(node_name)

            if node_name not in params['explicit-devices']:
                params['explicit-devices'][node_name] = []

            params['explicit-devices'][node_name].append(device_name)

        if node_name not in node_names:
            my_output.error('Unknown node name: %s' % (node_name))
            return None
        
        if node_name not in params['lsblk'] or params['lsblk'][node_name] is None:
            my_output.error('No block device information collected for node name: %s' % (node_name))
            return None
        
        if device_name is not None and device.startswith('wwn-'):
            found = False
            for block_device in params['lsblk'][node_name]:
                if 'disk-wwn' not in block_device:
                    continue

                if block_device['disk-wwn'] is None:
                    continue

                if block_device['disk-wwn'] == '/dev/disk/by-id/%s' % device_name:
                    found = True

            if not found:
                my_output.error('No wwn block device [%s] found on node [%s]' % (device_name, node_name))
                return None
            
        if device_name is not None and device.startswith('nvme-'):
            found = False
            for block_device in params['lsblk'][node_name]:
                if 'disk-wwn' not in block_device:
                    continue

                if block_device['disk-wwn'] is None:
                    continue

                if block_device['disk-wwn'] == '/dev/disk/by-wwn/%s' % device_name:
                    found = True

            if not found:
                my_output.error('No nvme device [%s] found on node [%s]' % (device_name, node_name))
                return None
            
    if volume_mode is None:
        my_output.error('Unexpected volume mode detection failure')
        return None
    
    params['volume-mode'] = volume_mode
    my_output.default('- detected volume create mode: %s' % (my_output.add_color(params['volume-mode'], 'Blue')))

    if params['volume-mode'] == 'discovery-node':
        if len(params['discovery-nodes']) == 0:
            my_output.error('Unexpected no discovery nodes defined')
            return None
        
        if len(params['local_volume']) > 0:
            my_output.default('Local Volume already defined', before_newline=True)
            k8s_output_handler.print_local_volumes(params['local_volume'])
            return None
    
        if len(params['local_volume_discovery']) > 0:
            my_output.default('Local Volume Discovery already defined', before_newline=True)
            k8s_output_handler.print_local_volume_discoveries(params['local_volume_discovery'])

        if len(params['local_volume_set']) > 0:
            my_output.default('Local Volume Set already defined', before_newline=True)
            k8s_output_handler.print_local_volume_sets(params['local_volume_set'])
        
            for lvs in params['local_volume_set']:
                if lvs['pv'] is not None and len(lvs['pv']) > 0:
                    k8s_output_handler.print_pvs(lvs['pv'])

        if len(params['local_volume_discovery']) > 0 or len(params['local_volume_set']) > 0:
            return None

    if params['volume-mode'] == 'explicit':
        if len(params['local_volume_discovery']) > 0:
            my_output.default('Local Volume Discovery already defined', before_newline=True)
            k8s_output_handler.print_local_volume_discoveries(params['local_volume_discovery'])

        if len(params['local_volume_set']) > 0:
            my_output.default('Local Volume Set already defined', before_newline=True)
            k8s_output_handler.print_local_volume_sets(params['local_volume_set'])

            for lvs in params['local_volume_set']:
                if lvs['pv'] is not None and len(lvs['pv']) > 0:
                    k8s_output_handler.print_pvs(lvs['pv'])

        if len(params['local_volume_discovery']) > 0 or len(params['local_volume_set']) > 0:
            return None

    my_output.default('- state and values verified')

    return params


def label_discovery_nodes(params, my_output):
    my_output.default('Label Discovery Nodes', before_newline=True, underline=True)
    my_output.default('- node label: cluster.ocs.openshift.io/openshift-storage=""')
    for node_name in params['discovery-nodes']:
        my_output.default('- node: %s' % (node_name))
        if not params['k8s_handler'].add_node_label(node_name, 'cluster.ocs.openshift.io/openshift-storage', ''):
            my_output.error('REST API failed')
            return False
    
    return True


def label_explicit_nodes(params, my_output):
    my_output.default('Label Nodes', before_newline=True, underline=True)
    my_output.default('- node label: cluster.ocs.openshift.io/openshift-storage=""')
    for node_name in params['explicit-nodes']:
        my_output.default('- node: %s' % (node_name))
        if not params['k8s_handler'].add_node_label(node_name, 'cluster.ocs.openshift.io/openshift-storage', ''):
            my_output.error('REST API failed')
            return False
    
    return True


def create_local_volume_discovery(params, my_output, k8s_output_handler, name='auto-discover-devices'):
    success = params['k8s_handler'].create_local_volume_discovery(
        params['namespace'],
        name,
        params['discovery-nodes'],
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return None

    object_filter = []
    object_filter.append('nodes:%s' % (','.join(params['discovery-nodes'])))
    params['discovery_results'] = params['k8s_handler'].get_local_volume_discovery_results(
        object_filter=object_filter,
        cache_enabled=False
    )

    k8s_output_handler.print_local_volume_discovery_results(
        params['discovery_results'],
        unavailable=False
    )

    return params


def get_expected_local_volume_set_outcome(params, my_output):
    params['available-device'] = {}
    for node_name in params['discovery-nodes']:
        params['available-device'][node_name] = None
        for result in params['discovery_results']:
            if result['node'] == node_name:
                params['available-device'][node_name] = len(result['available_devices'])
                break

        if params['available-device'][node_name] is None:
            my_output.error('Unexpected no available device for node: %s' % (node_name))
            return None
    
    params['device-limit'] = {}
    params['expected-device'] = {}
    params['expected-device-count'] = 0
    for node_name in params['discovery-nodes']:
        params['device-limit'][node_name] = params['max']
        if params['max'] < 0:
            params['expected-device'][node_name] = params['available-device'][node_name]
        else:
            params['expected-device'][node_name] = min(
                params['available-device'][node_name],
                params['max']
            )

        params['expected-device-count'] += params['expected-device'][node_name]

    display_items = []
    for node_name in params['discovery-nodes']:
        display_item = {}
        display_item['node'] = node_name
        display_item['avilable-device'] = params['available-device'][node_name]
        display_item['device-limit'] = params['device-limit'][node_name]
        display_item['expected-device'] = params['expected-device'][node_name]
        display_items.append(display_item)

    order = [
        'node',
        'avilable-device',
        'device-limit',
        'expected-device'
    ]

    headers = [
        'Node',
        'Available Devices',
        'Max Device Count',
        'Expected Devices'
    ]

    my_output.my_table(
        display_items,
        order=order,
        headers=headers,
        row_separator=False,
        allow_order_subkeys=True,
        underline=True,
        table=True
    )

    my_output.default(
        'Total expected devices to be provisioned: %s' % (params['expected-device-count']), 
        before_newline=True, 
        after_newline=True
    )
    return params


def create_local_volume_set(params, my_output, k8s_output_handler):
    params = get_expected_local_volume_set_outcome(params, my_output)
    if params is None:
        return None

    success = params['k8s_handler'].create_local_volume_set(
        params['namespace'],
        'my-local-disks',
        params['discovery-nodes'],
        params['volume'],
        params['sc'],
        limits=params['limit'],
        max_count=params['max'],
        fstype=params['fstype'],
        expected_outcome=params['expected-device-count'],
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return None
        
    local_volume_sets = params['k8s_handler'].get_local_volume_sets(pv_info=True, cache_enabled=False)
    if local_volume_sets is None:
        my_output.error('Unexpected failure in local volume set get')
        return None
    
    k8s_output_handler.print_local_volume_sets(local_volume_sets)
    for lvs in local_volume_sets:
        if lvs['pv'] is not None and len(lvs['pv']) > 0:
            k8s_output_handler.print_pvs(lvs['pv'])

    return True


def create_local_volume(params, my_output, k8s_output_handler):
    lv_names = []
    for node_name in params['explicit-devices']:
        for device in params['explicit-devices'][node_name]:
            lv_name = 'local-disks-%s' % (ip_helper.get_short_uuid())
            lv_names.append(lv_name)

            if device.startswith('wwn-'):
                success = params['k8s_handler'].create_local_volume(
                    params['namespace'],
                    lv_name,
                    [node_name],
                    params['volume'],
                    ['/dev/disk/by-id/%s' % (device)],
                    params['sc'],
                    confirmation=params['confirmation'],
                    my_output=my_output,
                    wait=True
                )
            else:
                success = params['k8s_handler'].create_local_volume(
                    params['namespace'],
                    lv_name,
                    [node_name],
                    params['volume'],
                    ['/dev/disk/by-id/%s' % (device)],
                    params['sc'],
                    confirmation=params['confirmation'],
                    my_output=my_output,
                    wait=True
                )

            if not success:
                return False

    pvs = params['k8s_handler'].get_pvs(
        object_filter=['local-volumes:%s' % (','.join(lv_names))],
        cache_enabled=False
    )
    if pvs is None:
        my_output.error('Failed to get persistent volumes')
        return False
    
    k8s_output_handler.print_pvs(pvs)

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    my_output.default('OpenShift Workflow - Local Storage Operator - Create Local Volume', before_newline=True, after_newline=True, double_underline=True)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, ssh_required=params['ssh-required'])
    if params is None:
        return False

    state = local_common.check_state(
        params, 
        my_output,
        check_ready=True
    )
    if not state['installed'] or not state['ready']:
        return False
    
    params = validate_values(params, my_output, log_id)
    if params is None:
        return False

    if params['volume-mode'] in ['discovery-all', 'discovery-node']:
        if not label_discovery_nodes(params, my_output):
            return False
        
        params = create_local_volume_discovery(params, my_output, k8s_output_handler)
        if params is None:
            return False

        if not create_local_volume_set(params, my_output, k8s_output_handler):
            return False

    if params['volume-mode'] == 'explicit':
        if len(params['explicit-nodes']) == 0:
            my_output.default('Nothing to do', before_newline=True)
            return True
        
        if not label_explicit_nodes(params, my_output):
            return False

        if not create_local_volume(params, my_output, k8s_output_handler):
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Volumes created')

    return True
