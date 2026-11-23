import copy
from progress.bar import Bar
from lib import ip_helper
from lib import output_helper
from lib.workflow.aci_interface import common as local_common


def validate(params):
    if 'apic' not in params:
        return None, 'APIC name required'

    if 'interface' not in params:
        return None, 'Interface list required'

    if not isinstance(params['interface'], list):
        return None, 'Interface list required'

    if len(params['interface']) == 0:
        return None, 'Define at least one interface'

    interface = []
    for item in params['interface']:
        if not isinstance(item, dict):
            return None, 'Interface list of dict required'

        if 'context' not in item:
            item['context'] = None

        if 'node' not in item:
            return None, 'interface.node required'
        
        if not isinstance(item['node'], str):
            return None, 'interface.node type string required'
        
        if 'port' not in item:
            return None, 'interface.port required'
        
        if not isinstance(item['port'], str):
            return None, 'interface.port type string required'

        if 'ip' in item:
            if not ip_helper.is_valid_ipv4_address(item['ip']):
                return None, 'interface.ip must be ip address' % (item['ip'])
            
        if 'gateway' in item:
            if not ip_helper.is_valid_ipv4_cidr(item['gateway']):
                return None, 'interface.gateway must be cidr' % (item['gateway'])

        if item['ip'] not in item and item['gateway'] in item:
            return None, 'interface.gateway required interface.ip'
        
        if 'mac' in item:
            if not ip_helper.is_valid_mac_address(item['mac']):
                return None, 'interface.mac must be mac address' % (item['mac'])

        if 'vlan' in item:
            if not isinstance(item['vlan'], int):
                return None, 'interface.vlan type int required'
            
        if 'bond' in item:
            if not isinstance(item['bond'], bool):
                return None, 'interface.bond type bool required'

        if 'trunk' in item:
            if not isinstance(item['trunk'], bool):
                return None, 'interface.trunk type bool required'

        allowed_keys = [
            'context',
            'node',
            'port',
            'ip',
            'gateway',
            'mac',
            'vlan',
            'bond',
            'trunk'
        ]
        interface.append(
            local_common.sanitize_params(
                item,
                allowed_keys
            )
        ) 
    
    params['interface'] = copy.deepcopy(interface)
    return params, None


def check_node(handler, interface):
    node_info = handler.get_node(
        node_id=interface['node'],
        cache_enabled=False
    )
    if node_info is None:
        interface['__Output']['node'] = 'Red'
        interface['info'].append('Node not found')
        return False, interface
    
    interface['__Output']['node'] = 'Green'
    interface['pod'] = node_info['podId']

    return True, interface


def check_phy(handler, interface):
    interface['__phy'] = handler.get_interface_phy(
        interface['pod'],
        interface['node'],
        'eth%s' % (interface['port']),
        policy_info=True,
        pc_info=True,
        epg_stats_info=True,
        cache_enabled=False
    )
    if interface['__phy'] is None:
        interface['__Output']['port'] = 'Red'
        interface['info'].append('Port not found')
        return False, interface

    if interface['__phy']['stats'] is None:
        interface['__Output']['port'] = 'Red'
        interface['info'].append('Port stats missing')
        return False, interface

    if interface['__phy']['usage'] != 'epg':
        interface['__Output']['port'] = 'Red'
        interface['info'].append('EPG not configured')
        return False, interface

    if interface['__phy']['switchingSt'] != 'enabled':
        interface['__Output']['port'] = 'Red'
        interface['info'].append('Switching disabled')
        return False, interface

    interface['__Output']['port'] = 'Green'
    interface['__Output']['__phy.stats.operSt'] = interface['__phy']['__Output']['stats.operSt']

    if 'epg_stats' not in interface['__phy']:
        interface['__phy']['epg_stats'] = None
        interface['info'].append('No port epg stats')

    if 'policy_selector' not in interface['__phy']:
        interface['__phy']['policy_selector'] = None

    return True, interface


