import json
from lib import filter_helper
from lib import ip_helper
from lib.workflow.ocp_fabric import common


def check_tenant(handler, tenant_name, my_output):
    if not handler.is_tenant(tenant_name):
        my_output.error('Tenant [%s] not found' % (tenant_name))
        return False

    my_output.default('- Tenant [%s] found' % (tenant_name))
    return True


def check_vrf(handler, tenant_name, vrf_name, my_output):
    in_tenant = handler.is_vrf(tenant_name, vrf_name)
    in_common = handler.is_vrf('common', vrf_name)

    if not in_tenant and not in_common:
        my_output.error('VRF [%s] not found in common and %s tenant' % (vrf_name, tenant_name))
        return False

    if in_tenant:
        my_output.default('- VRF [%s] found in %s tenant' % (vrf_name, tenant_name))
    else:
        my_output.default('- VRF [%s] found in common tenant' % (vrf_name))

    return True


def check_l3out(handler, tenant_name, l3out_name, my_output):
    in_tenant = handler.is_l3out(tenant_name, l3out_name)
    in_common = handler.is_l3out('common', l3out_name)

    if not in_tenant and not in_common:
        my_output.error('L3Out [%s] not found in common and %s tenants' % (l3out_name, tenant_name))
        return None

    if in_tenant:
        my_output.default('- L3Out [%s] found in %s tenant' % (l3out_name, tenant_name))
        return tenant_name

    my_output.default('- L3Out [%s] found in common tenant' % (l3out_name))
    return 'common'


def check_l3out_external_epg(handler, tenant_name, l3out_name, my_output):
    info = handler.get_l3out(
        tenant_name,
        l3out_name,
        cache_enabled=False
    )
    if info is None:
        my_output.error(
            'L3out [%s/%s] not found' % (
                tenant_name,
                l3out_name
            )
        )
        return None

    if info['l3extInstP'] is None or len(info['l3extInstP']) != 1:
        my_output.error(
            'Define controller.external_epg value valid for L3out [%s/%s]' % (
                tenant_name,
                l3out_name
            )
        )
        return None

    return info['l3extInstP'][0]['name']


def check_epg_name(handler, fabric, my_output):
    if fabric['epg'] is None:
        return True, fabric

    if len(fabric['epg']['name'].split('/')) not in [1, 3]:
        my_output.error('EPG [%s] format invalid' % (fabric['epg']['name']))
        return False, fabric

    if len(fabric['epg']['name'].split('/')) == 1:
        if fabric['tenant'] is None:
            my_output.error('EPG tenant required')
            return False, fabric

        if fabric['ap'] is None:
            my_output.error('EPG ap required')
            return False, fabric

        fabric['epg']['name'] = '%s/%s/%s' % (
            fabric['tenant'],
            fabric['ap']['name'],
            fabric['epg']['name']
        )

    if len(fabric['epg']['name'].split('/')) == 3:
        (epg_tenant, epg_ap, epg_name) = fabric['epg']['name'].split('/')
        if fabric['tenant'] is None:
            fabric['tenant'] = epg_tenant

        if fabric['ap'] is None:
            fabric['ap'] = {}
            fabric['ap']['name'] = epg_ap

        if fabric['tenant'] != epg_tenant:
            my_output.error('EPG tenant mismatch')
            return False, fabric

        if fabric['ap']['name'] != epg_ap:
            my_output.error('EPG application profile mismatch')
            return False, fabric

    return True, fabric


