from lib import ip_helper
from lib.workflow.ocp_fabric import common
from lib.aci import settings as aci_settings


def validate_fabric_controller_aci(controller, mode, domain_interface, my_output, log_id):
    controller['check_mode'] = 'full'

    controller['ip'] = common.get_controller_ip(controller, my_output, log_id)
    if controller['ip'] is None:
        my_output.error('Controller not found')
        return None

    if len(domain_interface) == 0:
        my_output.error('Domain has no interfaces')
        return None

    if mode not in ['check', 'install', 'delete']:
        my_output.error('Unsupported fabric mode: %s' % (mode))
        return None

    if 'mo_name' not in controller:
        controller['mo_name'] = None

    if 'tenant' not in controller or controller['tenant'] is None:
        controller['check_mode'] = 'partial'
        # my_output.error('controller.tenant required')
        # return None

    if controller['check_mode'] == 'full':
        if not isinstance(controller['tenant'], str):
            my_output.error('controller.tenant required')
            return None

    if 'l3out' not in controller or controller['l3out'] is None:
        controller['check_mode'] = 'partial'
        # my_output.error('controller.l3out required')
        # return None

    if controller['check_mode'] == 'full':
        if not isinstance(controller['l3out'], str):
            my_output.error('controller.l3out required')
            return None

    if 'vrf' not in controller or controller['vrf'] is None:
        controller['check_mode'] = 'partial'
        # my_output.error('controller.vrf required')
        # return None

    if controller['check_mode'] == 'full':
        if not isinstance(controller['vrf'], str):
            my_output.error('controller.vrf required')
            return None

    interface_vlan = None
    for interface in domain_interface:
        if 'vlan' in interface and interface['vlan'] is not None:
            if interface_vlan is None:
                interface_vlan = interface['vlan']
                continue

            if interface_vlan != interface['vlan']:
                my_output.error('server.interface.vlan must be the same in domain')
                return None

    interface_gateway = None
    for interface in domain_interface:
        if 'gateway' in interface and interface['gateway'] is not None:
            if interface_gateway is None:
                interface_gateway = interface['gateway']
                continue

            if interface_gateway != interface['gateway']:
                my_output.error('server.interface.gateway must be the same in domain')
                return None

    interface_nodes = []
    for interface in domain_interface:
        if interface['node'] not in interface_nodes:
            interface_nodes.append(interface_nodes)

    if len(domain_interface) == 1:
        interface_policy_type = 'individual'
    else:
        if len(interface_nodes) == 1:
            interface_policy_type = 'pc'
        else:
            interface_policy_type = 'vpc'

    if controller['check_mode'] == 'partial':
        return controller

    keys = [
        'vlan_pool',
        'physical_domain',
        'aaep',
        'policy_group'
    ]

    if 'bgp' not in controller:
        keys.append('ap')
        keys.append('epg')
        keys.append('bd')
        controller['l3_domain'] = {}
        controller['l3_domain']['enabled'] = False
        controller['bgp'] = {}
        controller['bgp']['enabled'] = False
    else:
        keys.append('l3_domain')
        controller['ap'] = {}
        controller['ap']['enabled'] = False
        controller['epg'] = {}
        controller['epg']['enabled'] = False
        controller['bd'] = {}
        controller['bd']['enabled'] = False
        controller['bgp']['enabled'] = True

    for key in keys:
        if key not in controller:
            if mode == 'check' and controller['mo_name'] is None:
                controller[key] = None
            else:
                controller[key] = {}

        if controller[key] is not None:
            if 'managed' not in controller[key]:
                controller[key]['managed'] = True

            if 'enabled' not in controller[key]:
                controller[key]['enabled'] = True

            if 'shared' not in controller[key]:
                controller[key]['shared'] = False

            if 'name' not in controller[key]:
                if controller['mo_name'] is None:
                    my_output.error('controller.%s.name required or controller.mo_name for generated value' % (key))
                    return None

                if key == 'ap':
                    controller[key]['name'] = controller['mo_name']
                    continue

                if key == 'epg':
                    controller[key]['name'] = controller['domain']
                    continue

                if key == 'bd':
                    controller[key]['name'] = '%s-%s' % (controller['mo_name'], controller['domain'])
                    continue

                controller[key]['name'] = '%s-%s-%s' % (
                    controller['tenant'],
                    controller['mo_name'],
                    controller['domain']
                )

    # BGP

    if controller['bgp']['enabled']:
        if 'managed' not in controller['bgp']:
            controller['bgp']['managed'] = True

        if 'shared' not in controller['bgp']:
            controller['bgp']['shared'] = False

        if 'name' not in controller['bgp']:
            if controller['mo_name'] is None:
                my_output.error('controller.bgp.name required or controller.mo_name for generated value')
                return None

            controller['bgp']['name'] = controller['mo_name']

        if 'type' not in controller['bgp']:
            controller['bgp']['type'] = 'svi'

        if controller['bgp']['type'] not in ['svi']:
            my_output.error('Unsupported controller.bgp.type')
            return None

        if 'gateway' not in controller['bgp']:
            if interface_gateway is not None:
                controller['bgp']['gateway'] = interface_gateway
            else:
                my_output.error('controller.bgp.gateway required')
                return None

        if not ip_helper.is_valid_ipv4_cidr(controller['bgp']['gateway']):
            my_output.error('controller.bgp.gateway cidr required')
            return None

        if 'asn' not in controller['bgp']:
            my_output.error('controller.bgp.asn required')
            return None

        if not isinstance(controller['bgp']['asn'], int):
            my_output.error('controller.bgp.asn invalid - integer expected')
            return None

        if controller['bgp']['asn'] < 1 or controller['bgp']['asn'] > 65535:
            my_output.error('controller.bgp.asn invalid - out of range')
            return None

        if 'ttl' not in controller['bgp']:
            controller['bgp']['ttl'] = 5

        if not isinstance(controller['bgp']['ttl'], int):
            my_output.error('controller.bgp.ttl invalid')
            return None

        if controller['bgp']['ttl'] < 1 or controller['bgp']['ttl'] > 128:
            my_output.error('controller.bgp.ttl invalid')
            return None

        if 'l3out' not in controller['bgp']:
            controller['bgp']['l3out'] = {}

        if 'name' not in controller['bgp']['l3out']:
            if controller['mo_name'] is None:
                my_output.error('controller.bgp.l3out.name required or controller.mo_name for generated value')
                return None

            controller['bgp']['l3out']['name'] = controller['mo_name']

        if 'epg' not in controller['bgp']:
            controller['bgp']['epg'] = {}

        if 'name' not in controller['bgp']['epg']:
            if controller['mo_name'] is None:
                my_output.error('controller.bgp.epg.name required or controller.mo_name for generated value')
                return None

            controller['bgp']['epg']['name'] = controller['mo_name']

        if 'subnet' not in controller['epg']:
            controller['bgp']['epg']['subnet'] = []
            subnet_mo = {}
            subnet_mo['ip'] = ip_helper.get_network_cidr_from_cidr(
                controller['bgp']['gateway']
            )
            subnet_mo['scope'] = ['import-security']
            controller['bgp']['epg']['subnet'].append(subnet_mo)

        if controller['bgp']['type'] == 'svi':
            if 'leaf_A' not in controller['bgp']:
                my_output.error('controller.bgp.leaf_A structure required')
                return None

            if not isinstance(controller['bgp']['leaf_A'], dict):
                my_output.error('controller.bgp.leaf_A structure required')
                return None

            if 'leaf_B' not in controller['bgp']:
                my_output.error('controller.bgp.leaf_B structure required')
                return None

            if not isinstance(controller['bgp']['leaf_B'], dict):
                my_output.error('controller.bgp.leaf_B structure required')
                return None

            keys = [
                'id',
                'ip',
                'rtr_id'
            ]
            for key in keys:
                if key not in controller['bgp']['leaf_A']:
                    my_output.error('controller.bgp.leaf_A.%s required' % (key))
                    return None

                if not isinstance(controller['bgp']['leaf_A'][key], str):
                    my_output.error('controller.bgp.leaf_A.%s string required' % (key))
                    return None

                if key not in controller['bgp']['leaf_B']:
                    my_output.error('controller.bgp.leaf_B.%s required' % (key))
                    return None

                if not isinstance(controller['bgp']['leaf_B'][key], str):
                    my_output.error('controller.bgp.leaf_B.%s string required' % (key))
                    return None

            if not ip_helper.is_ipv4_in_cidr(controller['bgp']['leaf_A']['ip'], controller['bgp']['gateway']):
                my_output.error('controller.bgp.leaf_A.ip not in subnet')
                return None

            controller['bgp']['leaf_A']['cidr'] = '%s/%s' % (
                controller['bgp']['leaf_A']['ip'],
                controller['bgp']['gateway'].split('/')[1]
            )

            if not ip_helper.is_ipv4_in_cidr(controller['bgp']['leaf_B']['ip'], controller['bgp']['gateway']):
                my_output.error('controller.bgp.leaf_B.ip not in subnet')
                return None

            controller['bgp']['leaf_B']['cidr'] = '%s/%s' % (
                controller['bgp']['leaf_B']['ip'],
                controller['bgp']['gateway'].split('/')[1]
            )

            if not ip_helper.is_valid_ipv4_address(controller['bgp']['leaf_A']['rtr_id']):
                my_output.error('controller.bgp.leaf_A.rtr_id ip required')
                return None

            if not ip_helper.is_valid_ipv4_address(controller['bgp']['leaf_B']['rtr_id']):
                my_output.error('controller.bgp.leaf_B.rtr_id ip required')
                return None

            if 'loopback' not in controller['bgp']['leaf_A']:
                controller['bgp']['leaf_A']['loopback'] = True
                
            if not isinstance(controller['bgp']['leaf_A']['loopback'], bool):
                my_output.error('controller.bgp.leaf_A.loopback bool expected')
                return None

            if 'loopback' not in controller['bgp']['leaf_B']:
                controller['bgp']['leaf_B']['loopback'] = True
                
            if not isinstance(controller['bgp']['leaf_B']['loopback'], bool):
                my_output.error('controller.bgp.leaf_B.loopback bool expected')
                return None

        if 'lnp' not in controller['bgp']:
            controller['bgp']['lnp'] = {}

        if 'name' not in controller['bgp']['lnp']:
            if controller['mo_name'] is None:
                my_output.error('controller.bgp.lnp.name required or controller.mo_name for generated value')
                return None

            controller['bgp']['lnp']['name'] = '%s_%s' % (
                controller['bgp']['leaf_A']['id'],
                controller['bgp']['leaf_B']['id']
            )

        if 'lip' not in controller['bgp']['lnp']:
            controller['bgp']['lnp']['lip'] = controller['mo_name']

    # Policies

    keys = [
        'cdp',
        'lldp',
        'link_level',
        'l2'
    ]
    if interface_policy_type in ['pc', 'vpc']:
        keys.append(
            'port_channel'
        )

    for key in keys:
        if key not in controller or controller[key] is None:
            if mode == 'check' and controller['mo_name'] is None:
                controller[key] = None
            else:
                controller[key] = {}

        if controller[key] is not None:
            if 'managed' not in controller[key]:
                controller[key]['managed'] = True

            if 'enabled' not in controller[key]:
                controller[key]['enabled'] = True

            if 'shared' not in controller[key]:
                controller[key]['shared'] = False

            if 'name' not in controller[key]:
                if controller['mo_name'] is None:
                    my_output.error('controller.%s.name required or controller.mo_name for generated value' % (key))
                    return None

                controller[key]['name'] = '%s-%s-%s' % (
                    controller['tenant'],
                    controller['mo_name'],
                    controller['domain']
                )

            if key == 'cdp':
                if 'cdp_enabled' not in controller[key]:
                    controller[key]['cdp_enabled'] = True

            if key == 'lldp':
                if 'lldp_receive' not in controller[key]:
                    controller[key]['lldp_receive'] = True
                if 'lldp_transmit' not in controller[key]:
                    controller[key]['lldp_transmit'] = True

            if key == 'l2':
                if 'qinq' not in controller[key] or controller[key]['qinq'] is None:
                    controller[key]['qinq'] = 'disabled'

                if controller[key]['qinq'] not in ['disabled', 'core', 'double', 'edge']:
                    my_output.error('controller.%s.qinq unsupported value' % (key))
                    return None

                if 'relay' not in controller[key] or controller[key]['relay'] is None:
                    controller[key]['relay'] = False

                if not isinstance(controller[key]['relay'], bool):
                    my_output.error('controller.%s.relay unsupported value' % (key))
                    return None

                if 'vlan' not in controller[key] or controller[key]['vlan'] is None:
                    controller[key]['vlan'] = 'local'

                if controller[key]['vlan'] not in ['global', 'local']:
                    my_output.error('controller.%s.vlan unsupported value' % (key))
                    return None

            if key == 'link_level':
                if 'auto' not in controller[key] or controller[key]['auto'] is None:
                    controller[key]['auto'] = 'on'

                if controller[key]['auto'] not in ['on', 'off', 'enforce']:
                    my_output.error('controller.%s.auto unsupported value' % (key))
                    return None

                if 'media' not in controller[key] or controller[key]['media'] is None:
                    controller[key]['media'] = 'auto'

                if controller[key]['media'] not in ['auto', 'sfp10gtx']:
                    my_output.error('controller.%s.media unsupported value' % (key))
                    return None

                if 'debounce' not in controller[key] or controller[key]['debounce'] is None:
                    controller[key]['debounce'] = 100

                if not isinstance(controller[key]['debounce'], int):
                    my_output.error('controller.%s.debounce unsupported value' % (key))
                    return None

                if controller[key]['debounce'] < 0:
                    my_output.error('controller.%s.debounce unsupported value' % (key))
                    return None

                if 'delay' not in controller[key] or controller[key]['delay'] is None:
                    controller[key]['delay'] = 0

                if not isinstance(controller[key]['delay'], int):
                    my_output.error('controller.%s.delay unsupported value' % (key))
                    return None

                if controller[key]['delay'] < 0:
                    my_output.error('controller.%s.delay unsupported value' % (key))
                    return None

                if 'emi' not in controller[key] or controller[key]['emi'] is None:
                    controller[key]['emi'] = False

                if not isinstance(controller[key]['emi'], bool):
                    my_output.error('controller.%s.emi unsupported value' % (key))
                    return None

            if key == 'port_channel':
                if 'mode' not in controller[key] or controller[key]['mode'] is None:
                    controller[key]['mode'] = 'on'

                if controller[key]['mode'] not in ['on', 'active', 'passive', 'pinning', 'load', 'explicit']:
                    my_output.error('controller.%s.mode unsupported value' % (key))
                    return None

                if 'min' not in controller[key] or controller[key]['min'] is None:
                    controller[key]['min'] = 1

                if not isinstance(controller[key]['min'], int):
                    my_output.error('controller.%s.min unsupported value' % (key))
                    return None

                if controller[key]['min'] < 1:
                    my_output.error('controller.%s.min unsupported value' % (key))
                    return None

                if 'max' not in controller[key] or controller[key]['max'] is None:
                    controller[key]['max'] = 16

                if not isinstance(controller[key]['max'], int):
                    my_output.error('controller.%s.max unsupported value' % (key))
                    return None

                if controller[key]['max'] < 1 or controller[key]['max'] > 16:
                    my_output.error('controller.%s.min unsupported value' % (key))
                    return None

                if controller[key]['max'] < controller[key]['min']:
                    my_output.error('controller.%s.min/max combination' % (key))
                    return None

                if 'lb' not in controller[key] or controller[key]['lb'] is None:
                    controller[key]['lb'] = 'static'

                if controller[key]['lb'] not in ['static', 'dynamic']:
                    my_output.error('controller.%s.lb unsupported value' % (key))
                    return None

                if 'suspend' not in controller[key] or controller[key]['suspend'] is None:
                    controller[key]['suspend'] = True

                if not isinstance(controller[key]['suspend'], bool):
                    my_output.error('controller.%s.suspend unsupported value' % (key))
                    return None

                if 'graceful' not in controller[key] or controller[key]['graceful'] is None:
                    controller[key]['graceful'] = True

                if not isinstance(controller[key]['graceful'], bool):
                    my_output.error('controller.%s.graceful unsupported value' % (key))
                    return None

                if 'fast' not in controller[key] or controller[key]['fast'] is None:
                    controller[key]['fast'] = True

                if not isinstance(controller[key]['fast'], bool):
                    my_output.error('controller.%s.fast unsupported value' % (key))
                    return None

                if 'symmetric' not in controller[key] or controller[key]['symmetric'] is None:
                    controller[key]['symmetric'] = False

                if not isinstance(controller[key]['symmetric'], bool):
                    my_output.error('controller.%s.symmetric unsupported value' % (key))
                    return None

                if 'hash' not in controller[key]:
                    controller[key]['hash'] = None

                if controller[key]['hash'] is not None:
                    if controller[key]['hash'] not in ['dip', 'sip', 'sport', 'dport']:
                        my_output.error('controller.%s.hash unsupported value' % (key))
                        return None

    if interface_policy_type == 'individual':
        if mode in ['check']:
            controller['port_channel'] = None
        else:
            controller['port_channel'] = {}
            controller['port_channel']['enabled'] = False

    # VLAN Pool

    if controller['vlan_pool'] is not None:
        if 'vlan' not in controller['vlan_pool']:
            controller['vlan_pool']['vlan'] = interface_vlan

        if 'mode' not in controller['vlan_pool']:
            controller['vlan_pool']['mode'] = 'static'

        if controller['vlan_pool']['mode'] not in ['static']:
            my_output.error('controller.vlan_pool.mode set to static required')
            return None

    if controller['policy_group'] is not None:
        if 'type' not in controller['policy_group']:
            controller['policy_group']['type'] = interface_policy_type

        if controller['policy_group']['type'] not in ['vpc']:
            my_output.error('controller.policy_group.type must be one of [vpc]')
            return None

        if 'encap' not in controller['policy_group']:
            controller['policy_group']['encap'] = 'vlan-%s' % (interface_vlan)

        if 'immediacy' not in controller['policy_group']:
            controller['policy_group']['immediacy'] = 'immediate'

    if controller['bd'] is not None:
        if 'gateway' not in controller['bd']:
            if interface_gateway is not None:
                controller['bd']['gateway'] = interface_gateway
            else:
                my_output.error('controller.bd.gateway required')
                return None

        if not ip_helper.is_valid_ipv4_cidr(controller['bd']['gateway']):
            my_output.error('controller.bd.gateway cidr required')
            return None

    return controller


