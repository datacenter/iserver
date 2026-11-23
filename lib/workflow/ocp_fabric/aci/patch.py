import json
from lib import ip_helper
from lib import log_helper
from lib.workflow.ocp_fabric.aci import check
from lib.workflow.ocp_fabric import common
from lib.workflow.ocp_fabric.aci import bgp


def configure_vlan_pool(handler, fabric, my_output):
    my_output.default('VLAN Pool', before_newline=True)
    if not fabric['vlan_pool']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tEnabled')
    pool_name = fabric['vlan_pool']['name']
    vlans = fabric['vlan_pool']['vlan']

    my_output.default('\tPool [%s] with vlans [%s]' % (pool_name, vlans))
    my_output.default('\tManaged mode [%s]' % (fabric['vlan_pool']['managed']))

    info = handler.get_pool_vlan(
        pool_name,
        cache_enabled=False
    )
    if info is not None:
        my_output.default('\t- already defined')

        inconsistent = handler.check_pool_vlan_consistency(
            info['fvnsEncapBlk'],
            vlans
        )
        if len(inconsistent) > 0:
            my_output.error('VLAN inconsistency between requested and configured: %s' % (','.join(inconsistent)))
            return False

        my_output.default('\t- vlans consistency verified')
        return True

    if not fabric['vlan_pool']['managed']:
        my_output.error('VLAN pool not found')
        return False

    my_output.default('\t- VLAN pool will be created')

    blocks = []
    for item in fabric['vlan_pool']['vlan'].split(','):
        if len(item.split('-')) == 1:
            blocks.append(
                '%s-%s' % (item, item)
            )
        else:
            blocks.append(item)

    success, error = handler.create_pool_vlan(
        pool_name,
        blocks,
        wait=True
    )
    if not success:
        my_output.error('VLAN pool create failed: %s' % (error))
        return False

    my_output.default('\t- VLAN pool created')
    return True


def configure_physical_domain(handler, fabric, my_output):
    my_output.default('Physical Domain', before_newline=True)
    if not fabric['physical_domain']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tEnabled')
    domain_name = fabric['physical_domain']['name']
    my_output.default('\tName [%s]' % (domain_name))
    my_output.default('\tManaged mode [%s]' % (fabric['physical_domain']['managed']))

    info = handler.get_domain_phy(
        domain_name,
        cache_enabled=False
    )
    if info is not None:
        my_output.default('\t- already defined')
        if not fabric['vlan_pool']['enabled']:
            my_output.default('Skipping domain to vlan pool association check')
            return True

        if 'vlan' not in info or info['vlan'] is None:
            if not fabric['physical_domain']['managed']:
                my_output.error('Association with vlan pool [%s] must be defined' % (fabric['vlan_pool']['name']))
                return False

            my_output.default('\t- domain association with vlan pool will be defined')
            success, error = handler.add_domain_phy_vlan_pool(
                domain_name,
                fabric['vlan_pool']['name'],
                fabric['vlan_pool']['mode']
            )
            if not success:
                my_output.error('Domain association with vlan pool failed: %s' % (error))
                return False

            my_output.default('Domain associated with vlan pool [%s]' % (fabric['vlan_pool']['name']))
            return True

        if info['vlan'] != fabric['vlan_pool']['name']:
            my_output.error('Inconsistency of domain association with vlan pool: %s vs. %s' % (info['vlan'], fabric['vlan_pool']['name']))
            return False

        my_output.default('\t- association with vlan pool [%s] consistency checked' % (fabric['vlan_pool']['name']))
        return True

    if not fabric['physical_domain']['managed']:
        my_output.error('Physical domain not found')
        return False

    my_output.default('\t- physical domain will be created')

    pool_name = None
    if fabric['vlan_pool']['enabled']:
        pool_name = fabric['vlan_pool']['name']
        my_output.default('\t- associated with vlan pool [%s]' % (pool_name))

        if not handler.is_pool_vlan(pool_name, cache_enabled=False):
            my_output.error('VLAN pool [%s] not found' % (pool_name))
            return False

    success, error = handler.create_domain_phy(
        domain_name,
        pool=pool_name,
        wait=True
    )
    if not success:
        my_output.error('Physical domain create failed: %s' % (error))
        return False

    my_output.default('\t- phys domain created')
    return True


