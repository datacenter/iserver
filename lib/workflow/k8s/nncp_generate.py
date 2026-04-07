from lib import ip_helper 
from lib.workflow.k8s import nncp_validate


def generate_route(data):
    route_mo = {}
    route_mo['destination'] = data['destination']
    if 'metric' in data and data['metric'] is not None:
        route_mo['metric'] = data['metric']
    if 'table' in data and data['table'] is not None:
        route_mo['table-id'] = data['table']
    if 'interface' in data and data['interface'] is not None:
        route_mo['next-hop-interface'] = data['interface']
    if 'gateway' in data and data['gateway'] is not None:
        route_mo['next-hop-address'] = data['gateway']
    if 'state' in data:
        route_mo['state'] = data['state']
    return route_mo

def generate_nncp_vlan(data):
    interface_mo = {}
    interface_mo['name'] = '%s.%s' % (data['base'], data['vlan_id'])
    interface_mo['type'] = 'vlan'
    interface_mo['state'] = data['state']
    interface_mo['vlan'] = {}
    interface_mo['vlan']['base-iface'] = data['base']
    interface_mo['vlan']['id'] = data['vlan_id']
    if 'ipv4' in data and data['ipv4'] is not None:
        if data['ipv4'] == 'dhcp':
            interface_mo['ipv4'] = {}
            interface_mo['ipv4']['dhcp'] = True
            interface_mo['ipv4']['enabled'] = True

        if data['ipv4'] == 'none':
            interface_mo['ipv4'] = {}
            interface_mo['ipv4']['enabled'] = False

        if ip_helper.is_valid_ipv4_cidr(data['ipv4']):
            interface_mo['ipv4'] = {}
            interface_mo['ipv4']['dhcp'] = False
            interface_mo['ipv4']['enabled'] = True
            interface_mo['ipv4']['address'] = []

            address_mo = {}
            address_mo['ip'] = data['ipv4'].split('/')[0]
            address_mo['prefix-length'] = int(data['ipv4'].split('/')[1])
            interface_mo['ipv4']['address'].append(
                address_mo
            )

    return interface_mo

def generate_nncp_eth(data):
    interface_mo = {}
    interface_mo['name'] = data['name']
    interface_mo['type'] = 'ethernet'
    interface_mo['state'] = data['state']
    if data['ipv4'] is not None:
        if data['ipv4'] == 'dhcp':
            interface_mo['ipv4'] = {}
            interface_mo['ipv4']['dhcp'] = True
            interface_mo['ipv4']['enabled'] = True

        if data['ipv4'] == 'none':
            interface_mo['ipv4'] = {}
            interface_mo['ipv4']['enabled'] = False

        if ip_helper.is_valid_ipv4_cidr(data['ipv4']):
            interface_mo['ipv4'] = {}
            interface_mo['ipv4']['dhcp'] = False
            interface_mo['ipv4']['enabled'] = True
            interface_mo['ipv4']['address'] = []

            address_mo = {}
            address_mo['ip'] = data['ipv4'].split('/')[0]
            address_mo['prefix-length'] = int(data['ipv4'].split('/')[1])
            interface_mo['ipv4']['address'].append(
                address_mo
            )

    return interface_mo

def generate_nncp_bond(data):
    interface_mo = {}
    interface_mo['name'] = data['name']
    interface_mo['type'] = 'bond'
    interface_mo['state'] = data['state']

    if interface_mo['state'] == 'absent':
        return interface_mo
    
    if data['ipv4'] is not None:
        if data['ipv4'] == 'dhcp':
            interface_mo['ipv4'] = {}
            interface_mo['ipv4']['dhcp'] = True
            interface_mo['ipv4']['enabled'] = True

        if data['ipv4'] == 'none':
            interface_mo['ipv4'] = {}
            interface_mo['ipv4']['enabled'] = False

        if ip_helper.is_valid_ipv4_cidr(data['ipv4']):
            interface_mo['ipv4'] = {}
            interface_mo['ipv4']['dhcp'] = False
            interface_mo['ipv4']['enabled'] = True
            interface_mo['ipv4']['address'] = []

            address_mo = {}
            address_mo['ip'] = data['ipv4'].split('/')[0]
            address_mo['prefix-length'] = int(data['ipv4'].split('/')[1])
            interface_mo['ipv4']['address'].append(
                address_mo
            )

    interface_mo['link-aggregation'] = {}
    interface_mo['link-aggregation']['mode'] = data['mode']
    if data['miimon'] is not None:
        interface_mo['link-aggregation']['options'] = {}
        interface_mo['link-aggregation']['options']['miimon'] = data['miimon']

    interface_mo['link-aggregation']['port'] = data['port'].split(',')

    if 'mtu' in data:
        interface_mo['mtu'] = data['mtu']

    return interface_mo

