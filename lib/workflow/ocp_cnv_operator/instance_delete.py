from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cnv_operator import common as local_common
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
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete HyperConverged Instance')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    subscription = ocp_common.get_subscription(
        params['k8s_handler'],
        params['__default__']['name'],
        my_output=my_output,
        expected=False,
    )
    if subscription is None:
        return True

    if params['k8s_handler'].get_hyperconverged(cache_enabled=False) is None:
        my_output.default('No hyperconverged instance found')
        return True
    
    if local_common.is_cnv_used(params['k8s_handler'], k8s_output_handler, my_output):
        return False
    
    success = params['k8s_handler'].delete_hyperconverged(
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Hyperconverged instance deleted')
    return True