def configure_l3_domain(handler, fabric, my_output):
    my_output.default('L3 Domain', before_newline=True)
    if not fabric['l3_domain']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tEnabled')
    domain_name = fabric['l3_domain']['name']
    my_output.default('\tName [%s]' % (domain_name))
    my_output.default('\tManaged mode [%s]' % (fabric['l3_domain']['managed']))

    info = handler.get_domain_l3(
        domain_name,
        cache_enabled=False
    )
    if info is not None:
        my_output.default('\t- already defined')
        if not fabric['vlan_pool']['enabled']:
            my_output.default('Skipping domain to vlan pool association check')
            return True

        if 'vlan' not in info or info['vlan'] is None:
            if not fabric['l3_domain']['managed']:
                my_output.error('Association with vlan pool [%s] must be defined' % (fabric['vlan_pool']['name']))
                return False

            my_output.default('\t- domain association with vlan pool will be defined')
            success, error = handler.add_domain_l3_vlan_pool(
                domain_name,
                fabric['vlan_pool']['name'],
                fabric['vlan_pool']['mode']
            )
            if not success:
                my_output.error('Domain association with vlan pool failed: %s' % (error))
                return False

            my_output.default('Domain associated with vlan pool [%s]' % (fabric['vlan_pool']['name']))
            return True

        if info['vlan'] != fabric['vlan_pool']['name']:
            my_output.error('Inconsistency of domain association with vlan pool: %s vs. %s' % (info['vlan'], fabric['vlan_pool']['name']))
            return False

        my_output.default('\t- association with vlan pool [%s] consistency checked' % (fabric['vlan_pool']['name']))
        return True

    if not fabric['l3_domain']['managed']:
        my_output.error('L3 domain not found')
        return False

    my_output.default('\t- l3 domain will be created')

    pool_name = None
    if fabric['vlan_pool']['enabled']:
        pool_name = fabric['vlan_pool']['name']
        my_output.default('\t- associated with vlan pool [%s]' % (pool_name))

        if not handler.is_pool_vlan(pool_name, cache_enabled=False):
            my_output.error('VLAN pool [%s] not found' % (pool_name))
            return False

    success, error = handler.create_domain_l3(
        domain_name,
        pool=pool_name,
        wait=True
    )
    if not success:
        my_output.error('Physical domain create failed: %s' % (error))
        return False

    my_output.default('\t- l3 domain created')
    return True


