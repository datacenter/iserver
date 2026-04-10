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


def get_advertisement_body(params, my_output):
    pools = params['k8s_handler'].get_ip_address_pools(cache_enabled=False)
    if pools is None:
        my_output.error('failed to get IPAddressPool crds')
        return None

    peers = params['k8s_handler'].get_bgp_peers(cache_enabled=False)
    if peers is None:
        my_output.error('failed to get BGPPeer crds')
        return None

    body = {}
    body['apiVersion'] = 'metallb.io/v1beta1'
    body['kind'] = 'BGPAdvertisement'
    body['metadata'] = {}
    body['metadata']['namespace'] = params['__default__']['namespace']
    body['metadata']['name'] = my_output.get_value('BGP advertisement crd name', empty=True)
    if body['metadata']['name'] is None or len(body['metadata']['name']) == 0:
        return None
    
    current_advertisement = params['k8s_handler'].get_bgp_advertisement(body['metadata']['namespace'], body['metadata']['name'], return_mo=True, cache_enabled=True)
    if current_advertisement is not None:
        body['metadata']['resourceVersion'] = current_advertisement['metadata']['resourceVersion']
        my_output.default('BGP advertisement name already defined and will be replaced')
    
    body['spec'] = {}
    
    adv_pools = []
    if len(pools) > 0:
        while True:
            value = my_output.get_value('IPAddressPool name', empty=True)
            if value is None or len(value) == 0:
                break

            if not params['k8s_handler'].is_ip_address_pool(params['__default']['namespace'], value, cache_enabled=True):
                my_output.error('ip address pool not found')
                continue

            adv_pools.append(
                value
            )
    
    if len(adv_pools) > 0:
        body['spec']['ipAddressPools'] = adv_pools

    adv_peers = []
    if len(peers) > 0:
        while True:
            value = my_output.get_value('BGPPeer name', empty=True)
            if value is None or len(value) == 0:
                break

            if not params['k8s_handler'].is_bgp_peer(params['__default']['namespace'], value, cache_enabled=True):
                my_output.error('bgp peer not found')
                continue

            adv_peers.append(
                value
            )
    
    if len(adv_peers) > 0:
        body['spec']['peers'] = adv_peers

    communities = []
    while True:
        value = my_output.get_value('Community x:y value', empty=True)
        if value is None or len(value) == 0:
            break

        if len(value.split(':')) != 2:
            my_output.default('Community value format X:Y required')
            continue

        communities.append(
            value
        )

    if len(communities) > 0:
        body['spec']['communities'] = communities

    agg4 = my_output.get_integer('Aggregation v4 length', min_value=0, max_value=32, default=0)
    if agg4 > 0:
        body['spec']['aggregationLength'] = agg4

    agg6 = my_output.get_integer('Aggregation v6 length', min_value=0, max_value=128, default=0)
    if agg6 > 0:
        body['spec']['aggregationLengthV6'] = agg6

    return body


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - MetalLB Operator - Create bgp advertisement', before_newline=True, after_newline=True, double_underline=True)

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

    advertisements = params['k8s_handler'].get_bgp_advertisements(cache_enabled=False)
    if advertisements is None:
        my_output.error('failed to get BGPAdvertisement crds')
        return False
    
    k8s_output_handler.print_bgp_advertisements(advertisements)
    my_output.default('')

    body = get_advertisement_body(params, my_output)
    if body is None:
        return False
    
    success = params['k8s_handler'].create_or_update_bgp_advertisement(
        body, 
        my_output=my_output, 
        confirmation=params['confirmation'], 
        wait=params['wait']
    )
    if not success:
        return False
    
    advertisements = params['k8s_handler'].get_bgp_advertisements(cache_enabled=False)
    if advertisements is None:
        my_output.error('failed to get BGPAdvertisement crds')
        return False
    
    k8s_output_handler.print_bgp_advertisements(advertisements)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- MetalLB bgp advertisement defined')

    return True