def check_vlan_pool(handler, fabric, my_output):
    if fabric['vlan_pool'] is None:
        my_output.default('- VLAN pool not defined')
        return True

    if not fabric['vlan_pool']['enabled']:
        my_output.default('- VLAN pool not enabled')
        return True

    if not handler.is_pool_vlan(fabric['vlan_pool']['name'], cache_enabled=False):
        my_output.error('VLAN pool [%s] not found' % (fabric['vlan_pool']['name']))
        return False

    my_output.default('- VLAN pool [%s] found' % (fabric['vlan_pool']['name']))

    if 'vlan' in fabric['vlan_pool']:
        info = handler.get_pool_vlan(
            fabric['vlan_pool']['name'],
            cache_enabled=False
        )
        vlans = filter_helper.get_values_from_range(fabric['vlan_pool']['vlan'])
        all_found = True
        for vlan in vlans:
            found = False
            for vlan_block_info in info['fvnsEncapBlk']:
                if int(vlan_block_info['fromVlan']) <= vlan <= int(vlan_block_info['toVlan']):
                    found = True

            all_found = all_found and found

        if all_found:
            my_output.default('\tVlans [%s] match' % (fabric['vlan_pool']['vlan']))
        else:
            my_output.error('VLAN pool [%s] missing some vlans [%s]' % (fabric['vlan_pool']['name'], fabric['vlan_pool']['vlan']))
            return False

    return True


def check_aaep(handler, fabric, my_output):
    if fabric['aaep'] is None:
        my_output.default('- aaep not defined')
        return True

    if not fabric['aaep']['enabled']:
        my_output.default('- aaep not enabled')
        return True

    if not handler.is_policy_global_aae(fabric['aaep']['name'], cache_enabled=False):
        my_output.error('AAEP [%s] not found' % (fabric['aaep']['name']))
        return False

    my_output.default('- AAEP [%s] found' % (fabric['aaep']['name']))
    return True


def check_physical_domain(handler, fabric, my_output):
    if fabric['physical_domain'] is None:
        my_output.default('- phys domain not defined')
        return True

    if not fabric['physical_domain']['enabled']:
        my_output.default('- phys domain not enabled')
        return True

    if not handler.is_domain_phy(fabric['physical_domain']['name'], cache_enabled=False):
        my_output.error('Physical domain [%s] not found' % (fabric['physical_domain']['name']))
        return False

    my_output.default('- Physical domain [%s] found' % (fabric['physical_domain']['name']))

    success = True

    info = handler.get_domain_phy(
        fabric['physical_domain']['name'],
        cache_enabled=False
    )

    if fabric['vlan_pool'] is not None:
        if info['vlan'] == fabric['vlan_pool']['name']:
            my_output.default('\tVLAN pool [%s] match' % (fabric['vlan_pool']['name']))
        else:
            my_output.error('Physical domain [%s] vlan pool mismatch [%s] expected [%s]' % (fabric['physical_domain']['name'], info['vlan'], fabric['vlan_pool']['name']))
            success = False

    if fabric['aaep'] is not None:
        if fabric['aaep']['name'] in info['aaep_names']:
            my_output.default('\tAAEP [%s] match' % (fabric['aaep']['name']))
        else:
            my_output.error('Physical domain [%s] aaep mismatch [%s] expected [%s]' % (fabric['physical_domain']['name'], ','.join(info['aaep_names']), fabric['aaep']['name']))
            success = False

    return success


def check_l3_domain(handler, fabric, my_output):
    if fabric['l3_domain'] is None:
        my_output.default('- l3 domain not defined')
        return True

    if not fabric['l3_domain']['enabled']:
        my_output.default('- l3 domain not enabled')
        return True

    if not handler.is_domain_l3(fabric['l3_domain']['name'], cache_enabled=False):
        my_output.error('L3 domain [%s] not found' % (fabric['l3_domain']['name']))
        return False

    my_output.default('- L3 domain [%s] found' % (fabric['l3_domain']['name']))

    success = True

    info = handler.get_domain_l3(
        fabric['l3_domain']['name'],
        cache_enabled=False
    )

    if fabric['vlan_pool'] is not None:
        if info['vlan'] == fabric['vlan_pool']['name']:
            my_output.default('\tVLAN pool [%s] match' % (fabric['vlan_pool']['name']))
        else:
            my_output.error('L3 domain [%s] vlan pool mismatch [%s] expected [%s]' % (fabric['l3_domain']['name'], info['vlan'], fabric['vlan_pool']['name']))
            success = False

    if fabric['aaep'] is not None:
        if fabric['aaep']['name'] in info['aaep_names']:
            my_output.default('\tAAEP [%s] match' % (fabric['aaep']['name']))
        else:
            my_output.error('L3 domain [%s] aaep mismatch [%s] expected [%s]' % (fabric['l3_domain']['name'], ','.join(info['aaep_names']), fabric['aaep']['name']))
            success = False

    return success