def configure_aae(handler, fabric, my_output):
    my_output.default('Attachable Access Entity Profile', before_newline=True)
    if not fabric['aaep']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tEnabled')
    policy_name = fabric['aaep']['name']
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (fabric['aaep']['managed']))

    physical_domain_name = None
    if fabric['physical_domain']['enabled']:
        physical_domain_name = fabric['physical_domain']['name']

    l3_domain_name = None
    if fabric['l3_domain']['enabled']:
        l3_domain_name = fabric['l3_domain']['name']

    info = handler.get_policy_global_aae(
        policy_name,
        domain_info=True,
        cache_enabled=False
    )
    if info is not None:
        my_output.default('\t- already defined')

        if physical_domain_name is None:
            my_output.default('\t- skipping aaep to phys domain association check')
        else:
            found = False
            for domain in info['infraRsDomP']:
                if domain['tCl'] == 'physDomP' and domain['domainName'] == physical_domain_name:
                    found = True

            if found:
                my_output.default('\t- association with phys domain [%s] confirmed' % (physical_domain_name))
            else:
                if not fabric['aaep']['managed']:
                    my_output.error('Profile must be associated with phys domain [%s]' % (physical_domain_name))
                    return False

                my_output.default('\t- profile needs associated with phys domain [%s]' % (physical_domain_name))
                success, error = handler.add_policy_global_aae_domain_phy(
                    policy_name,
                    physical_domain_name
                )
                if not success:
                    my_output.error('Profile association with phys domain failed: %s' % (error))
                    return False

        if l3_domain_name is None:
            my_output.default('\t- skipping aaep to l3 domain association check')
        else:
            found = False
            for domain in info['infraRsDomP']:
                if domain['tCl'] == 'l3extDomP' and domain['domainName'] == l3_domain_name:
                    found = True

            if found:
                my_output.default('\t- association with l3 domain [%s] confirmed' % (l3_domain_name))
            else:
                if not fabric['aaep']['managed']:
                    my_output.error('Profile must be associated with l3 domain [%s]' % (l3_domain_name))
                    return False

                my_output.default('\t- profile needs associated with l3 domain [%s]' % (l3_domain_name))
                success, error = handler.add_policy_global_aae_domain_l3(
                    policy_name,
                    l3_domain_name
                )
                if not success:
                    my_output.error('Profile association with l3 domain failed: %s' % (error))
                    return False

        return True

    if not fabric['aaep']['managed']:
        my_output.error('AAEP not found')
        return False

    if physical_domain_name is not None:
        my_output.default('\t- profile will be created and associated with phys domain [%s]' % (physical_domain_name))

        if not handler.is_domain_phy(physical_domain_name, cache_enabled=False):
            my_output.error('Phys domain [%s] not found' % (physical_domain_name))
            return False

    if l3_domain_name is not None:
        my_output.default('\t- profile will be created and associated with l3 domain [%s]' % (l3_domain_name))

        if not handler.is_domain_l3(l3_domain_name, cache_enabled=False):
            my_output.error('L3 domain [%s] not found' % (l3_domain_name))
            return False

    success, error = handler.create_policy_global_aae(
        policy_name,
        phys=physical_domain_name,
        l3=l3_domain_name,
        wait=True
    )
    if not success:
        my_output.error('Profile create failed: %s' % (error))
        return False

    my_output.default('\t- profile created')
    return True


def configure_policy_group_vpc(handler, fabric, policy_name, managed, my_output):
    my_output.default('Policy Group VPC', before_newline=True)
    my_output.default('\tName [%s]' % (policy_name))

    info = handler.get_policy_group_access_interface_vpc(
        policy_name,
        cache_enabled=False
    )
    if info is not None:
        my_output.default('\t- already defined')
        return True

    if not managed:
        my_output.error('Policy group not found')
        return False

    my_output.default('\t- policy group will be created')

    aaep_name = fabric['aaep']['name']
    if not handler.is_policy_global_aae(aaep_name, cache_enabled=False):
        my_output.error('AAEP [%s] not found' % (aaep_name))
        return False

    pc_policy_name = None
    if fabric['port_channel']['enabled']:
        pc_policy_name = fabric['port_channel']['name']
        if not handler.is_policy_interface_port_channel(pc_policy_name, cache_enabled=False):
            my_output.error('Port channel interface policy not found: %s' % (pc_policy_name))
            return False

        my_output.default('\t- Port channel interface policy [%s] found' % (pc_policy_name))

    cdp_policy_name = None
    if fabric['cdp'] is not None:
        cdp_policy_name = fabric['cdp']['name']
        if not handler.is_policy_interface_cdp(cdp_policy_name, cache_enabled=False):
            my_output.error('CDP interface policy not found: %s' % (cdp_policy_name))
            return False

        my_output.default('\t- CDP interface policy [%s] found' % (cdp_policy_name))

    lldp_policy_name = None
    if fabric['lldp'] is not None:
        lldp_policy_name = fabric['lldp']['name']
        if not handler.is_policy_interface_lldp(lldp_policy_name, cache_enabled=False):
            my_output.error('LLDP interface policy not found: %s' % (lldp_policy_name))
            return False

        my_output.default('\t- LLDP interface policy [%s] found' % (lldp_policy_name))

    link_level_policy_name = None
    if fabric['link_level'] is not None:
        link_level_policy_name = fabric['link_level']['name']
        if not handler.is_policy_interface_link_level(link_level_policy_name, cache_enabled=False):
            my_output.error('Link level interface policy not found: %s' % (link_level_policy_name))
            return False

        my_output.default('\t- Link level interface policy [%s] found' % (link_level_policy_name))

    l2_policy_name = None
    if fabric['l2'] is not None:
        l2_policy_name = fabric['l2']['name']
        if not handler.is_policy_interface_l2(l2_policy_name, cache_enabled=False):
            my_output.error('Layer2 interface policy not found: %s' % (l2_policy_name))
            return False

        my_output.default('\t- Layer2 interface policy [%s] found' % (l2_policy_name))

    success, error = handler.create_policy_group_access_interface_vpc(
        policy_name,
        aaep=aaep_name,
        port_channel=pc_policy_name,
        cdp=cdp_policy_name,
        lldp=lldp_policy_name,
        l2=l2_policy_name,
        link_level=link_level_policy_name,
        wait=True
    )
    if not success:
        my_output.error('Policy group create failed: %s' % (error))
        return False

    my_output.default('\t- policy group created')
    return True


