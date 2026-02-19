from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_cilium_cni import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

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
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def get_pod(params, my_output, k8s_output_handler):
    pods = params['k8s_handler'].get_pods(
        object_filter=['namespace:%s' % (params['namespace'])],
        service_info=True
    )
    if pods is None:
        my_output.error('Failed to get cilium pods information')
        return False

    my_output.default('Cilium PODs', underline=True, before_newline=True)
    k8s_output_handler.print_pods_state(
        pods, 
        skip=['Net', 'Restart']
    )


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    my_output.default('OpenShift Workflow - Cilium - Get pods', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    get_pod(params, my_output, k8s_output_handler)
    return True
