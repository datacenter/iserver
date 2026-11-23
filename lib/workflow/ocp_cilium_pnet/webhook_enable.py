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

    ocp_common.print_title(params, my_output, 'Enable Webhook')
    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return False
    
    if not params['k8s_handler'].is_cilium_private_network_enabled(cache_enabled=False):
        my_output.default('Private network %s' % (my_output.add_color('must be enabled first', 'Red')))
        return False

    my_output.default('Private network %s' % (my_output.add_color('enabled', 'Green')))

    if params['k8s_handler'].is_cilium_private_network_webhook_enabled(cache_enabled=True):
        my_output.default('Private network webhook already %s' % (my_output.add_color('enabled', 'Green')))
        if params['k8s_handler'].is_clusterwide_private_network_webhook(cache_enabled=False):
            my_output.default('Private network mutating webhook %s' % (my_output.add_color('found', 'Green')))
        else:
            my_output.default('Private network mutating webhook %s' % (my_output.add_color('not found', 'Red')))
            return False
        return True
    
    success = params['k8s_handler'].enable_cilium_private_network_webhook(
        my_output=my_output, 
        confirmation=params['confirmation']
    )
    if not success:
        return False  

    my_output.default('Wait for mutating webhook being created...')
    if not params['k8s_handler'].wait_clusterwide_private_network_webhook():
        my_output.error('timed out')
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Private Network webhook enabled and ready')

    return True