from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.k8s import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['__id__', True, None, None, None, None, None, None],
        ['namespace', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['label', True, None, 'dict', None, None, None, None],
        ['node', True, None, 'str', None, None, None, None],
        ['app', False, None, 'str', None, None, ['netshoot', 'nginx'], None],
        ['network', False, [], 'list-of-str', None, None, None, None],
        ['udn-port', False, [], 'list-of-str', None, None, None, None]
    ]

    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params

    return ocp_common.sanitize_params(params, allowed_keys, add_defaults=False, copy_handler=False), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Pod - Create')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    body = params['k8s_handler'].get_pod_template_body(params)
    if body is None:
        my_output.error('Exception in processing input data')
        return False
    
    success = params['k8s_handler'].create_pod(
        body,
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=params['wait']
    )
    if not success:
        return False

    info = params['k8s_handler'].get_pod(
        params['namespace'], 
        params['name'], 
        cache_enabled=False
    )
    k8s_output_handler.print_pods_state([info])
    k8s_output_handler.print_pods_net([info])
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- pod created')
    return True
