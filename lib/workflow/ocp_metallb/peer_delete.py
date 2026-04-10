from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_metallb import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['peer', True, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - MetalLB Operator - Delete bgp peer', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    subscription = ocp_common.get_subscription(
        params['k8s_handler'],
        params['__default__']['name'],
        my_output=my_output,
        brief=True
    )
    if subscription is None:
        return True
    
    if params['peer'] is None:
        peers = params['k8s_handler'].get_bgp_peers(cache_enabled=False)
        if peers is None:
            my_output.error('failed to get BGPPeer crds')
            return False
        
        k8s_output_handler.print_bgp_peers(peers)
        if len(peers) == 0:
            return True
        
        peer_index = my_output.get_integer(prompt='Select peer by index (0=all)', min_value=0, max_value=len(peers))
        if peer_index == 0:
            params['peer'] = '__all__'
        else:
            params['peer'] = peers[peer_index-1]['name']

    if params['peer'] == '__all__':
        peers = params['k8s_handler'].get_bgp_peers(cache_enabled=False)
        if peers is None:
            my_output.error('failed to get BGPPeer crds')
            return False
        
        k8s_output_handler.print_bgp_peers(peers)
        if len(peers) == 0:
            my_output.default('No bgp peer found')
            return True
        
        for peer in peers:
            success = params['k8s_handler'].delete_bgp_peer(
                peer['namespace'], 
                peer['name'], 
                my_output=my_output, 
                wait=params['wait']
            )
            if not success:
                return False
            
    if params['peer'] != '__all__':
        success = params['k8s_handler'].delete_bgp_peer(
            params['__default__']['namespace'], 
            params['peer'], 
            my_output=my_output, 
            wait=params['wait']
        )
        if not success:
            return False

    peers = params['k8s_handler'].get_bgp_peers(cache_enabled=False)
    if peers is None:
        my_output.error('failed to get BGPPeer crds')
        return False
    
    k8s_output_handler.print_bgp_peers(peers)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- MetalLB bgp peer deleted')

    return True