def validate_fabric_interface(interface, my_output):
    if 'ip' in interface:
        if not ip_helper.is_valid_ipv4_address(interface['ip']):
            my_output.error('server.interface.ip invalid')
            return None
    else:
        interface['ip'] = None

    if 'gateway' in interface:
        if not ip_helper.is_valid_ipv4_cidr(interface['gateway']):
            my_output.error('server.interface.gateway invalid')
            return None
    else:
        interface['gateway'] = None

    if 'mac' in interface:
        if not ip_helper.is_mac_address(interface['mac']):
            my_output.error('server.interface.mac invalid')
            return None
    else:
        interface['mac'] = None

    if 'mtu' not in interface:
        interface['mtu'] = "1500"

    if 'bond' not in interface:
        interface['bond'] = False

    if 'bond' in interface:
        if not isinstance(interface['bond'], bool):
            my_output.error('server.interface.bond invalid')
            return None

    if 'trunk' not in interface:
        my_output.error('server.interface.trunk required')
        return None

    if 'trunk' in interface:
        if not isinstance(interface['trunk'], bool):
            my_output.error('server.interface.trunk invalid')
            return None

    if 'vlan' not in interface:
        my_output.error('server.interface.vlan required')
        return None

    if 'vlan' in interface:
        if not isinstance(interface['vlan'], int):
            my_output.error('server.interface.vlan int required')
            return None

        interface['vlan'] = interface['vlan']

    keys = [
        'node',
        'port'
    ]
    for key in keys:
        if key not in interface:
            my_output.error('server.interface.%s required' % (key))
            return None

    return interface


