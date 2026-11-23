from lib import output_helper
from lib.workflow.ocp_tetragon_operator import common as local_common
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

    ocp_common.print_title(params, my_output, 'Wipe')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_tetragon_subscription(params['__default__']['namespace'], params['__default__']['name']):
        my_output.default('Tetragon Operator %s' % (my_output.add_color('not installed', 'Red')))
        return True
    
    success = params['k8s_handler'].delete_alert_rules(my_output=my_output, wait=True)
    if not success:
        return False

    success = params['k8s_handler'].delete_sandbox_policys(my_output=my_output, wait=True)
    if not success:
        return False

    success = params['k8s_handler'].delete_sandbox_policy_namespaceds(my_output=my_output, wait=True)
    if not success:
        return False
    
    # success = params['k8s_handler'].delete_tetragon_network_policys(my_output=my_output, wait=True)
    # if not success:
    #     return False
    
    # success = params['k8s_handler'].delete_tetragon_network_policy_namespaceds(my_output=my_output, wait=True)
    # if not success:
    #     return False
    
    success = params['k8s_handler'].delete_tracing_policys(my_output=my_output, wait=True)
    if not success:
        return False
    
    success = params['k8s_handler'].delete_tracing_policy_namespaceds(my_output=my_output, wait=True)
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Tetragon resources deleted')
    return True