def check_policy_group(handler, fabric, servers, my_output):
    if fabric['policy_group'] is None:
        my_output.default('- Policy group not defined')
        return True

    if not fabric['policy_group']['enabled']:
        my_output.default('- Policy group not enabled')
        return True

    vpc_policies = []

    if fabric['policy_group']['type'] == 'vpc':
        if len(servers) == 1:
            vpc_policies.append(
                fabric['policy_group']['name']
            )

        if len(servers) > 1:
            index = 1
            for server in servers:
                policy_name = '%s-%s' % (fabric['policy_group']['name'], index)
                vpc_policies.append(
                    policy_name
                )
                index += 1

    success = True

    for policy_name in vpc_policies:
        if not handler.is_policy_group_access_interface_vpc(policy_name, cache_enabled=False):
            my_output.error('PolicyGroup [%s] not found' % (policy_name))
            success = False
            continue

        my_output.default('- PolicyGroup [%s]' % (policy_name))

        info = handler.get_configuration_vpc(
            policy_name,
            cache_enabled=False
        )
        if info is None:
            my_output.error('PolicyGroup not configured on any interface')
            success = False
            continue

        if len(info['interfaces']) == 0:
            my_output.error('PolicyGroup not configured on any interface')
            success = False
            continue

        for interface in info['interfaces']:
            my_output.default('\tConfigured interface: pod [%s] node [%s] interface [%s]' % (
                interface['pod'],
                interface['node'],
                interface['interfaceId']
            ))

        info = handler.get_policy_group_access_interface_vpc(
            policy_name,
            node_info=True,
            cache_enabled=False
        )

        if fabric['cdp'] is not None and fabric['cdp']['enabled']:
            if 'infraRsCdpIfPol' not in info or info['infraRsCdpIfPol']['name'] != fabric['cdp']['name']:
                my_output.error('PolicyGroup [%s] CDP policy expected [%s]' % (fabric['policy_group']['name'], fabric['cdp']['name']))
                success = False
            else:
                my_output.default('\tCDP policy [%s] match' % (fabric['cdp']['name']))

        if fabric['lldp'] is not None and fabric['lldp']['enabled']:
            if 'infraRsLldpIfPol' not in info or info['infraRsLldpIfPol']['name'] != fabric['lldp']['name']:
                my_output.error('PolicyGroup [%s] LLDP policy expected [%s]' % (fabric['policy_group']['name'], fabric['lldp']['name']))
                success = False
            else:
                my_output.default('\tLLDP policy [%s] match' % (fabric['lldp']['name']))

        if fabric['link_level'] is not None and fabric['link_level']['enabled']:
            if 'infraRsHIfPol' not in info or info['infraRsHIfPol']['name'] != fabric['link_level']['name']:
                my_output.error('PolicyGroup [%s] link level policy expected [%s]' % (fabric['policy_group']['name'], fabric['link_level']['name']))
                success = False
            else:
                my_output.default('\tLink level policy [%s] match' % (fabric['link_level']['name']))

        if fabric['port_channel'] is not None and fabric['port_channel']['enabled']:
            if 'infraRsLacpPol' not in info or info['infraRsLacpPol']['name'] != fabric['port_channel']['name']:
                my_output.error('PolicyGroup [%s] port channel policy expected [%s]' % (fabric['policy_group']['name'], fabric['port_channel']['name']))
                success = False
            else:
                my_output.default('\tPort channel policy [%s] match' % (fabric['port_channel']['name']))

        if fabric['l2'] is not None and fabric['l2']['enabled']:
            if 'infraRsL2IfPol' not in info or info['infraRsL2IfPol']['name'] != fabric['l2']['name']:
                my_output.error('PolicyGroup [%s] l2 policy expected [%s]' % (fabric['policy_group']['name'], fabric['l2']['name']))
                success = False
            else:
                my_output.default('\tL2 policy [%s] match' % (fabric['l2']['name']))

        if 'interface' not in info or info['interface'] is None:
            my_output.error('PolicyGroup [%s] not deployed on any interface' % (fabric['policy_group']['name']))
            success = False
            continue

        for interface in info['interface']:
            my_output.default('\tDeployed on pod-%s:node-%s:%s' % (interface['pod_id'], interface['node_id'], interface['intf_name']))

            found = False
            for server in servers:
                for server_interface in server['interface']:
                    if server_interface['domain'] == fabric['domain']:
                        if server_interface['pod'] != interface['pod_id']:
                            continue

                        if server_interface['node'] != interface['node_id']:
                            continue

                        if 'eth%s' % (server_interface['port']) != interface['intf_name']:
                            continue

                        my_output.default('\tServer [%s] interface mac [%s]' % (server['hostname'], server_interface['mac']))
                        found = True

            if not found:
                my_output.error('No server found')
                success = False

    return success


