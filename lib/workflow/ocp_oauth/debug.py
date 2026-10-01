import time
from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_oauth import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['level', True, 'Normal', 'str', None, None, ['Normal', 'Debug', 'Trace', 'TraceAll'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Log Level')
    params = ocp_common.workflow_init(params, my_output, log_id)
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