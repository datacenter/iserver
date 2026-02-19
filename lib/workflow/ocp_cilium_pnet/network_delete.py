from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_pnet import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'network' not in params or params['network'] is None:
        return None, 'Private network name required'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
    
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
        'network',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium Private Network - Delete Private Network', before_newline=True, after_newline=True, double_underline=True) 

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_pnet_ready(params, my_output):
        return False

    network_info = params['k8s_handler'].get_clusterwide_private_network(
        params['network'],
        pod_info=True, 
        cache_enabled=False
    )
    if network_info is None:
        my_output.error('ClusterwidePrivateNetwork %s not found' % (params['network']))
        return True
    
    k8s_output_handler.print_clusterwide_private_networks([network_info])

    if params['confirmation']:
        if not get_confirmation():
            return False
    
    success = params['k8s_handler'].delete_clusterwide_private_network(
        params['network'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Private Network deleted')

    return True