def check_application_profile(handler, fabric, my_output):
    if fabric['ap'] is None:
        my_output.default('- Application profile not defined')
        return True

    if not fabric['ap']['enabled']:
        my_output.default('- Application profile not enabled')
        return True

    if not handler.is_application_profile(fabric['ap']['name'], tenant_name=fabric['tenant'], cache_enabled=False):
        my_output.error('Application profile [%s] not found in tenant [%s]' % (fabric['ap']['name'], fabric['tenant']))
        return False

    my_output.default('- Application profile [%s] found' % (fabric['ap']['name']))
    my_output.default('\tTenant [%s] match' % (fabric['tenant']))
    return True


def check_epg(handler, fabric, my_output):
    if fabric['epg'] is None:
        my_output.default('- epg not defined')
        return True

    if not fabric['epg']['enabled']:
        my_output.default('- epg not enabled')
        return True

    is_epg = handler.is_epg(
        fabric['epg']['name'].split('/')[0],
        fabric['epg']['name'].split('/')[1],
        fabric['epg']['name'].split('/')[2],
        cache_enabled=False
    )
    if not is_epg:
        my_output.error('EPG [%s] not found' % (fabric['epg']['name']))
        return False

    my_output.default('- EPG [%s] found' % (fabric['epg']['name']))

    info = handler.get_epg(
        fabric['epg']['name'].split('/')[0],
        fabric['epg']['name'].split('/')[1],
        fabric['epg']['name'].split('/')[2],
        node_info=True,
        cache_enabled=False
    )

    success = True

    if fabric['bd'] is not None:
        if info['bd_name'] == fabric['bd']['name']:
            my_output.default('\tBridge Domain [%s] match' % (fabric['bd']['name']))
        else:
            my_output.error('EPG [%s] bridge domain mismatch [%s] vs. [%s]' % (fabric['epg']['name'], fabric['bd']['name'], info['bd_name']))
            success = False

    if 'policy_group' in fabric:
        if 'staticPort' in info and len(info['staticPort']) > 0:
            found = False
            for static_port in info['staticPort']:
                if 'pathEp' in static_port and static_port['pathEp'] == fabric['policy_group']['name']:
                    my_output.default('\tStatic port [%s] match' % (static_port['pathEp']))
                    found = True

    return success


