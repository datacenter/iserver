from lib import filter_helper
from lib.workflow import ocp_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def get_default_params():
    params = cilium_common.get_default_params()
    params['title'] = 'OpenShift Workflow - Isovalent Private Network'
    params['resource_keys'] = [
        'clusterwide_private_network',
        'private_network_endpoint_slice',
        'private_network_external_endpoint',
        'private_network_node_attachment'
    ]
    params['resource_output'] = [
        ['clusterwide private network', 'clusterwide_private_network'],
        ['endpoint slice', 'private_network_endpoint_slice'],
        ['external endpoint', 'private_network_external_endpoint'],
        ['node attachment', 'private_network_node_attachment']
    ]
    params['db_keys'] = [
        'private-networks',
        'privnet-subnets',
        'privnet-routes',
        'privnet-node-attachments',
        'privnet-inbs',
        'privnet-endpoints',
        'privnet-mapentries'
    ]
    params['db_output'] = [
        ['network', 'private-networks'],
        ['subnet', 'privnet-subnets'],
        ['route', 'privnet-routes'],
        ['node attach', 'privnet-node-attachments'],
        ['inb', 'privnet-inbs'],
        ['endpoint', 'privnet-endpoints'],
        ['map', 'privnet-mapentries']
    ]
    return params


def collect_state_info(params):
    params['state'] = params['k8s_handler'].get_clusterwide_private_network_state(cache_enabled=False)
    params['state']['resources'] = False

    params['resource'] = {}  
    params['state']['crd'] = True
    for key in params['__default__']['resource_keys']:
        params['resource'][key] = getattr(params['k8s_handler'], 'get_%ss' % (key))(cache_enabled=False)
        if params['resource'][key] is None:
            params['state']['crd'] = False

    params['resource_summary'] = {}
    for key in params['__default__']['resource_keys']:
        params['resource_summary'][key] = '---'
        if params['resource'][key] is not None:
            params['resource_summary'][key] = len(params['resource'][key])
            if len(params['resource'][key]) > 0:
                params['state']['resources'] = True

    params['state']['ready'] = True
    if not params['state']['enabled']:
        params['state']['ready'] = False
    if not params['state']['crd']:
        params['state']['ready'] = False

    params['state'] = filter_helper.add_tick(
        params['state'],
        'ready',
        True,
        'readyTick'
    )
    params['state'] = filter_helper.add_tick(
        params['state'],
        'crd',
        True,
        'crdTick'
    )
    return params


def collect_db_state_info(params, db_name=None):
    params['db'] = params['k8s_handler'].get_cilium_private_network_dbs(db_name=db_name, cache_enabled=True)
    params['db_summary'] = {}

    for key in params['db'].keys():
        params['db_summary'][key] = len(params['db'][key])
        
    return params


def print_state(params, my_output):
    if not params['state']['enabled']:
        my_output.dictionary_ng(
            'Isovalent Private Network State',
            params['state'],
            [
                ['enabled', 'enabledTick']
            ]
        )

    if params['state']['enabled']:
        my_output.dictionary_ng(
            'Isovalent Private Network State',
            params['state'],
            [
                ['enabled', 'enabledTick'],
                ['multus', 'multusEnabledTick'],
                ['webhook', 'webhookEnabledTick'],
                ['crds', 'crdTick'],
                ['ready', 'readyTick']
            ]
        )
        print_webhook(params, my_output)


def print_webhook(params, my_output):
    if filter_helper.get_attr(params['state'], 'webhook:enabled', on_none=False):
        my_output.dictionary_ng(
            'Webhook State',
            params['state']['webhook'],
            [
                ['name', 'name'],
                ['configured', 'configured'],
                ['service_name', 'service_name'],
                ['service_found', 'service_found'],
                ['service_endpoints', 'service_endpoints']
            ]
        )


def print_resource_summary(params, my_output):
    my_output.dictionary_ng(
        'Private Network Custom Resources',
        params['resource_summary'],
        params['__default__']['resource_output']
    )   


