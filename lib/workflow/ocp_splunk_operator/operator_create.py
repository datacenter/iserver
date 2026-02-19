from lib import output_helper
from lib.workflow.ocp_splunk_operator import common as local_common
from lib.workflow import ocp_common as global_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'channel' not in params:
        params['channel'] = 'stable'

    if 'confirmation' not in params:
        params['confirmation'] = False

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'channel',
        'confirmation',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Splunk Operator - Create Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['k8s_handler'].is_splunk_subscription(params['namespace'], params['name']):
        my_output.default('Splunk already created')
    else:
        success = params['k8s_handler'].create_namespace(
            params['namespace'],
            confirmation=params['confirmation'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
        
        success = params['k8s_handler'].create_operator_group(
            params['namespace'], 
            name=params['operator-group-name'], 
            add_target_namespaces=True, 
            target_namespaces=[params['namespace']], 
            upgrade_strategy=None, 
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].create_splunk_subscription(
            params['namespace'], 
            params['name'], 
            channel=params['channel'],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True            
        )
        if not success:
            return False

    if params['license-at-splunk']:
        success = params['k8s_handler'].update_splunk_subscription_license(
            params['name'],
            confirmation=params['confirmation'],
            my_output=my_output
        )
        if not success:
            return False

    if params['role-binding']:
        success = params['k8s_handler'].create_splunk_subscription_role_binding(
            params['name'],
            params['role-binding-name'],
            my_output=my_output,
            confirmation=params['confirmation']
        )
        if not success:
            return False

    subscription = global_common.get_subscription(
        params['k8s_handler'], 
        params['name'], 
        my_output=my_output
    )
    if subscription is None:
        return True
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Namespace created')
    my_output.default('- Operator Group created')
    my_output.default('- Splunk Operator installed')
    if params['license-at-splunk']:
        my_output.default('- Splunk license accept at splunk.com set')
    if params['role-binding']:
        my_output.default('- Role binding created')

    return True