def generate_nncp_lb(data):
    interface_mo = {}
    interface_mo['name'] = data['name']
    interface_mo['type'] = 'linux-bridge'
    interface_mo['state'] = data['state']

    if interface_mo['state'] == 'absent':
        return interface_mo
    
    if data['ipv4'] is not None:
        if data['ipv4'] == 'dhcp':
            interface_mo['ipv4'] = {}
            interface_mo['ipv4']['dhcp'] = True
            interface_mo['ipv4']['enabled'] = True

        if data['ipv4'] == 'none':
            interface_mo['ipv4'] = {}
            interface_mo['ipv4']['enabled'] = False

        if ip_helper.is_valid_ipv4_cidr(data['ipv4']):
            interface_mo['ipv4'] = {}
            interface_mo['ipv4']['dhcp'] = False
            interface_mo['ipv4']['enabled'] = True
            interface_mo['ipv4']['address'] = []

            address_mo = {}
            address_mo['ip'] = data['ipv4'].split('/')[0]
            address_mo['prefix-length'] = int(data['ipv4'].split('/')[1])
            interface_mo['ipv4']['address'].append(
                address_mo
            )

    interface_mo['bridge'] = {}
    interface_mo['bridge']['options'] = {}
    interface_mo['bridge']['options']['stp'] = {}
    interface_mo['bridge']['options']['stp']['enabled'] = data['stp']

    interface_mo['bridge']['port'] = []
    port_mo = {}
    port_mo['name'] = data['port']
    interface_mo['bridge']['port'].append(
        port_mo
    )

    return interface_mo

def run(params, my_output):
    item = nncp_validate.run(params, my_output)
    if item is None:
        return None
    
    nncp_mo = {}
    nncp_mo['apiVersion'] = 'nmstate.io/v1'
    nncp_mo['kind'] = 'NodeNetworkConfigurationPolicy'
    nncp_mo['metadata'] = {}

    policy_name = 'policy'
    if 'policy' in item:
        policy_name = item['policy']

    if params['k8s_handler'].is_node_network_configuration_policy(policy_name, cache_enabled=False):
        policy_name = '%s-%s' % (policy_name, ip_helper.get_short_uuid())

    nncp_mo['metadata']['name'] = policy_name

    item['nncp'] = nncp_mo

    nncp_mo['spec'] = {}
    if item['node'] == '__workers__':
        nncp_mo['spec']['nodeSelector'] = {}
        nncp_mo['spec']['nodeSelector']['node-role.kubernetes.io/worker'] = ''

    if item['node'] not in ['__all__', '__workers__']:
        nncp_mo['spec']['nodeSelector'] = {}
        nncp_mo['spec']['nodeSelector']['kubernetes.io/hostname'] = item['node']

    nncp_mo['spec']['desiredState'] = {}

    if 'interfaces' in item:
        nncp_mo['spec']['desiredState']['interfaces'] = []
        for interface in item['interfaces']:
            if interface['type'] == 'vlan':
                nncp_mo['spec']['desiredState']['interfaces'].append(
                    generate_nncp_vlan(interface)
                )

            if interface['type'] == 'eth':
                nncp_mo['spec']['desiredState']['interfaces'].append(
                    generate_nncp_eth(interface)
                )

            if interface['type'] == 'bond':
                nncp_mo['spec']['desiredState']['interfaces'].append(
                    generate_nncp_bond(interface)
                )

            if interface['type'] == 'lb':
                nncp_mo['spec']['desiredState']['interfaces'].append(
                    generate_nncp_lb(interface)
                )

    if 'routes' in item:
        nncp_mo['spec']['desiredState']['routes'] = {}
        nncp_mo['spec']['desiredState']['routes']['config'] = []
        for route in item['routes']:
            nncp_mo['spec']['desiredState']['routes']['config'].append(
                generate_route(route)
            )

    return item