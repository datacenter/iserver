from lib import output_helper
from lib.workflow.ocp_cilium_pnet import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'confirmation' not in params:
        params['confirmation'] = True

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
        'channel',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium Private Network - Enable Webhook', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not cilium_common.is_cilium(params, my_output):
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
