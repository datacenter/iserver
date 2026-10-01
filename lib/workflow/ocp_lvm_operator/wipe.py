from lib import output_helper
from lib.workflow.ocp_lvm_operator import common as local_common
from lib.workflow import ocp_common
from lib.workflow.linux_lvm import wipe
from lib.workflow.linux_disk import zap


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['wipe', True, True, 'bool', None, None, None, None],
        ['zap', True, True, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def wipe_devices(params, my_output, log_id):
    if not params['wipe']:
        return True
    
    my_output.default('Wipe LVM', before_newline=True, underline=True)
    linux_handlers = ocp_common.get_nodes_linux_handler(
        params['cluster'],
        params['k8s_handler'],
        log_id=log_id
    )
    if linux_handlers is None:
        return False
    
    for node_name in linux_handlers:
        success = wipe.run(linux_handlers[node_name], my_output, server_name=node_name, break_on_error=True)
        if not success:
            return False
        
    return True


def zap_devices(params, log_id):
    if not params['zap']:
        return True
    
    servers = ocp_common.get_nodes_linux_server(
        params['cluster'],
        params['k8s_handler'],
        log_id=log_id
    )
    if servers is None:
        return False
    
    child_params = {}
    child_params['cluster'] = params['cluster']
    child_params['server'] = servers
    child_params['fstype'] = ['LVM2']
    child_params['confirmation'] = params['confirmation']
    
    success = zap.run(
        child_params,
        log_id=log_id
    )
    return success


def check_lvm_children(params, my_output, log_id):
    if not params['wipe'] or not params['zap']:
        return
    
    my_output.default('Check stale lvm children devices', before_newline=True, underline=True)
    found = False

    lsblk = local_common.get_linux_lsblk(
        params['cluster'], 
        params['k8s_handler'], 
        my_output, 
        log_id=log_id, 
        include_disk_paths=True
    )
    if lsblk is None:
        my_output.error('Failed to get block devices, error no false-positive')
        return
    
    for node_name in lsblk:
        if lsblk[node_name] is None:
            my_output.error('Failed to get lsblk on node [%s]' % (node_name))
            return
        
        for device in lsblk[node_name]:
            if device['lvm_children']:
                found = True
                my_output.default('- node %s device %s has lvm children devices' % (node_name, device['name']))

    if found:
        my_output.default('[%s] Consider power reload of the nodes with stale lvm state' % (my_output.add_color('WARNING', 'Red')))
    else:
        my_output.default('No stale lvm children devices found')

    return


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Wipe LVM')
    params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True)
    if params is None:
        return False

    if not local_common.is_lvm_ready(params, my_output, instance_allowed=False, instance_required=False, ready_required=False):
        return False
    
    if not wipe_devices(params, my_output, log_id):
        return False
    
    if not zap_devices(params, log_id):
        return False

    check_lvm_children(params, my_output, log_id)
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- LVM wiped')
    return True