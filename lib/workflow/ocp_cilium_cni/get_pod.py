from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def get_pod(params, my_output, k8s_output_handler):
    pods = params['k8s_handler'].get_pods(
        object_filter=['namespace:%s' % (params['__default__']['namespace'])],
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

    if params['initialize']:
        params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
        if params is None:
            return False

    get_pod(params, my_output, k8s_output_handler)
    return True
