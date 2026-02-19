from lib.k8s import output as k8s_output
from lib.linux import output as linux_output
from lib import output_helper
from lib.workflow.ocp_lvm_operator import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'ssh-required' not in params:
        params['ssh-required'] = False

    if not isinstance(params['ssh-required'], bool):
        return None, 'ssh-required param must be true or false'
    
    if 'wipe' not in params:
        params['wipe'] = False

    if not isinstance(params['wipe'], bool):
        return None, 'wipe params must be true or false'

    if params['wipe']:
        params['ssh-required'] = True

    if 'confirmation' not in params:
        params['confirmation'] = True

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
        'wipe',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def check_resources(params, my_output, k8s_output_handler):
    params['lvmc'] = params['k8s_handler'].get_lvm_cluster(cache_enabled=False)
    if params['lvmc'] is None:
        my_output.default('LVM cluster already deleted')
        return params
    
    my_output.default('Checking lvm cluster resources...')

    resources = local_common.get_lvm_resources(
        params,
        my_output,
        title='Current Resources',
        pvc=True,
        snapshot=True,
        k8s_output_handler=k8s_output_handler
    )
    if resources is None:
        return None
    
    if resources['used']:
        my_output.default('')
        my_output.error('LVM resources found. Clean it up first.')
        return None

    return params


def wipe_devices(params, my_output, linux_output_handler, log_id):
    if not params['wipe']:
        return True
    
    if params['lvmc'] is None:
        return True
    
    my_output.default('Devices to be wiped', before_newline=True, underline=True)
    device_names = {}
    for device_class in params['lvmc']['info']['deviceClass']:
        for node_status in device_class['nodeStatus']:
            device_names[node_status['node']] = node_status['devices']
            my_output.default('- node [%s]: %s' % (node_status['node'], ', '.join(node_status['devices'])))

    if not params['confirmation'] or get_confirmation(title='Do you want to see linux lvm info first?', before_newline=True):
        lvm_resources = local_common.get_linux_lvm(
            params['cluster'], 
            params['k8s_handler'], 
            my_output, 
            log_id=log_id
        )
        local_common.print_linux_lvm(lvm_resources, linux_output_handler)

    if params['confirmation']:
        if not get_confirmation():
            return False

    wiped = local_common.wipe_linux_lvm(
        params['cluster'], 
        params['k8s_handler'], 
        my_output, 
        log_id=log_id
    )        
    if wiped:
        my_output.default('LVM wiped from servers', before_newline=True)
    else:
        my_output.default('LVM partially wiped from servers', before_newline=True)

    lvm_resources = local_common.get_linux_lvm(
        params['cluster'], 
        params['k8s_handler'], 
        my_output, 
        log_id=log_id
    )
    local_common.print_linux_lvm(lvm_resources, linux_output_handler)

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    linux_output_handler = linux_output.LinuxOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - LVM Operator - Delete Cluster', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, ssh_required=True)
    if params is None:
        return False

    if not local_common.is_lvm_ready(params, my_output, instance_required=False, ready_required=False):
        return True

    params = check_resources(params, my_output, k8s_output_handler)
    if params is None:
        return False
    
    success = params['k8s_handler'].delete_lvm_cluster(
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_lvm_storage_class(
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    if not wipe_devices(params, my_output, linux_output_handler, log_id):
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- LVM Cluster instance deleted')
    my_output.default('- LVM storage class deleted')

    return True