def check_ip(handler, interface):
    if 'ip' not in interface:
        return True, interface
    
    interface['__Output']['ip'] = 'Green'
    interface['__bd_name_tenant'] = None
    
    endpoints = handler.get_endpoints(
        endpoint_filter=['ip:%s' % (interface['ip'])],
        fabric_info=True,
        cache_enabled=False
    )
    if endpoints is None:
        interface['__Output']['ip'] = 'Red'
        interface['info'].append('EP api failed')
        return False, interface
    
    if len(endpoints) == 0:
        interface['__Output']['ip'] = 'Yellow'
        interface['info'].append('IP EP not found')

    endpoint_interfaces = []
    for endpoint in endpoints:
        if len(endpoint['bdNameTenant']) > 0:
            interface['__bd_name_tenant'] = endpoint['bdNameTenant']

        if len(endpoint['epgNameApTenant']) > 0:
            interface['info'].append('EPG %s' % (endpoint['epgNameApTenant']))

        if 'epg' in interface:
            if endpoint['epgNameApTenant'] != interface['epg']:
                interface['__Output']['ip'] = 'Yellow'
                interface['info'].append('EPG mismatch %s/%s' % (endpoint['epgNameApTenant'], interface['epg']))

        if 'fabric' in endpoint and endpoint['fabric'] is not None:
            for endpoint_fabric in endpoint['fabric']:
                interface['info'].append(
                    'IP EP %s:%s' % (
                        endpoint_fabric['node_id'], 
                        endpoint_fabric['port_id'].replace('eth', '')
                    )
                )
                endpoint_interfaces.append(
                    '%s:%s:%s' % (
                        endpoint_fabric['pod_id'],
                        endpoint_fabric['node_id'],
                        endpoint_fabric['port_id'].replace('eth', '')
                    )
                )

    if len(endpoint_interfaces) > 0:
        expected_interface = '%s:%s:%s' % (
            interface['pod'],
            interface['node'],
            interface['port']
        )
        if expected_interface not in endpoint_interfaces:
            interface['__Output']['ip'] = 'Red'
            interface['info'].append('IP EP port mismatch')

    return True, interface


def check_gateway(handler, interface):
    if 'gateway' not in interface:
        return True, interface
    
    interface['__Output']['gateway'] = 'Green'

    external_ips = handler.l3out_external_ips(
        cache_enabled=False
    )
    if external_ips is None:
        interface['__Output']['gateway'] = 'Red'
        interface['info'].append('l3extIp api failed')
        return False, interface

    for external_ip in external_ips:
        if interface['gateway'] == external_ip['cidr']:
            interface['info'].append('L3Out %s/%s' % (external_ip['tenant'], external_ip['l3out']))
            return True, interface
        
    bridge_domains = handler.get_bridge_domains(
        cache_enabled=False
    )
    if bridge_domains is None:
        interface['__Output']['gateway'] = 'Red'
        interface['info'].append('bd api failed')
        return False, interface

    for bridge_domain in bridge_domains:
        for gateway in bridge_domain['fvSubnets'].split(','):
            if gateway == external_ip['cidr']:
                interface['info'].append('BD %s' % (bridge_domain['nameTenant']))
                return True, interface

    interface['__Output']['gateway'] = 'Yellow'
    interface['info'].append('Gateway not in l3out/bd')

    return True, interface


