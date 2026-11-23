from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_lvm_operator import common as local_common
from lib.workflow import ocp_common
from lib.workflow.ocp_lvm_operator import wipe


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


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete Cluster')
    params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True)
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

    if params['wipe'] or params['zap']:
        cparams = {}
        cparams['cluster'] = params['cluster']
        cparams['wipe'] = params['wipe']
        cparams['zap'] = params['zap']
        success = wipe.run(cparams, log_id=log_id)
        if not success:
            return False
                
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- LVM Cluster instance deleted')
    my_output.default('- LVM storage class deleted')
    if params['wipe'] or params['zap']:
        my_output.default('- LVM wiped')

    return True