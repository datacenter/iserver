from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_splunk_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    instance_rules = [
        ['name', False, None, 'str', None, None, None, None]
    ]

    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['instance', False, None, 'list-of-dict', 1, None, None, None]
    ]

    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete Instance')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_deployment(params['__default__']['namespace'], params['__default__']['deployment'], cache_enabled=False):
        my_output.error('Splunk operator must be installed first')
        return False

    for instance in params['instance']:
        success = params['k8s_handler'].delete_splunk_standalone_route(
            params['__default__']['namespace'], 
            instance['name'], 
            my_output=my_output
        )
        if not success:
            return False

        success = params['k8s_handler'].delete_splunk_standalone(
            params['__default__']['namespace'], 
            instance['name'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Standalone instance deleted')
    return True
