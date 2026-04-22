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


def get_state(params, my_output, k8s_output_handler):
    network = params['k8s_handler'].get_network('cluster')
    if network is None:
        my_output.error('Failed to get network information')
        return False
    
    if network['network_type'] != 'Cilium':
        my_output.error('Unexpected network type: %s' % (network['network_type']))
        return False

    k8s_output_handler.print_network(network)

    if params['ssh_handler'] is not None:
        success, output, error = params['ssh_handler'].run_cmd(
            'cilium status -n cilium'
        )
        if not success:
            my_output.error('Failed to get cilium status via cli')
            my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
        else:
            my_output.default(output, before_newline=True)

    
def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Get state', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    if params['initialize']:
        params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True, ssh_required=True)
        if params is None:
            return False
    
    get_state(params, my_output, k8s_output_handler)
    return True
