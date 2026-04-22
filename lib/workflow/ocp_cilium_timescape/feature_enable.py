from lib import output_helper
from lib.workflow.ocp_cilium_cni import common as cilium_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['route', True, True, 'bool', None, None, None, None],
        ['insecure', True, False, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=cilium_common.get_default_params()), None

def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Enable Timescape', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id)
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

        route = params['k8s_handler'].get_cilium_timescape_route(return_info=True, cache_enabled=False)

        success = params['k8s_handler'].update_route_security_mode(
            route['namespace'],
            route['name'],
            not params['insecure'],
            confirmation=params['confirmation'], 
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Timescape feature enabled')
    if params['route']:
        my_output.default('- ui: %s' % (route['route']))

    return True