def check_mac(handler, interface):
    if 'mac' not in interface:
        return True, interface
    
    interface['__Output']['mac'] = 'Green'

    endpoints = handler.get_endpoints(
        endpoint_filter=['mac:%s' % (interface['mac'])],
        fabric_info=True,
        cache_enabled=False
    )
    if endpoints is None:
        interface['__Output']['mac'] = 'Red'
        interface['info'].append('EP api failed')
        return False, interface
    
    if len(endpoints) == 0:
        interface['__Output']['mac'] = 'Yellow'
        interface['info'].append('MAC EP not found')

    endpoint_interfaces = []
    for endpoint in endpoints:
        if len(endpoint['epgNameApTenant']) > 0:
            interface['info'].append('EPG %s' % (endpoint['epgNameApTenant']))

        if 'epg' in interface:
            if endpoint['epgNameApTenant'] != interface['epg']:
                interface['__Output']['mac'] = 'Yellow'
                interface['info'].append('EPG mismatch %s/%s' % (endpoint['epgNameApTenant'], interface['epg']))

        if 'fabric' in endpoint and endpoint['fabric'] is not None:
            for endpoint_fabric in endpoint['fabric']:
                interface['info'].append(
                    'MAC EP %s:%s' % (
                        endpoint_fabric['node_id'], 
                        endpoint_fabric['port_id'].replace('eth', '')
                    )
                )
                endpoint_interfaces.append(
                    '%s:%s:%s' % (
                        endpoint_fabric['pod_id'],
                        endpoint_fabric['node_id'],
                        endpoint_fabric['port_id'].replace('eth', '')
                    )
                )

    if len(endpoint_interfaces) > 0:
        expected_interface = '%s:%s:%s' % (
            interface['pod'],
            interface['node'],
            interface['port']
        )
        if expected_interface not in endpoint_interfaces:
            interface['__Output']['mac'] = 'Red'
            interface['info'].append('MAC EP port mismatch')

    return True, interface


def check_bond_configuration(interface):
    if 'bond' not in interface:
        return True, interface

    interface['__Output']['bond'] = 'Green'

    if not interface['bond']:
        if interface['__phy']['policy_selector'] is not None:
            if interface['__phy']['policy_selector']['policy_group_type'] == 'infraAccBndlGrp':
                interface['__Output']['bond'] = 'Red'
                interface['info'].append('PC/VPC PG unexpected')
                return False, interface
    
    if interface['bond']:
        if interface['__phy']['policy_selector'] is None:
            interface['__Output']['bond'] = 'Red'
            interface['info'].append('No policy selector')
            return False, interface
        
        if interface['__phy']['policy_selector']['policy_group_type'] != 'infraAccBndlGrp':
            interface['__Output']['bond'] = 'Red'
            interface['info'].append('PC/VPC PG policy expected')
            return False, interface

        if 'policy_group_name' not in interface:
            interface['__Output']['bond'] = 'Green'
            interface['info'].append('PV/VPC PG %s' % (interface['__phy']['policy_selector']['policy_group_name']))
            return True, interface
        
        if interface['__phy']['policy_selector']['policy_group_name'] == interface['policy_group_name']:
            interface['__Output']['bond'] = 'Green'
            interface['info'].append('PV/VPC PG %s' % (interface['__phy']['policy_selector']['policy_group_name']))
            return True, interface

        interface['__Output']['bond'] = 'Yellow'
        interface['info'].append(
            'PV/VPC PG mismatch %s/%s' % (
                interface['__phy']['policy_selector']['policy_group_name'],
                interface['policy_group_name']
            )
        )

    return True, interface


def check_bond_state(interface):
    if 'bond' not in interface:
        return True, interface

    if interface['bond']:
        if 'bundleIndex' not in interface['__phy']['stats']:
            interface['__Output']['bond'] = 'Red'
            interface['info'].append('Bundle index unknown')

    if not interface['bond']:
        if 'bundleIndex' in interface['__phy']['stats']:
            interface['__Output']['bond'] = 'Red'
            interface['info'].append('Bundle index defined')

    return True, interface


