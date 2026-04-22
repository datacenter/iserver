from lib import output_helper
from lib.workflow.ocp_cilium_cni import common as local_common
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
    my_output.default('OpenShift Workflow - Cilium - Approve install plan', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    if params['initialize']:
        params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
        if params is None:
            return False

    subscription = local_common.get_subscription(params, my_output, True)

    if subscription['installplan'] is None:
        my_output.default('No install plan found')
        return True
    
    if subscription['installplan']['approved']:
        my_output.default('Install plan already approved', before_newline=True)
        return True

    my_output.default('Install plan will be approved...', before_newline=True)

    success = params['k8s_handler'].approve_installplan(
        subscription['install_plan_namespace'],
        subscription['install_plan_name'],
        my_output=my_output
    )
    if not success:
        my_output.error('REST API failed')
        return False
    
    local_common.get_subscription(params, my_output, True, cache_enabled=False)
    return True
