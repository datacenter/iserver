from lib import output_helper
from lib.workflow.ocp_cilium_pnet import common as local_common
from lib.workflow.ocp_cilium_pnet import wipe
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['wipe', True, False, 'bool', None, None, None, None]
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

    ocp_common.print_title(params, my_output, 'Disable')
    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return False
    
    if not params['k8s_handler'].is_cilium_private_network_enabled(cache_enabled=False):
        my_output.default('Private network already disabled')
        return True
    
    if params['wipe']:
        child_params = {}
        child_params['cluster'] = params['cluster']
        child_params['check-verbose'] = False
        child_params['confirmation'] = params['confirmation']
        success = wipe.run(child_params, log_id=log_id)
        if not success:
            return False
        
    if params['k8s_handler'].is_cilium_private_network_configured(cache_enabled=False):
        my_output.error('Unconfigure private networks crds first')
        return False

    success = params['k8s_handler'].disable_cilium_private_network(
        my_output=my_output, 
        confirmation=params['confirmation']
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Private Network feature disabled')

    return True