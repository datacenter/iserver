import os
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_ai_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'channel' not in params:
        params['channel'] = 'stable'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'channel',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Data Science (AI) - Create Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is not None:
        my_output.default('Data Science (AI) Operator already created')
        return True
    
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
        confirmation=params['confirmation'], 
        add_target_namespaces=False,
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_ods_subscription(
        params['namespace'], 
        params['name'], 
        channel=params['channel'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )
    if not success:
        return False

    initialization = params['k8s_handler'].wait_any_data_science_cluster_initialization(
        my_output=my_output
    )
    if initialization is None:
        return False
    
    success = params['k8s_handler'].wait_data_science_cluster_initialization_ready(
        initialization,
        my_output=my_output
    )
    if not success:
        return False

    auth = params['k8s_handler'].wait_any_auth(
        my_output=my_output
    )
    if auth is None:
        return False
    
    success = params['k8s_handler'].wait_auth_ready(
        auth,
        my_output=my_output
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Namespace created')
    my_output.default('- Operator Group created')
    my_output.default('- Data Science (AI) Operator installed')
    my_output.default('- Data Science Cluster Initialization ready')
    my_output.default('- Auth ready')

    return True