def configure_policy_group(handler, fabric, servers, my_output):
    my_output.default('Policy Group', before_newline=True)
    if not fabric['policy_group']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tEnabled')
    policy_name = fabric['policy_group']['name']
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (fabric['policy_group']['managed']))

    if fabric['policy_group']['type'] not in ['vpc']:
        my_output.error('Unsupported policy group type: %s' % (fabric['policy_group']['type']))
        return False

    if fabric['policy_group']['type'] == 'vpc':
        if len(servers) == 1:
            success = configure_policy_group_vpc(
                handler,
                fabric,
                fabric['policy_group']['name'],
                fabric['physical_domain']['managed'],
                my_output
            )

        if len(servers) > 1:
            index = 1
            success = True
            for server in servers:
                success = success and configure_policy_group_vpc(
                    handler,
                    fabric,
                    '%s-%s' % (fabric['policy_group']['name'], index),
                    fabric['physical_domain']['managed'],
                    my_output
                )
                index += 1

    return success


def configure_access_policy_server(handler, policy_name, server, my_output):
    my_output.default('Policy Group on access interface [%s]' % (server['hostname']), before_newline=True)

    my_output.default('\tPolicy [%s]' % (policy_name))

    is_configured = True
    info = handler.get_configuration_vpc(
        policy_name,
        cache_enabled=False
    )
    if info is None:
        my_output.default('\t- not configured on any interface')
        is_configured = False

    if is_configured:
        for interface in info['interfaces']:
            my_output.default('\t- pod [%s] node [%s] interface [%s]' % (
                interface['pod'],
                interface['node'],
                interface['interfaceId']
            ))
        my_output.default('\t- already defined')
        return True

    for interface in server['interface']:
        my_output.default(
            '\tChecking interface pod [%s] node [%s] interface [%s]' % (
                interface['pod'],
                interface['node'],
                interface['port']
            )
        )

        configurations = handler.get_configuration_interface(
            interface['pod'],
            interface['node'],
            interface['port'],
            cache_enabled=False
        )

        if configurations is None:
            my_output.error('Check failed')
            return False

        if len(configurations) == 0:
            my_output.default('\t- no configuration')
        else:
            for configuration in configurations:
                my_output.default(
                    '\t- mode [%s] policy [%s]' % (
                        configuration['mode'],
                        configuration['policyName']
                    )
                )

            my_output.error('Unexpected configuration on an interface')
            return False

        success, error = handler.create_leaf_interface_configuration_vpc(
            policy_name,
            interface['node'],
            interface['port']
        )
        if not success:
            my_output.error('REST API failed: %s' % (error))
            return False

        if success:
            my_output.default('\t- policy [%s] configured on interface' % (policy_name))

    return True


def configure_access_policy(handler, fabric, servers, my_output):
    if len(servers) == 1:
        success = configure_access_policy_server(
            handler,
            fabric['policy_group']['name'],
            servers[0],
            my_output
        )
    else:
        index = 1
        success = True
        for server in servers:
            success = success and configure_access_policy_server(
                handler,
                '%s-%s' % (fabric['policy_group']['name'], index),
                server,
                my_output
            )
            index += 1

    return success


