from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_bgp import common as local_common


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
        'check-verbose',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium BGP Control Plane - Wipe', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    success = params['k8s_handler'].delete_isovalent_bgp_advertisements(
        my_output=my_output, 
        wait=True,
        brief=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_isovalent_bgp_peer_configs(
        my_output=my_output, 
        wait=True,
        brief=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_isovalent_bgp_cluster_configs(
        my_output=my_output, 
        wait=True,
        brief=True
    )
    if not success:
        return False

    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- All BGP control plane configuration crds deleted')

    return True
