from lib import output_helper
from lib.workflow.ocp_cilium_pnet import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Wipe')
    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return False
    
    if not params['k8s_handler'].is_cilium_private_network_enabled(cache_enabled=False):
        my_output.default('Private network disabled')
        return True

    if not params['k8s_handler'].delete_clusterwide_private_networks(my_output=my_output, wait=True):
        return False
    
    if not params['k8s_handler'].delete_private_network_endpoint_slices(my_output=my_output, wait=True):
        return False

    if not params['k8s_handler'].delete_private_network_external_endpoints(my_output=my_output, wait=True):
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Private Network crds deleted')
    return True