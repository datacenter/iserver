from lib import filter_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_metallb import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def get_peer_body(params, my_output):
    body = {}
    body['apiVersion'] = 'metallb.io/v1beta2'
    body['kind'] = 'BGPPeer'
    body['metadata'] = {}
    body['metadata']['namespace'] = params['__default__']['namespace']
    body['metadata']['name'] = my_output.get_value('BGP peer crd name', empty=True)
    if body['metadata']['name'] is None or len(body['metadata']['name']) == 0:
        return None
    
    current_peer = params['k8s_handler'].get_bgp_peer(body['metadata']['namespace'], body['metadata']['name'], return_mo=True, cache_enabled=True)
    if current_peer is not None:
        body['metadata']['resourceVersion'] = current_peer['metadata']['resourceVersion']
        my_output.default('BGP peer name already defined and will be updated')
    
    body['spec'] = {}
    body['spec']['myASN'] = my_output.get_integer('My ASN', min_value=1, default=filter_helper.get(current_peer, 'spec:myASN'))
    body['spec']['peerASN'] = my_output.get_integer('Peer ASN', min_value=1, default=filter_helper.get(current_peer, 'spec:peerASN'))
    body['spec']['peerAddress'] = my_output.get_ip_address('Peer address', default=filter_helper.get(current_peer, 'spec:peerAddress'))
    body['spec']['ebgpMultiHop'] = my_output.get_bool('Multihop', default=filter_helper.get(current_peer, 'spec:ebgpMultiHop'))
    return body


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - MetalLB Operator - Create bgp peer', before_newline=True, after_newline=True, double_underline=True)

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

    peers = params['k8s_handler'].get_bgp_peers(cache_enabled=False)
    if peers is None:
        my_output.error('failed to get BGPPeer crds')
        return False
    
    k8s_output_handler.print_bgp_peers(peers)
    my_output.default('')

    body = get_peer_body(params, my_output)
    if body is None:
        return False
    
    success = params['k8s_handler'].create_or_update_bgp_peer(
        body, 
        my_output=my_output, 
        confirmation=params['confirmation'], 
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
    my_output.default('- MetalLB bgp peer defined')

    return True
