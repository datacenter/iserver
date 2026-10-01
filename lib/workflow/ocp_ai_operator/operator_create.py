from lib import output_helper
from lib.workflow.ocp_ai_operator import common as local_common
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

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['__default__']['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is not None:
        my_output.default('Data Science (AI) Operator already created')
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
        add_target_namespaces=False,
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_ods_subscription(
        params['__default__']['namespace'], 
        params['__default__']['name'], 
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

    if not params['k8s_handler'].wait_any_auth(
        my_output=my_output
    ):
        return False
    
    auths = params['k8s_handler'].get_auths(cache_enabled=False)
    for auth in auths:
        success = params['k8s_handler'].wait_auth_ready(
            auth['name'],
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