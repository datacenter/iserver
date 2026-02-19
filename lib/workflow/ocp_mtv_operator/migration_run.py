from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'action' not in params:
        return None, 'Action required'

    if params['action'] not in ['run']:
        return None, 'Unsupported action'
    
    if 'plan' not in params:
        return None, 'Migration plan name required'
    
    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'wait' not in params:
        params['wait'] = True

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
        'action',
        'plan',
        'wait',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Migration Toolkit for Virtualization Operator - Run Migration', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True
    
    if params['action'] == 'run':
        success = params['k8s_handler'].create_migration(
            params['namespace'],
            params['plan'],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True            
        )
        if not success:
            return False  
            
    my_output.default('')
    my_output.default('Completed tasks')
    if params['action'] == 'run':
        my_output.default('- migration completed successfully')

    return True