def configure_bd(handler, fabric, my_output):
    my_output.default('Bridge Domain', before_newline=True)
    if not fabric['bd']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tEnabled')
    tenant_name = fabric['tenant']
    bd_name = fabric['bd']['name']
    my_output.default('\tName [%s/%s]' % (tenant_name, bd_name))
    my_output.default('\tManaged mode [%s]' % (fabric['bd']['managed']))

    info = handler.get_bridge_domain(
        tenant_name,
        bd_name,
        cache_enabled=False
    )
    if info is not None:
        my_output.default('\t- already defined')
        return True

    if not fabric['bd']['managed']:
        my_output.error('Bridge domain not found')
        return False

    my_output.default('\t- bridge domain will be created')

    success, error = handler.create_bridge_domain(
        tenant_name,
        bd_name,
        fabric['bd']['gateway'],
        fabric['vrf'],
        fabric['l3out']
    )
    if not success:
        my_output.error('Bridge domain create failed: %s' % (error))
        return False

    my_output.default('\t- bridge domain created')
    return True


def configure_ap(handler, fabric, my_output):
    my_output.default('Application Profile', before_newline=True)
    if not fabric['ap']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tEnabled')
    tenant_name = fabric['tenant']
    ap_name = fabric['ap']['name']
    my_output.default('\tName [%s/%s]' % (tenant_name, ap_name))
    my_output.default('\tManaged mode [%s]' % (fabric['ap']['managed']))

    info = handler.get_application_profile(
        ap_name,
        tenant_name=tenant_name,
        cache_enabled=False
    )
    if info is not None:
        my_output.default('\t- already defined')
        return True

    if not fabric['ap']['managed']:
        my_output.error('Application profile not found')
        return False

    my_output.default('\t- application profile will be created')

    success, error = handler.create_application_profile(
        tenant_name,
        ap_name
    )
    if not success:
        my_output.error('Application profile create failed: %s' % (error))
        return False

    my_output.default('\t- application profile created')
    return True


def configure_epg(handler, fabric, servers, my_output):
    my_output.default('EPG', before_newline=True)
    if not fabric['epg']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tEnabled')
    my_output.default('\tName [%s]' % (fabric['epg']['name']))
    my_output.default('\tManaged mode [%s]' % (fabric['ap']['managed']))

    (epg_tenant, epg_ap, epg_name) = fabric['epg']['name'].split('/')
    if not fabric['bd']['enabled']:
        my_output.error('Cannot create EPG without bridge domain association')
        return False

    bd_name = fabric['bd']['name']

    info = handler.get_epg(
        epg_tenant,
        epg_ap,
        epg_name,
        cache_enabled=False
    )
    if info is not None:
        my_output.default('\t- already defined')

    if info is None:
        if not fabric['epg']['managed']:
            my_output.error('EPG not found')
            return False

        my_output.default('\t- epg will be created')

        success, error = handler.create_epg(
            epg_tenant,
            epg_ap,
            epg_name,
            bd_name,
            wait=True
        )
        if not success:
            my_output.error('EPG create failed: %s' % (error))
            return False

        my_output.default('\t- epg created with bd [%s] association' % (bd_name))

    info = handler.get_epg(
        epg_tenant,
        epg_ap,
        epg_name,
        cache_enabled=False
    )

    if fabric['physical_domain']['enabled']:
        physical_domain_name = fabric['physical_domain']['name']
        found = False
        for domain in info['domain']:
            if domain['type'] == 'physDomP':
                if domain['name'] == physical_domain_name:
                    found = True

        if found:
            my_output.default('\t- epg already associated with phys domain [%s]' % (physical_domain_name))
        else:
            if not fabric['epg']['managed']:
                my_output.error('EPG association with phys domain [%s] must be configured' % (physical_domain_name))
                return False

            my_output.default('\t- epg association with phys domain [%s] must be configured' % (physical_domain_name))
            success, error = handler.add_epg_phys_domain(
                epg_tenant,
                epg_ap,
                epg_name,
                physical_domain_name
            )
            if not success:
                my_output.error('EPG phys domain association failed: %s' % (error))
                return False

            my_output.default('\t- epg associated with phys domain [%s]' % (physical_domain_name))

    if not fabric['epg']['managed']:
        my_output.error('EPG static ports must be configured')
        return False

    if len(servers) == 1:
        policy_name = fabric['policy_group']['name']
        configuration_info = handler.get_configuration_vpc(
            policy_name,
            cache_enabled=False
        )
        if configuration_info is None:
            my_output.error('Unexpected failure in getting configuration details: %s' % (policy_name))
            return False

        found = False
        for static_port in info['staticPort']:
            if static_port['tDn'] == configuration_info['pcPortDn']:
                found = True

        if found:
            my_output.default('\t- epg already has static port with policy [%s]' % (policy_name))
        else:
            my_output.default('\t- epg static port with policy [%s] must be configured' % (policy_name))
            success, error = handler.add_epg_static_port(
                epg_tenant,
                epg_ap,
                epg_name,
                configuration_info['pcPortDn'],
                fabric['policy_group']['encap'],
                fabric['policy_group']['immediacy']
            )
            if not success:
                my_output.error('EPG static port configuration failed: %s' % (error))
                return False

            my_output.default('\t- static port added [%s] [%s] [%s]' % (configuration_info['pcPortDn'], fabric['policy_group']['encap'], fabric['policy_group']['immediacy']))

    if len(servers) > 1:
        index = 1
        for server in servers:
            policy_name = '%s-%s' % (fabric['policy_group']['name'], index)
            index += 1

            configuration_info = handler.get_configuration_vpc(
                policy_name,
                cache_enabled=False
            )
            if configuration_info is None:
                my_output.error('Unexpected failure in getting configuration details: %s' % (policy_name))
                return False

            found = False
            for static_port in info['staticPort']:
                if static_port['tDn'] == configuration_info['pcPortDn']:
                    found = True

            if found:
                my_output.default('\t- epg already has static port with policy [%s]' % (policy_name))
            else:
                my_output.default('\t- epg static port with policy [%s] must be configured' % (policy_name))
                success, error = handler.add_epg_static_port(
                    epg_tenant,
                    epg_ap,
                    epg_name,
                    configuration_info['pcPortDn'],
                    fabric['policy_group']['encap'],
                    fabric['policy_group']['immediacy']
                )
                if not success:
                    my_output.error('EPG static port configuration failed: %s' % (error))
                    return False

                my_output.default('\t- static port added [%s] [%s] [%s]' % (configuration_info['pcPortDn'], fabric['policy_group']['encap'], fabric['policy_group']['immediacy']))

    return True


