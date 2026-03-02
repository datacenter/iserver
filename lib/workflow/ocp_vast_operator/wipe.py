from lib import output_helper
from lib.workflow.ocp_vast_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

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
        'wait',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - VAST CSI Operator - Wipe', before_newline=True, after_newline=True, double_underline=True)

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
        check_ready=True,
        check_resources=True
    )
    if not state['installed']:
        return True
    
    if state['storage'] is not None:
        for item in state['storage']:
            success = params['k8s_handler'].delete_vast_storage(
                item['namespace'],
                item['name'],
                my_output=my_output, 
                wait=params['wait']
            )
            if not success:
                return False
            
    if state['cluster'] is not None:
        for item in state['cluster']:
            success = params['k8s_handler'].delete_vast_cluster(
                item['namespace'],
                item['name'],
                my_output=my_output, 
                wait=params['wait']
            )
            if not success:
                return False

    if state['driver'] is not None:
        for item in state['driver']:
            success = params['k8s_handler'].delete_vast_driver(
                item['namespace'],
                item['name'],
                my_output=my_output, 
                wait=params['wait']
            )
            if not success:
                return False

    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- VAST CRDs deleted')

    return True