def check_bd(handler, fabric, my_output):
    if fabric['bd'] is None:
        my_output.default('- bridge domain not defined')
        return True

    if not fabric['bd']['enabled']:
        my_output.default('- bridge domain not enabled')
        return True

    if not handler.is_bridge_domain(fabric['tenant'], fabric['bd']['name'], cache_enabled=False):
        my_output.error('Bridge Domain [%s] not found in tenant [%s]' % (fabric['bd']['name'], fabric['tenant']))
        return False

    my_output.default('- Bridge Domain [%s] found' % (fabric['bd']['name']))
    my_output.default('\tTenant [%s] match' % (fabric['tenant']))

    info = handler.get_bridge_domain(
        fabric['tenant'],
        fabric['bd']['name'],
        cache_enabled=False
    )

    success = True
    if 'gateway' in fabric['bd']:
        found = False
        if 'fvSubnet' in info and info['fvSubnet'] is not None:
            for subnet_mo in info['fvSubnet']:
                if subnet_mo['ip'] == fabric['bd']['gateway']:
                    found = True

        if found:
            my_output.default('\tGateway [%s] match' % (fabric['bd']['gateway']))
        else:
            my_output.error('Bridge Domain [%s] gateway [%s] mismatch' % (fabric['bd']['name'], fabric['bd']['gateway']))
            success = False

    if 'l3out' in fabric['bd']:
        found = False
        if 'fvRsBDToOut' in info and info['fvRsBDToOut'] is not None:
            for l3out_mo in info['fvRsBDToOut']:
                if fabric['bd']['l3out'] == l3out_mo['name']:
                    found = True

        if found:
            my_output.default('\tL3out [%s] match' % (fabric['bd']['l3out']))
        else:
            my_output.error('Bridge Domain [%s] l3out [%s] mismatch' % (fabric['bd']['name'], fabric['bd']['l3out']))
            success = False

    return success