def configure_policy_cdp(handler, fabric, my_output):
    my_output.default('Policy CDP', before_newline=True)
    if not fabric['cdp']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tEnabled')
    policy_name = fabric['cdp']['name']
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (fabric['cdp']['managed']))

    info = handler.get_policy_interface_cdp(
        policy_name,
        cache_enabled=False
    )
    if info is not None:
        my_output.default('\t- already defined')
        return True

    if not fabric['cdp']['managed']:
        my_output.error('Policy cdp not found')
        return False

    my_output.default('\t- policy cdp will be created')
    my_output.default('\t- cdp enabled [%s]' % (fabric['cdp']['cdp_enabled']))

    success, error = handler.create_policy_interface_cdp(
        policy_name,
        fabric['cdp']['cdp_enabled']
    )
    if not success:
        my_output.error('Policy cdp create failed: %s' % (error))
        return False

    my_output.default('\t- policy cdp created')
    return True


def configure_policy_lldp(handler, fabric, my_output):
    my_output.default('Policy LLDP', before_newline=True)
    if not fabric['lldp']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tEnabled')
    policy_name = fabric['lldp']['name']
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (fabric['lldp']['managed']))

    info = handler.get_policy_interface_lldp(
        policy_name,
        cache_enabled=False
    )
    if info is not None:
        my_output.default('\t- already defined')
        return True

    if not fabric['lldp']['managed']:
        my_output.error('Policy lldp not found')
        return False

    my_output.default('\t- policy lldp will be created')
    my_output.default('\t- lldp receive enabled [%s]' % (fabric['lldp']['lldp_receive']))
    my_output.default('\t- lldp transmit enabled [%s]' % (fabric['lldp']['lldp_transmit']))

    success, error = handler.create_policy_interface_lldp(
        policy_name,
        fabric['lldp']['lldp_receive'],
        fabric['lldp']['lldp_transmit']
    )
    if not success:
        my_output.error('Policy lldp create failed: %s' % (error))
        return False

    my_output.default('\t- policy lldp created')
    return True


