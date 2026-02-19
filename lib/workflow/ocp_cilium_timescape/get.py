import yaml
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_timescape import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
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
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Get Timescape', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not cilium_common.is_cilium(params, my_output):
        return False

    if not params['k8s_handler'].is_cilium_timescape_enabled(cache_enabled=False):
        my_output.default('Timescape disabled')
        return True
    
    config = params['k8s_handler'].get_cilium_timescape_config(cache_enabled=False)
    if config is None:
        my_output.error('Failed to get timescape configuration')
        return False
    
    my_output.default('Cilium configuration', before_newline=True, after_newline=True, underline=True)
    my_output.default(yaml.dump(config), wrap='~~~')

    resources = params['k8s_handler'].get_cilium_timescape_resources(cache_enabled=False)
    ready = params['k8s_handler'].is_cilium_timescape_ready(resources=resources)

    if resources['pod'] is not None:
        k8s_output_handler.print_pods_state(resources['pod'])

    if resources['service'] is not None:
        k8s_output_handler.print_services(resources['service'])

    if resources['endpoint'] is not None:
        k8s_output_handler.print_endpoints(resources['endpoint'])

    route = params['k8s_handler'].get_cilium_timescape_route()
    
    my_output.default('Timescape summary', before_newline=True)
    my_output.default('- enabled')
    if ready:
        my_output.default('- resources ready')
    else:
        my_output.default('- resources %s ready' % (my_output.add_color('not', 'Red')))
    
    if route is None:
        my_output.default('- no route to ui')
    else:
        my_output.default('- ui: %s' % (route))

    return True