def check_interface(handler, fabric, interface, policy_index, my_output):
    my_output.default('\nInterface pod-%s:node-%s:%s' % (interface['pod'], interface['node'], interface['port']))
    info = handler.get_interface_phy(
        interface['pod'],
        interface['node'],
        'eth%s' % (interface['port']),
        policy_info=True,
        pc_info=True,
        epg_stats_info=True,
        cache_enabled=False
    )
    if info is None:
        my_output.error('Interface not found')
        return False

    if 'epg_stats' not in info:
        info['epg_stats'] = None

    success = True

    my_output.default('- Interface found')
    if info['stats'] is None:
        success = False
        my_output.error('Missing interface stats (breakout parent interface?)')
    else:
        my_output.default('\tOperational State %s' % (info['stats']['operSt']))
        my_output.default('\tSwitching State %s' % (info['switchingSt']))
        if info['switchingSt'] != 'enabled':
            success = False
            my_output.error('Switching not enabled (port not configured?)')

        my_output.default('\tUsage %s' % (info['usage']))
        if info['usage'] != 'epg':
            success = False
            my_output.error('Usage epg expected (port not configured?)')

        my_output.default('\tOperational Mode %s' % (info['stats']['operMode']))
        my_output.default('\tOperational Speed %s' % (info['stats']['operSpeed']))

    expected_epg = None
    if fabric['check_mode'] == 'full':
        if fabric['epg'] is not None and fabric['epg']['enabled']:
            expected_epg = fabric['epg']['name']

    if 'ip' in interface:
        ep_filter = ['ip:%s' % (interface['ip'])]
        ep_infos = handler.get_endpoints(
            endpoint_filter=ep_filter,
            fabric_info=True,
            cache_enabled=False
        )

        ep_interfaces = []
        if len(ep_infos) == 0:
            my_output.default('\tIP endpoint [%s] not found' % (interface['ip']))

        if len(ep_infos) > 0 and expected_epg is None:
            my_output.default('\tIP endpoint [%s] found' % (interface['ip']))
            for ep_info in ep_infos:
                my_output.default('\t- %s' % (ep_info['epgNameApTenant']))
                if 'fabric' in ep_info and ep_info['fabric'] is not None:
                    for ep_fabric in ep_info['fabric']:
                        ep_interfaces.append(
                            '%s:%s:%s' % (ep_fabric['pod_id'], ep_fabric['node_id'], ep_fabric['port_id'].replace('eth', ''))
                        )
                        my_output.default('\t\t%s' % (ep_fabric['ep']))

        if len(ep_infos) > 0 and expected_epg is not None:
            ep_success = True
            my_output.default('\tIP endpoint [%s] found' % (interface['ip']))
            for ep_info in ep_infos:
                my_output.default('\t- %s' % (ep_info['epgNameApTenant']))
                if 'fabric' in ep_info and ep_info['fabric'] is not None:
                    for ep_fabric in ep_info['fabric']:
                        ep_interfaces.append(
                            '%s:%s:%s' % (ep_fabric['pod_id'], ep_fabric['node_id'], ep_fabric['port_id'].replace('eth', ''))
                        )
                        my_output.default('\t\t%s' % (ep_fabric['ep']))

                if ep_info['epgNameApTenant'] != expected_epg:
                    success = False
                    ep_success = False

            if ep_success:
                my_output.default('\tIP endpoint with EPG match')
            else:
                my_output.error('IP Endpoint with EPG mismatch [%s]' % (expected_epg))

        if len(ep_interfaces) > 0:
            if '%s:%s:%s' % (interface['pod'], interface['node'], interface['port']) in ep_interfaces:
                my_output.default('\tIP endpoint found on the server interface (reinstallation)')
            else:
                my_output.error('IP endpoint found on different interfaces')
                success = False

    if 'mac' in interface:
        ep_filter = ['mac:%s' % (interface['mac'])]
        ep_infos = handler.get_endpoints(
            endpoint_filter=ep_filter,
            fabric_info=True,
            cache_enabled=False
        )

        ep_interfaces = []
        if len(ep_infos) == 0:
            my_output.default('\tMAC endpoint [%s] not found' % (interface['mac']))

        if len(ep_infos) > 0 and expected_epg is None:
            my_output.default('\tMAC endpoint [%s] found' % (interface['mac']))
            for ep_info in ep_infos:
                my_output.default('\t- %s' % (ep_info['epgNameApTenant']))
                if 'fabric' in ep_info and ep_info['fabric'] is not None:
                    for ep_fabric in ep_info['fabric']:
                        ep_interfaces.append(
                            '%s:%s:%s' % (ep_fabric['pod_id'], ep_fabric['node_id'], ep_fabric['port_id'].replace('eth', ''))
                        )
                        my_output.default('\t\t%s' % (ep_fabric['ep']))

        if len(ep_infos) > 0 and expected_epg is not None:
            ep_success = True
            my_output.default('\tMAC endpoint [%s] found' % (interface['mac']))
            for ep_info in ep_infos:
                my_output.default('\t- %s' % (ep_info['epgNameApTenant']))
                if 'fabric' in ep_info and ep_info['fabric'] is not None:
                    for ep_fabric in ep_info['fabric']:
                        ep_interfaces.append(
                            '%s:%s:%s' % (ep_fabric['pod_id'], ep_fabric['node_id'], ep_fabric['port_id'].replace('eth', ''))
                        )
                        my_output.default('\t\t%s' % (ep_fabric['ep']))

                if ep_info['epgNameApTenant'] != expected_epg:
                    success = False
                    ep_success = False

            if ep_success:
                my_output.default('\tMAC endpoint with EPG match')
            else:
                my_output.error('MAC Endpoint with EPG mismatch [%s]' % (expected_epg))

        if len(ep_interfaces) > 0:
            if '%s:%s:%s' % (interface['pod'], interface['node'], interface['port']) in ep_interfaces:
                my_output.default('\tMAC endpoint found on the server interface (reinstallation)')
            else:
                my_output.error('MAC endpoint found on different interfaces')
                success = False

    if expected_epg is not None and info['epg_stats'] is not None:
        found = False
        for epg_stats in info['epg_stats']:
            if epg_stats['nameApTenant'] == expected_epg:
                my_output.default('- EPG [%s] match' % (epg_stats['nameApTenant']))
                found = True

                bd_info = handler.get_bridge_domain(
                    epg_stats['bd_tenant_name'],
                    epg_stats['bd_name'],
                    cache_enabled=False
                )
                if bd_info is None:
                    success = False
                    my_output.error('Bridge domain associated with EPG not found [%s/%s]' % (epg_stats['bd_tenant_name'], epg_stats['bd_name']))
                    continue

                if 'bd' not in fabric or not fabric['bd']['enabled']:
                    my_output.default('- Bridge Domain [%s/%s] likely match' % (epg_stats['bd_tenant_name'], epg_stats['bd_name']))
                    continue

                my_output.default('- Bridge Domain [%s/%s] match' % (epg_stats['bd_tenant_name'], epg_stats['bd_name']))
                if 'ip' not in interface:
                    continue

                if 'fvSubnet' not in bd_info or bd_info['fvSubnet'] is None:
                    success = False
                    my_output.error('Bridge Domain [%s/%s] has not associated subnets' % (epg_stats['bd_tenant_name'], epg_stats['bd_name']))
                    continue

                cidr = None
                for subnet_mo in bd_info['fvSubnet']:
                    if ip_helper.is_ipv4_in_cidr(interface['ip'], subnet_mo['network']):
                        cidr = subnet_mo['network']

                if cidr is not None:
                    my_output.default('\tBridge domain subnet [%s] match' % (cidr))
                else:
                    my_output.error('Bridge Domain subnet mismatch for IP [%s]' % (interface['ip']))
                    success = False

        if not found:
            my_output.error('EPG [%s] may not be enabled on interface' % (expected_epg))
            success = False

    if 'trunk' in interface:
        if interface['trunk']:
            if info['mode'] == 'trunk':
                my_output.default('- Trunk mode match')
            else:
                my_output.error('Trunk mode mismatch')
                success = False

        if not interface['trunk']:
            if info['mode'] == 'trunk':
                my_output.error('Trunk mode mismatch')
                success = False
            else:
                my_output.default('- Trunk mode match')

    if 'vlan' in interface:
        if info['epg_stats'] is None:
            my_output.error('Cannot confirm if VLAN [%s] is configured on an interface' % (interface['vlan']))
            success = False
        else:
            found = False
            for epg_stats in info['epg_stats']:
                if 'vlan' in epg_stats and epg_stats['vlan'] is not None:
                    if epg_stats['vlan']['encap'] == 'vlan-%s' % (interface['vlan']):
                        found = True

                if 'staticPort' in epg_stats and epg_stats['staticPort'] is not None:
                    for static_port_mo in epg_stats['staticPort']:
                        if static_port_mo['encap'] == 'vlan-%s' % (interface['vlan']):
                            found = True

            if found:
                my_output.default('- VLAN [%s] match' % (interface['vlan']))
            else:
                my_output.error('VLAN [%s] may not be enabled' % (interface['vlan']))
                success = True

    if 'bond' in interface and interface['bond']:
        if 'policy_selector' not in info or info['policy_selector'] is None:
            my_output.error('No policy selector found')
            success = False
        else:
            if info['policy_selector']['policy_group_type'] != 'infraAccBndlGrp':
                my_output.error('PC/VPC policy expected')
                success = False

            if fabric['check_mode'] == 'partial':
                my_output.default('- PolicyGroup [%s]' % (info['policy_selector']['policy_group_name']))

            if fabric['check_mode'] == 'full':
                if fabric['policy_group'] is not None and fabric['policy_group']['enabled']:
                    expected_policy_group_name = fabric['policy_group']['name']
                    if policy_index is not None:
                        expected_policy_group_name = '%s-%s' % (expected_policy_group_name, policy_index)

                    if info['policy_selector']['policy_group_name'] == expected_policy_group_name:
                        my_output.default('- PolicyGroup [%s] match' % (info['policy_selector']['policy_group_name']))
                    else:
                        my_output.default('- PolicyGroup mismatch [%s] vs. [%s]' % (info['policy_selector']['policy_group_name'], expected_policy_group_name))
                        success = False

        is_bonding = True

        if info['stats'] is None:
            is_bonding = False
            success = False

        if info['stats'] is not None and 'bundleIndex' not in info['stats']:
            my_output.error('Interface bundle index unknown')
            success = False
            is_bonding = False

        if is_bonding:
            my_output.default('- Bonding enabled')

    return success


