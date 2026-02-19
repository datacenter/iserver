from lib import output_helper
from lib.workflow.ocp_cilium_timescape import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'route' not in params:
        params['route'] = True

    if not isinstance(params['route'], bool):
        return None, 'route param must be true or false'
    
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
        'route',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Enable Timescape', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not cilium_common.is_cilium(params, my_output):
        return False

    if params['k8s_handler'].is_cilium_timescape_enabled(cache_enabled=False):
        my_output.default('Timescape already enabled')
    else:
        success = params['k8s_handler'].enable_cilium_timescape(
            my_output=my_output, 
            confirmation=params['confirmation'],
            wait=True
        )
        if not success:
            return False

    if params['route']:
        success = params['k8s_handler'].create_cilium_timescape_route(
            confirmation=params['confirmation'], 
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
    
    route = params['k8s_handler'].get_cilium_timescape_route()

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Timescape feature enabled')
    if params['route']:
        my_output.default('- ui: %s' % (route))

    return True
