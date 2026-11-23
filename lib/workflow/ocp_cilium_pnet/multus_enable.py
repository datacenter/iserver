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

    params = local_common.initialize(params, my_output, 'Enable Multus', log_id)
    if params is None:
        return False

    if params['state']['multus']['enabled']:
        my_output.default('Private network multus %s' % (my_output.add_color('already enabled', 'Green')))
        return True
    
    success = params['k8s_handler'].enable_cilium_private_network_multus(
        my_output=my_output, 
        confirmation=params['confirmation']
    )
    if not success:
        return False  

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Private Network multus enabled and ready')
    return True