def run(fabric, servers, my_output, log_id, show_input=True):
    my_output.default('\nApic [%s] domain [%s] configuration' % (fabric['apic'], fabric['domain']), underline=True)
    success = True
    
    if show_input:
        my_output.default('Validated and resolved fabric configuration intent', before_newline=True)
        my_output.default(json.dumps(fabric, indent=4))
        my_output.default('Validated and resolved servers connectivity layout', before_newline=True)
        my_output.default(json.dumps(servers, indent=4))

    domain_servers = common.get_domain_servers(
        fabric['domain'],
        servers
    )
    if len(domain_servers) == 0:
        my_output.error(
            'No server associated with domain: %s' % (fabric['domain'])
        )
        return False

    handler = common.get_handler('aci', fabric['apic'], my_output, log_id)
    if handler is None:
        return False

    if fabric['check_mode'] == 'partial':
        success = True

    if fabric['check_mode'] == 'full':
        if not fabric['bgp']['enabled']:
            success, fabric = check_epg_name(handler, fabric, my_output)

        if not check_tenant(handler, fabric['tenant'], my_output):
            success = False

        if not check_vlan_pool(handler, fabric, my_output):
            success = False

        if not check_physical_domain(handler, fabric, my_output):
            success = False

        if not check_l3_domain(handler, fabric, my_output):
            success = False

        if not check_aaep(handler, fabric, my_output):
            success = False

        if not check_policy_group(handler, fabric, domain_servers, my_output):
            success = False

        if not fabric['bgp']['enabled']:
            if not check_application_profile(handler, fabric, my_output):
                success = False

            if not check_epg(handler, fabric, my_output):
                success = False

            if not check_bd(handler, fabric, my_output):
                success = False

    index = 1
    for server in servers:
        my_output.default('\nServer [%s] interfaces in domain [%s]' % (server['hostname'], fabric['domain']), underline=True)
        for interface in server['interface']:
            if interface['domain'] == fabric['domain']:
                if len(servers) == 1:
                    if not check_interface(handler, fabric, interface, None, my_output):
                        success = False
                else:
                    if not check_interface(handler, fabric, interface, index, my_output):
                        success = False

        index += 1

    return success