def run(fabric, mode, my_output, log_id):
    aci_settings_handler = aci_settings.ApicSettings(log_id=None)

    if 'controller' not in fabric:
        my_output.error('fabric.controller required')
        return None

    if not isinstance(fabric['controller'], list):
        my_output.error('fabric.controller list required')
        return None

    domains = []
    for item in fabric['controller']:
        if not isinstance(item, dict):
            my_output.error('fabric.controller list of dict required')
            return None

        if 'type' not in item:
            my_output.error('fabric.controller.type required')
            return None

        if item['type'] not in ['aci']:
            my_output.error('fabric.controller.type unsupported')
            return None

        if item['type'] == 'apic':
            if 'apic' not in item:
                my_output.error('fabric.controller.apic required')
                return None

            if aci_settings_handler.get_apic_controller(item['apic']) is None:
                my_output.error('fabric.controller.apic invalid')
                return None

        if 'domain' not in item:
            my_output.error('fabric.controller.domain required')
            return None

        domains.append(
            item['domain']
        )

    if 'server' not in fabric:
        my_output.error('fabric.server required')
        return None

    if not isinstance(fabric['server'], list):
        my_output.error('fabric.server list required')
        return None

    for item in fabric['server']:
        if not isinstance(item, dict):
            my_output.error('fabric.server list of dict required')
            return None

        if 'hostname' not in item:
            my_output.error('fabric.server.hostname required')
            return None

        if 'interface' not in item:
            my_output.error('fabric.server.interface required')
            return None

        if not isinstance(item['interface'], list):
            my_output.error('fabric.server.interface list required')
            return None

        for interface in item['interface']:
            if not isinstance(interface, dict):
                my_output.error('fabric.server.interface list of dict required')
                return None

            if 'domain' not in interface:
                my_output.error('fabric.server.interface.domain required')
                return None

            if interface['domain'] not in domains:
                my_output.error('fabric.server.interface.domain must match controller')
                return None

            if 'name' not in interface:
                my_output.error('fabric.server.interface.name required')
                return None
            
    for server in fabric['server']:
        for interface in server['interface']:
            interface = validate_fabric_interface(interface, my_output)
            if interface is None:
                return None

    for controller in fabric['controller']:
        if controller['type'] == 'aci':
            domain_interface = []
            for server in fabric['server']:
                for interface in server['interface']:
                    if interface['domain'] == controller['domain']:
                        domain_interface.append(interface)

            controller = validate_fabric_controller_aci(controller, mode, domain_interface, my_output, log_id)
            if controller is None:
                return None

    return fabric