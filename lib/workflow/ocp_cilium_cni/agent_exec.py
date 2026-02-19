from lib import output_helper
from lib.workflow.ocp_cilium_cni import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'command' not in params:
        return None, 'command required'
    
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
        'command',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    if not params['silent']:
        my_output.default('OpenShift Workflow - Cilium - Agent exec', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return None

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return None

    pods = params['k8s_handler'].get_pods_daemon_set(
        params['namespace'],
        params['agent-name']
    )
    if pods is None:
        if not params['silent']:
            my_output.error('Failed to get cilium agent pods')
        return None
    
    response = {}
    for pod in pods:
        response[pod['name']] = params['k8s_handler'].get_pod_exec(
            pod['namespace'],
            pod['name'],
            params['command']
        )

    return response