def validate(handler, fabric, servers, my_output):
    domain_servers = common.get_domain_servers(
        fabric['domain'],
        servers
    )
    if len(domain_servers) == 0:
        my_output.error(
            'No server associated with domain: %s' % (fabric['domain'])
        )
        return None, None

    my_output.default('Checks')
    if not check_tenant(handler, fabric['tenant'], my_output):
        return None, None

    if not check_vrf(handler, fabric['tenant'], fabric['vrf'], my_output):
        return None, None

    fabric['l3out_tenant'] = check_l3out(handler, fabric['tenant'], fabric['l3out'], my_output)
    if fabric['l3out_tenant'] is None:
        return None, None

    if fabric['bgp']['enabled']:
        if 'external_epg' in fabric:
            if not handler.is_l3out_external_epg(fabric['l3out_tenant'], fabric['l3out'], fabric['external_epg']):
                my_output.error(
                    'External EPG [%s] not found in L3out [%s/%s]' % (
                        fabric['external_epg'],
                        fabric['l3out_tenant'],
                        fabric['l3out']
                    )
                )
                return None, None
        else:
            fabric['external_epg'] = check_l3out_external_epg(handler, fabric['l3out_tenant'], fabric['l3out'], my_output)
            if fabric['external_epg'] is None:
                return None, None

        my_output.default('- L3Out External EPG [%s] found' % (fabric['external_epg']))

    if not fabric['bgp']['enabled']:
        success, fabric = check_epg_name(handler, fabric, my_output)
        if not success:
            return None, None

    return fabric, domain_servers