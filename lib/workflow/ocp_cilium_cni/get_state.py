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

    params = local_common.initialize(params, my_output, log_id, mgmt_required=False)
    if params is None:
        return False

    if not local_common.is_cilium(params, my_output, install_plan_enforced=False):
        return False
    
    get_state(params, my_output, k8s_output_handler)
    return True