def print_resources(params, k8s_output_handler):
    for key in params['__default__']['resource_keys']:
        if params['resource'][key] is None:
            continue

        if len(params['resource'][key]) == 0:
            continue

        getattr(k8s_output_handler, 'print_%ss_state' % (key))(params['resource'][key])
        

def print_db_summary(params, my_output):
    my_output.dictionary_ng(
        'Cilium Agent Database',
        params['db_summary'],
        params['__default__']['db_output']
    )   


def print_dbs(params, k8s_output_handler):
    for key in params['__default__']['db_keys']:
        if key not in params['db'] or params['db'][key] is None:
            continue

        if len(params['db'][key]) == 0:
            continue

        getattr(k8s_output_handler, 'print_cilium_agent_%s_state' % (key.replace('-','_')))(params['db'][key])


def is_pnet_crd(params, my_output=None):
    if my_output is not None:
        my_output.default('Check private network crd', underline=True, before_newline=True)
    
    if params['k8s_handler'].get_clusterwide_private_networks(cache_enabled=False) is None:
        if my_output is not None:
            my_output.error('ClusterwidePrivateNetwork CRD not found')
        return False
    
    if my_output is not None:
        my_output.default('- ClusterwidePrivateNetwork')

    if params['k8s_handler'].get_private_network_endpoint_slices(cache_enabled=False) is None:
        if my_output is not None:
            my_output.error('PrivateNetworkEndpointSlice CRD not found')
        return False
    
    if my_output is not None:
        my_output.default('- PrivateNetworkEndpointSlice')

    if params['k8s_handler'].get_private_network_external_endpoints(cache_enabled=False) is None:
        if my_output is not None:
            my_output.error('PrivateNetworkExternalEndpoint CRD not found')
        return False
    
    if my_output is not None:
        my_output.default('- PrivateNetworkExternalEndpoint')

    return True

def is_pnet_ready(params, my_output):
    if not cilium_common.is_cilium(params, my_output):
        return False

    if params['k8s_handler'].is_cilium_private_network_enabled(cache_enabled=False):
        my_output.default('Private network %s' % (my_output.add_color('enabled', 'Green')))
    else:
        my_output.default('Private network %s' % (my_output.add_color('disabled', 'Red')))
        return False

    if is_pnet_crd(params):
        my_output.default('Private network crds %s' % (my_output.add_color('found', 'Green')))
    else:
        my_output.default('Private network crds %s' % (my_output.add_color('not found', 'Red')))
        return False

    return True


def check_readiness(params, my_output):
    if not params['state']['enabled']:
        my_output.default('Isovalent Private Network feature %s' % (my_output.add_color('disabled', 'Red')))
        return False
    
    print_state(params, my_output)

    if not params['state']['ready']:
        my_output.default('Isovalent Private Network feature %s' % (my_output.add_color('not ready', 'Red')))
        return False
    
    return True


def get_private_network(params, name, my_output, k8s_output_handler=None):
    network_info = params['k8s_handler'].get_clusterwide_private_network(
        name,
        pod_info=True, 
        cache_enabled=False
    )
    if network_info is None:
        my_output.error('ClusterwidePrivateNetwork %s not found' % (params['name']))
        return None
    
    if k8s_output_handler is not None:
        k8s_output_handler.print_clusterwide_private_networks_state([network_info])

        if len(network_info['nad']) > 0:
            nads = params['k8s_handler'].get_nads(
                object_filter=['namespace_names:%s' % (','.join(network_info['nad']))],
                cache_enabled=False
            )
            if nads is None:
                my_output.error('Failed to get network attachment definitions')
            else:
                k8s_output_handler.print_nads_state(nads)
                if len(network_info['nad']) != len(nads):
                    my_output.error('Unexpected mismatch in network attachment definitions')

    return network_info


def initialize(params, my_output, title, log_id):
    ocp_common.print_title(params, my_output, title)
    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return None

    params = collect_state_info(params)
    if not check_readiness(params, my_output):
        return None
    
    return params