from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common
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

    ocp_common.print_title(params, my_output, 'Delete Forklift Controller Instance')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True

    instances = params['k8s_handler'].get_forklift_controllers(cache_enabled=False)
    if instances is None:
        my_output.error('Failed to get forklift instances')
        return False
    
    if len(instances) == 0:
        my_output.default('No forklift controller instance found', before_newline=True)
        return True

    if not local_common.is_mtv_unconfigured(params, my_output, k8s_output_handler):
        return False
    
    success = params['k8s_handler'].delete_forklift_controller(
        instances[0]['namespace'], 
        instances[0]['name'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- forklift controller instance deleted')

    return True