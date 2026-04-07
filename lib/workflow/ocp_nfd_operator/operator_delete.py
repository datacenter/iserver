from lib import output_helper
from lib.workflow.ocp_nfd_operator import common as local_common
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
    my_output.default('OpenShift Workflow - Node Feature Discover Operator - Delete Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    subscription = ocp_common.get_subscription(
        params['k8s_handler'],
        params['__default__']['name'],
        my_output=my_output
    )
    if subscription is not None:
        success = params['k8s_handler'].delete_node_feature_discoveries(
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].delete_nfd_subscription(
            subscription['namespace'],
            subscription['name'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    success = params['k8s_handler'].delete_operator_group_in_namespace(
        params['__default__']['namespace'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    if params['__default__']['delete-namespace']:
        success = params['k8s_handler'].delete_namespace(
            params['__default__']['namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- NFD instances deleted')
    my_output.default('- Subscription and csv deleted')
    my_output.default('- Operator Group deleted')
    my_output.default('- Namespace deleted')

    return True
