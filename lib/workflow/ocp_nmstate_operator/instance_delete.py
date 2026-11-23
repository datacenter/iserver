from lib import output_helper
from lib.workflow.ocp_nmstate_operator import common as local_common
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

    ocp_common.print_title(params, my_output, 'Delete Instance')
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

    success = params['k8s_handler'].delete_node_network_configuration_policies(
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_nmstate(
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].wait_no_subscription_nmstate(
        my_output=my_output, 
        instance_only=True
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- nncp crds deleted')
    my_output.default('- nmstate instance deleted')
    return True