def configure_policy_l2(handler, fabric, my_output):
    my_output.default('Policy L2', before_newline=True)
    if not fabric['l2']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tEnabled')
    policy_name = fabric['l2']['name']
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (fabric['l2']['managed']))

    info = handler.get_policy_interface_l2(
        policy_name,
        cache_enabled=False
    )
    if info is not None:
        my_output.default('\t- already defined')
        return True

    if not fabric['l2']['managed']:
        my_output.error('Policy l2 not found')
        return False

    my_output.default('\t- policy l2 will be created')
    my_output.default('\t- qinq [%s]' % (fabric['l2']['qinq']))
    my_output.default('\t- relay [%s]' % (fabric['l2']['relay']))
    my_output.default('\t- vlan [%s]' % (fabric['l2']['vlan']))

    success, error = handler.create_policy_interface_l2(
        policy_name,
        fabric['l2']['qinq'],
        fabric['l2']['relay'],
        fabric['l2']['vlan']
    )
    if not success:
        my_output.error('Policy l2 create failed: %s' % (error))
        return False

    my_output.default('\t- policy l2 created')
    return True


def configure_policy_link_level(handler, fabric, my_output):
    my_output.default('Policy Link Level', before_newline=True)
    if not fabric['link_level']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tEnabled')
    policy_name = fabric['link_level']['name']
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (fabric['link_level']['managed']))

    info = handler.get_policy_interface_link_level(
        policy_name,
        cache_enabled=False
    )
    if info is not None:
        my_output.default('\t- already defined')
        return True

    if not fabric['link_level']['managed']:
        my_output.error('Policy link level not found')
        return False

    my_output.default('\t- policy link level will be created')
    my_output.default('\t- auto [%s]' % (fabric['link_level']['auto']))
    my_output.default('\t- media [%s]' % (fabric['link_level']['media']))
    my_output.default('\t- debounce [%s]' % (fabric['link_level']['debounce']))
    my_output.default('\t- delay [%s]' % (fabric['link_level']['delay']))
    my_output.default('\t- emi [%s]' % (fabric['link_level']['emi']))

    success, error = handler.create_policy_interface_link_level(
        policy_name,
        fabric['link_level']['auto'],
        fabric['link_level']['media'],
        fabric['link_level']['debounce'],
        fabric['link_level']['delay'],
        fabric['link_level']['emi']
    )
    if not success:
        my_output.error('Policy link level create failed: %s' % (error))
        return False

    my_output.default('\t- policy link level created')
    return True


def configure_policy_port_channel(handler, fabric, my_output):
    my_output.default('Policy Port Channel', before_newline=True)
    if not fabric['port_channel']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tEnabled')
    policy_name = fabric['port_channel']['name']
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (fabric['port_channel']['managed']))

    info = handler.get_policy_interface_port_channel(
        policy_name,
        cache_enabled=False
    )
    if info is not None:
        my_output.default('\t- already defined')
        return True

    if not fabric['port_channel']['managed']:
        my_output.error('Policy port channel not found')
        return False

    my_output.default('\t- policy port channel will be created')
    my_output.default('\t- mode [%s]' % (fabric['port_channel']['mode']))
    my_output.default('\t- min [%s]' % (fabric['port_channel']['min']))
    my_output.default('\t- max [%s]' % (fabric['port_channel']['max']))
    my_output.default('\t- lb [%s]' % (fabric['port_channel']['lb']))
    my_output.default('\t- suspend [%s]' % (fabric['port_channel']['suspend']))
    my_output.default('\t- graceful [%s]' % (fabric['port_channel']['graceful']))
    my_output.default('\t- symmetric [%s]' % (fabric['port_channel']['symmetric']))
    my_output.default('\t- fast [%s]' % (fabric['port_channel']['fast']))
    my_output.default('\t- hash [%s]' % (fabric['port_channel']['hash']))

    success, error = handler.create_policy_interface_port_channel(
        policy_name,
        fabric['port_channel']['mode'],
        fabric['port_channel']['min'],
        fabric['port_channel']['max'],
        fabric['port_channel']['lb'],
        fabric['port_channel']['suspend'],
        fabric['port_channel']['graceful'],
        fabric['port_channel']['symmetric'],
        fabric['port_channel']['fast'],
        fabric['port_channel']['hash']
    )
    if not success:
        my_output.error('Policy port channel create failed: %s' % (error))
        return False

    my_output.default('\t- policy port channel created')
    return True


