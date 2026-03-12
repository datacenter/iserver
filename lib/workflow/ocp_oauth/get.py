from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_oauth import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'view' not in params or params['view'] is None:
        params['view'] = ['state']

    if not isinstance(params['view'], list):
        return None, 'view param must be list'

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
        'view',
        'check-verbose',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - OAuth - Get Information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    params = local_common.get_state(
        params,
        my_output
    )

    if 'state' in params['view']:
        local_common.print_state_summary(
            params, 
            my_output, 
            k8s_output_handler
        )

    if 'verbose' in params['view']:
        local_common.print_state(
            params, 
            my_output, 
            k8s_output_handler
        )

    return True
