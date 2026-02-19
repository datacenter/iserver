import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_grafana_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'channel' not in params:
        params['channel'] = '__default__'

    if 'confirmation' not in params:
        params['confirmation'] = False

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
    
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
    my_output.default('OpenShift Workflow - Grafana Operator - Create Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['k8s_handler'].is_grafana_subscription(params['namespace'], params['name']):
        my_output.default('Grafana Operator already created')
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
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_grafana_subscription(
        params['namespace'], 
        params['name'], 
        channel=params['channel'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks', underline=True, before_newline=True)
    my_output.default('- Namespace created')
    my_output.default('- Operator Group created')
    my_output.default('- Grafana Operator installed')
    
    return True
