from lib import output_helper
from lib.workflow.ocp_sriov_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    new_params = {}
    allowed_keys = [
        'cluster',
        'confirmation',
        'check-verbose'
    ]
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - SRIOV Operator - Create Instance', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_sriov_subscription(params['namespace'], params['name']):
        my_output.error('SRIOV operator required')
        return False

    if params['k8s_handler'].is_sriov_operator_config(cache_enabled=False):
        my_output.error('Sriov instance already created')
        return True
        
    success = params['k8s_handler'].create_sriov_operator_config(
        params['namespace'], 
        params['config']['name'], 
        params['config']['injector'],
        params['config']['webhook'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('- SRIOV Operator configuration created')

    return True
