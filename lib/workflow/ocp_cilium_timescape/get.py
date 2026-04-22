import yaml
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_cni import common as cilium_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['view', False, None, 'list-of-str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=cilium_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Get Timescape', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return False

    if not params['k8s_handler'].is_cilium_timescape_enabled(cache_enabled=False):
        my_output.default('Timescape %s' % (my_output.add_color('disabled', 'Red')))
        return True
    
    config = params['k8s_handler'].get_cilium_timescape_config(cache_enabled=False)
    if config is None:
        my_output.error('Failed to get timescape configuration')
        return False

    resources = params['k8s_handler'].get_cilium_timescape_resources(cache_enabled=False)
    ready = params['k8s_handler'].is_cilium_timescape_ready(resources=resources)
    route = params['k8s_handler'].get_cilium_timescape_route(return_info=True)

    if 'details' in params['view']:
        my_output.default('Cilium configuration', before_newline=True, after_newline=True, underline=True)
        my_output.default(yaml.dump(config), wrap='~~~')

        if resources['pod'] is not None:
            k8s_output_handler.print_pods_state(resources['pod'])

        if resources['service'] is not None:
            k8s_output_handler.print_services(resources['service'])

        if resources['endpoint'] is not None:
            k8s_output_handler.print_endpoints(resources['endpoint'])

    my_output.default('State summary', before_newline=True)
    my_output.default('- %s' % (my_output.add_color('enabled', 'Green')))
    if ready:
        my_output.default('- resources %s' % (my_output.add_color('ready', 'Green')))
    else:
        my_output.default('- resources %s ready' % (my_output.add_color('not', 'Red')))
    
    if route is None:
        my_output.default('- %s to ui' % (my_output.add_color('no route', 'Red')))
    else:
        if route['insecure']:
            my_output.default('- ui: %s [insecure]' % (route['route']))
        else:
            my_output.default('- ui: %s' % (route['route']))

    return True
