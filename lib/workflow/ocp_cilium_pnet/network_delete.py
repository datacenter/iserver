from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_pnet import common as local_common
from menu.common import get_confirmation
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, 'Delete', log_id)
    if params is None:
        return False

    network_info = local_common.get_private_network(
        params,
        params['name'],
        my_output=my_output,
        k8s_output_handler=k8s_output_handler
    )
    if network_info is None:
        return True
    
    if params['confirmation']:
        if not get_confirmation():
            return False
    
    success = params['k8s_handler'].delete_clusterwide_private_network(
        params['name'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Private Network deleted')
    return True