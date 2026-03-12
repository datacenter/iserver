import time
from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_oauth import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'level' not in params or params['level'] is None:
        params['level'] = 'Normal'

    if params['level'] not in ['Normal', 'Debug', 'Trace', 'TraceAll']:
        return None, 'unsupported level value'

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'level',
        'check-verbose',
        'confirmation',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - OAuth - Log Level', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    params = local_common.get_state(
        params,
        my_output,
        scope=['authentication', 'pod']
    )
    k8s_output_handler.print_authentications_state(params['state']['authentication'][0], table=False)

    if params['state']['authentication'][0]['logLevel'] == params['level']:
        my_output.default('Nothing to do', before_newline=True)
        return True
    
    success = params['k8s_handler'].set_authentication_log_level(
        params['level'], 
        my_output=my_output, 
        confirmation=params['confirmation']
    )
    if not success:
        return False

    params = local_common.get_state(
        params,
        my_output,
        scope=['authentication']
    )
    k8s_output_handler.print_authentications_state(params['state']['authentication'][0], table=False)

    success = params['k8s_handler'].wait_oauth_pods_restart(
        params['state']['oauth_pod'], 
        my_output=my_output
    )

    return True
