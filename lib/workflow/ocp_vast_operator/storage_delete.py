from lib import output_helper
from lib.workflow.ocp_vast_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'name' not in params or params['name'] is None:
        return None, 'Driver name required'
    
    params['storage_name'] = params['name']

    if 'wait' not in params:
        params['wait'] = True

    if not isinstance(params['wait'], bool):
        return None, 'wait param must be true or false'

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
        'storage_name',
        'wait',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - VAST CSI Operator - Delete Storage', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    state = local_common.check_state(
        params, 
        my_output,
        check_ready=True
    )
    if not state['installed']:
        return True

    if not state['ready']:
        my_output.error('VAST operator not ready')
        return False
    
    success = params['k8s_handler'].delete_vast_storage(
        params['namespace'],
        params['storage_name'],
        my_output=my_output, 
        wait=params['wait']
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- VAST CSI storage deleted')

    return True
