from lib import output_helper
from lib.workflow.ocp_intersight_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['channel', True, 'stable', 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cisco Intersight Operator - Create Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    if params['initialize']:
        params = ocp_common.workflow_init(params, my_output, log_id)
        if params is None:
            return False

    subscription = ocp_common.get_subscription(
        params['k8s_handler'],
        params['__default__']['name'],
        my_output=my_output
    )
    if subscription is not None:
        ocp_common.print_subscription(subscription, my_output)
        return True
    
    success = params['k8s_handler'].create_namespace(
        params['__default__']['namespace'],
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_operator_group(
        params['__default__']['namespace'], 
        name=params['__default__']['operator-group-name'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_intersight_subscription(
        params['__default__']['namespace'], 
        params['__default__']['name'], 
        channel=params['channel'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )
    if not success:
        return False

    subscription = ocp_common.get_subscription(
        params['k8s_handler'],
        params['__default__']['name'],
        my_output=my_output
    )

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Namespace created')
    my_output.default('- Operator Group created')
    my_output.default('- Cisco intersight operator installed')

    return True