def check_vlan(interface):
    if 'vlan' not in interface:
        return True, interface

    interface['__Output']['vlan'] = 'Green'

    if interface['__phy']['epg_stats'] is None:
        interface['__Output']['vlan'] = 'Yellow'
        return True, interface
    
    for epg_stats in interface['__phy']['epg_stats']:
        if 'vlan' in epg_stats and epg_stats['vlan'] is not None:
            if epg_stats['vlan']['encap'] == 'vlan-%s' % (interface['vlan']):
                interface['__Output']['vlan'] = 'Green'
                return True, interface

        if 'staticPort' in epg_stats and epg_stats['staticPort'] is not None:
            for static_port_mo in epg_stats['staticPort']:
                if static_port_mo['encap'] == 'vlan-%s' % (interface['vlan']):
                    interface['__Output']['vlan'] = 'Green'
                    return True, interface

    try:
        if interface['vlan'] in interface['__phy']['policy_selector']['policy_group_info']['aaep']['vlanIds']:
            return True, interface
    except BaseException:
        pass

    interface['__Output']['vlan'] = 'Yellow'
    interface['info'].append('VLAN may not be enabled')
    return True, interface


def check_trunk(interface):
    if 'trunk' not in interface:
        return True, interface
    
    interface['__Output']['trunk'] = 'Green'

    if interface['trunk'] and interface['__phy']['mode'] != 'trunk':
            interface['__Output']['trunk'] = 'Red'
            interface['info'].append('Trunk mode mismatch')
            return False, interface

    if not interface['trunk'] and interface['__phy']['mode'] == 'trunk':
            interface['__Output']['trunk'] = 'Red'
            interface['info'].append('Trunk mode mismatch')
            return False, interface

    return True, interface


def check_interface(handler, interface):
    interface['__Output'] = {}
    interface['__Output']['successTick'] = 'Green'
    interface['success'] = True
    interface['successTick'] = '\u2713'
    interface['info'] = []

    success, interface = check_node(handler, interface)
    if not success:
        interface['success'] = False
        interface['successTick'] = '\u2717'
        interface['__Output']['successTick'] = 'Red'
        return interface

    success, interface = check_phy(handler, interface)
    if not success:
        interface['success'] = False
        interface['successTick'] = '\u2717'
        interface['__Output']['successTick'] = 'Red'
        return interface

    success, interface = check_ip(handler, interface)
    if not success:
        interface['success'] = False

    success, interface = check_gateway(handler, interface)
    if not success:
        interface['success'] = False

    success, interface = check_mac(handler, interface)
    if not success:
        interface['success'] = False

    success, interface = check_bond_configuration(interface)
    if not success:
        interface['success'] = False

    success, interface = check_bond_state(interface)
    if not success:
        interface['success'] = False

    success, interface = check_vlan(interface)
    if not success:
        interface['success'] = False

    success, interface = check_trunk(interface)
    if not success:
        interface['success'] = False

    if not interface['success']:
        interface['successTick'] = '\u2717'
        interface['__Output']['successTick'] = 'Red'

    return interface


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('ACI Workflow - Check interface', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    bar_handler = Bar('Interface', max=len(params['interface']))
    bar_handler.goto(0)
    interfaces = []
    for item in params['interface']:
        item['apic'] = params['apic']
        interfaces.append(
            check_interface(
                params['apic_handler'],
                item
            )
        )
        bar_handler.next()
    bar_handler.finish()

    order = [
        'context',
        'successTick',
        'apic',
        'node',
        'port',
        '__phy.stats.operSt',
        'ip',
        'gateway',
        'mac',
        'bond',
        'vlan',
        'trunk',
        'info'
    ]

    headers = [
        'Ctx',
        'Sync',
        'Apic',
        'Node',
        'Port',
        'State',
        'IP',
        'Gateway',
        'MAC',
        'Bond',
        'Vlan',
        'Trunk',
        'Info'
    ]

    for interface in interfaces:
        if len(interface['info']) == 0:
            interface['info'].append('---')

    my_output.my_table(
        my_output.expand_lists(
            interfaces,
            order,
            ['info']
        ),
        order=order,
        headers=headers,
        allow_order_subkeys=True,
        underline=True,
        row_separator=True,
        table=True
    )

    return True
