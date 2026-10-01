from lib import output_helper
from lib.workflow.ocp_splunk_operator import common as local_common
from lib.workflow import ocp_common as global_common
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

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Create Operator')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    success = ocp_common.create_operator(
        params,
        my_output
    )
    if not success:
        return False
    
    # if params['k8s_handler'].is_splunk_subscription(params['namespace'], params['name']):
    #     my_output.default('Splunk already created')
    # else:
        
    #     success = params['k8s_handler'].create_operator_group(
    #         params['namespace'], 
    #         name=params['operator-group-name'], 
    #         add_target_namespaces=True, 
    #         target_namespaces=[params['namespace']], 
    #         upgrade_strategy=None, 
    #         confirmation=params['confirmation'], 
    #         my_output=my_output, 
    #         wait=True
    #     )
    #     if not success:
    #         return False

    #     success = params['k8s_handler'].create_splunk_subscription(
    #         params['namespace'], 
    #         params['name'], 
    #         channel=params['channel'],
    #         confirmation=params['confirmation'], 
    #         my_output=my_output, 
    #         wait=True            
    #     )
    #     if not success:
    #         return False

    if params['__default__']['license-at-splunk']:
        success = params['k8s_handler'].update_splunk_subscription_license(
            params['__default__']['name'],
            confirmation=params['confirmation'],
            my_output=my_output
        )
        if not success:
            return False

    if params['__default__']['role-binding']:
        success = params['k8s_handler'].create_splunk_subscription_role_binding(
            params['__default__']['name'],
            params['__default__']['role-binding-name'],
            my_output=my_output,
            confirmation=params['confirmation']
        )
        if not success:
            return False

    # subscription = global_common.get_subscription(
    #     params['k8s_handler'], 
    #     params['name'], 
    #     my_output=my_output
    # )
    # if subscription is None:
    #     return True
    
    # my_output.default('')
    # my_output.default('Completed tasks')
    # my_output.default('- Namespace created')
    # my_output.default('- Operator Group created')
    # my_output.default('- Splunk Operator installed')
    # if params['license-at-splunk']:
    #     my_output.default('- Splunk license accept at splunk.com set')
    # if params['role-binding']:
    #     my_output.default('- Role binding created')

    return True
