import json
from lib import output_helper
from lib.workflow import ocp_common as workflow_common
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_trident_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'channel' not in params:
        params['channel'] = 'stable'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    new_params = {}
    allowed_keys = [
        'cluster',
        'channel',
        'confirmation',
        'check-verbose'
    ]
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Trident Operator - Create Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['k8s_handler'].is_trident_subscription(params['namespace'], params['name']):
        my_output.default('Trident operator already created')
        return True

    success = params['k8s_handler'].create_trident_subscription(
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
    my_output.default('Completed tasks')
    my_output.default('- Trident Operator installed')

    return True