def configure_bgp(handler, fabric, server, my_output, log_handler):
    my_output.default('BGP', before_newline=True)
    if not fabric['bgp']['enabled']:
        my_output.default('\tDisabled')
        return True

    if handler.is_l3out(fabric['tenant'], fabric['bgp']['l3out']['name'], cache_enabled=False):
        my_output.default('\t- already defined')
    else:
        my_output.default('\t- l3out will be created')

        body = bgp.get_body(handler, fabric, server, my_output)
        if body is None:
            return False

        log_handler.debug(
            'configure_bgp.l3out',
            json.dumps(body, indent=4)
        )
        success, error = handler.create_l3out(
            fabric['tenant'],
            fabric['bgp']['l3out']['name'],
            body,
            wait=False
        )
        if not success:
            my_output.error('L3Out create failed: %s' % (error))
            my_output.default(json.dumps(body, indent=4))
            return False

        my_output.default('\t- l3out created')

    info = handler.get_l3out(
        fabric['l3out_tenant'],
        fabric['l3out'],
        cache_enabled=False
    )
    if info is None:
        my_output.error('Main L3Out not found: %s/%s' % (fabric['l3out_tenant'], fabric['l3out']))
        return False

    subnet = ip_helper.get_network_cidr_from_cidr(fabric['bgp']['gateway'])
    exists = handler.is_l3out_external_epg_subnet(
        fabric['l3out_tenant'],
        fabric['l3out'],
        fabric['external_epg'],
        subnet,
        cache_enabled=False
    )
    if exists:
        my_output.default('\t- l3out external epg subnet already defined [%s]' % (subnet))
    else:
        success, error = handler.add_l3out_external_epg_subnet(
            fabric['l3out_tenant'],
            fabric['l3out'],
            fabric['external_epg'],
            subnet,
            fabric['mo_name'],
            'export-rtctrl'
        )
        if not success:
            my_output.error('L3Out external epg update failed: %s' % (error))
            return False

        my_output.default('\t- l3out external epg updated')

    return True


def run(fabric, servers, my_output, log_id):
    log_handler = log_helper.Log(log_id=log_id)
    my_output.default('\nApic [%s] domain [%s] configuration' % (fabric['apic'], fabric['domain']), underline=True)

    handler = common.get_handler('aci', fabric['apic'], my_output, log_id)
    if handler is None:
        return False

    fabric, domain_servers = check.validate(handler, fabric, servers, my_output)
    if fabric is None:
        return False

    my_output.default('Validated and resolved fabric configuration intent', before_newline=True)
    my_output.default(json.dumps(fabric, indent=4))
    my_output.default('Validated and resolved servers connectivity layout', before_newline=True)
    my_output.default(json.dumps(servers, indent=4))

    if not configure_vlan_pool(handler, fabric, my_output):
        return False

    if not configure_physical_domain(handler, fabric, my_output):
        return False

    if not configure_l3_domain(handler, fabric, my_output):
        return False

    if not configure_aae(handler, fabric, my_output):
        return False

    if not configure_policy_cdp(handler, fabric, my_output):
        return False

    if not configure_policy_lldp(handler, fabric, my_output):
        return False

    if not configure_policy_link_level(handler, fabric, my_output):
        return False

    if not configure_policy_l2(handler, fabric, my_output):
        return False

    if not configure_policy_port_channel(handler, fabric, my_output):
        return False

    if not configure_policy_group(handler, fabric, domain_servers, my_output):
        return False

    if not configure_access_policy(handler, fabric, domain_servers, my_output):
        return False

    if fabric['bgp']['enabled']:
        if not configure_bgp(handler, fabric, domain_servers, my_output, log_handler):
            return False

    if not fabric['bgp']['enabled']:
        if not configure_bd(handler, fabric, my_output):
            return False

        if not configure_ap(handler, fabric, my_output):
            return False

        if not configure_epg(handler, fabric, domain_servers, my_output):
            return False

    return True
