import json
from lib import ip_helper
from lib.workflow.ocp_fabric.aci import check
from lib.workflow.ocp_fabric import common


def unconfigure_epg(handler, fabric, my_output):
    my_output.default('EPG', before_newline=True)
    if not fabric['epg']['enabled']:
        my_output.default('\tDisabled')
        return True

    my_output.default('\tName [%s]' % (fabric['epg']['name']))
    my_output.default('\tManaged mode [%s]' % (fabric['epg']['managed']))
    if not fabric['epg']['managed']:
        return True
    my_output.default('\tShared mode [%s]' % (fabric['epg']['shared']))

    (epg_tenant, epg_ap, epg_name) = fabric['epg']['name'].split('/')
    info = handler.get_epg(
        epg_tenant,
        epg_ap,
        epg_name,
        cache_enabled=False
    )

    if info is None:
        my_output.default('\t- already deleted')
        return True

    my_output.default('\t- checking domain associations')
    for domain in info['domain']:
        if domain['type'] not in ['physDomP']:
            my_output.error('Unsupported EPG domain association: %s' % (domain['type']))
            return False

        if domain['type'] == 'physDomP':
            success, error = handler.delete_epg_phys_domain(
                epg_tenant,
                epg_ap,
                epg_name,
                domain['name']
            )
            if not success:
                my_output.error('EPG phys domain delete failed: %s' % (error))
                return False

            my_output.default('\t- phys domain association deleted: %s' % (domain['name']))

    my_output.default('\t- checking static ports')
    for static_port in info['staticPort']:
        success, error = handler.delete_epg_static_port(
            epg_tenant,
            epg_ap,
            epg_name,
            static_port['tDn']
        )
        if not success:
            my_output.error('EPG static port delete failed: %s' % (error))
            return False

        my_output.default('\t- static port deleted: %s' % (static_port['tDn']))

    success, error = handler.delete_epg(
        epg_tenant,
        epg_ap,
        epg_name,
        wait=True
    )
    if not success:
        my_output.error('EPG delete failed: %s' % (error))
        return False

    my_output.default('\t- EPG deleted')
    return True


def unconfigure_ap(handler, fabric, my_output):
    my_output.default('Application Profile', before_newline=True)
    if not fabric['ap']['enabled']:
        my_output.default('\tDisabled')
        return True

    ap_tenant = fabric['tenant']
    ap_name = fabric['ap']['name']
    my_output.default('\tName [%s/%s]' % (ap_tenant, ap_name))
    my_output.default('\tManaged mode [%s]' % (fabric['ap']['managed']))
    if not fabric['ap']['managed']:
        return True
    my_output.default('\tShared mode [%s]' % (fabric['ap']['shared']))

    info = handler.get_application_profile(
        ap_name,
        tenant_name=ap_tenant,
        epg_info=True,
        cache_enabled=False
    )

    if info is None:
        my_output.default('\t- already deleted')
        return True

    my_output.default('\t- check association epgs')
    if len(info['epgs']) > 0:
        my_output.error('Application profile still has EPGs')
        if fabric['ap']['shared']:
            return True
        return False

    success, error = handler.delete_application_profile(
        ap_tenant,
        ap_name
    )
    if not success:
        my_output.error('Application profile delete failed: %s' % (error))
        return False

    my_output.default('\t- application profile deleted')
    return True


def unconfigure_bd(handler, fabric, my_output):
    my_output.default('Bridge Domain', before_newline=True)
    if not fabric['bd']['enabled']:
        my_output.default('\tDisabled')
        return True

    bd_tenant = fabric['tenant']
    bd_name = fabric['bd']['name']
    my_output.default('\tName [%s/%s]' % (bd_tenant, bd_name))
    my_output.default('\tManaged mode [%s]' % (fabric['bd']['managed']))
    if not fabric['bd']['managed']:
        return True
    my_output.default('\tShared mode [%s]' % (fabric['bd']['shared']))

    info = handler.get_bridge_domain(
        bd_tenant,
        bd_name,
        epg_info=True,
        cache_enabled=False
    )

    if info is None:
        my_output.default('\t- already deleted')
        return True

    my_output.default('\t- check epg associations')
    if len(info['fvAEPg']) > 0:
        my_output.error('EPG associated with bridge domain')
        if fabric['bd']['shared']:
            return True
        return False

    success, error = handler.delete_bridge_domain(
        bd_tenant,
        bd_name
    )
    if not success:
        my_output.error('Bridge domain delete failed: %s' % (error))
        return False

    my_output.default('\t- bridge domain deleted')
    return True


def unconfigure_vlan_pool(handler, fabric, my_output):
    my_output.default('VLAN Pool', before_newline=True)
    if not fabric['vlan_pool']['enabled']:
        my_output.default('\tDisabled')
        return True

    pool_name = fabric['vlan_pool']['name']
    my_output.default('\tName [%s]' % (pool_name))
    my_output.default('\tManaged mode [%s]' % (fabric['vlan_pool']['managed']))
    if not fabric['vlan_pool']['managed']:
        return True
    my_output.default('\tShared mode [%s]' % (fabric['vlan_pool']['shared']))

    info = handler.get_pool_vlan(
        pool_name,
        cache_enabled=False
    )
    if info is None:
        my_output.default('\t- already deleted')
        return True

    my_output.default('\t- check vlan pool details with relationships')
    info = handler.get_pool_vlan(
        pool_name,
        cache_enabled=False
    )

    for key in ['VlanNsToInterface', 'VlanNsToVirtualMachines', 'VlanNsToVmmPortGroups', 'fvnsRtVlanNs']:
        if info[key] is None or len(info[key]) == 0:
            my_output.default('\t\t %s' % (key))
        else:
            my_output.error('VLAN pool relationship [%s] found: %s' % (key, info[key]))
            if fabric['vlan_pool']['shared']:
                return True
            return False

    success, error = handler.delete_pool_vlan(
        pool_name,
        info['allocMode']
    )
    if not success:
        my_output.error('VLAN pool delete failed: %s' % (error))
        return False

    my_output.default('\t- VLAN pool deleted')
    return True


def unconfigure_physical_domain(handler, fabric, my_output):
    my_output.default('Physical Domain', before_newline=True)
    if not fabric['physical_domain']['enabled']:
        my_output.default('\tDisabled')
        return True

    domain_name = fabric['physical_domain']['name']
    my_output.default('\tName [%s]' % (domain_name))
    my_output.default('\tManaged mode [%s]' % (fabric['physical_domain']['managed']))
    if not fabric['physical_domain']['managed']:
        return True
    my_output.default('\tShared mode [%s]' % (fabric['physical_domain']['shared']))

    info = handler.get_domain_phy(
        domain_name,
        vlan_info=True,
        cache_enabled=False
    )
    if info is None:
        my_output.default('\t- already deleted')
        return True

    my_output.default('\t- checking vlan pool association')
    if info['vlan_info'] is not None:
        my_output.default('\t- VLAN Pool association [%s]' % (info['vlan_info']['name']))
        if info['vlan_info']['name'] != fabric['vlan_pool']['name']:
            my_output.error('Unexpected vlan pool association: [%s] vs [%s]' % (info['vlan_info']['name'], fabric['vlan_pool']['name']))
            return False

        my_output.default('\t- delete vlan pool association')
        success, error = handler.delete_domain_phy_vlan_pool(domain_name)
        if not success:
            my_output.error('Delete vlan pool association failed: %s' % (error))
            return False

    success, error = handler.delete_domain_phy(domain_name)
    if not success:
        my_output.error('Phy domain delete failed: %s' % (error))
        return False

    my_output.default('\t- phys domain deleted')
    return True


def unconfigure_l3_domain(handler, fabric, my_output):
    my_output.default('L3 Domain', before_newline=True)
    if not fabric['l3_domain']['enabled']:
        my_output.default('\tDisabled')
        return True

    domain_name = fabric['l3_domain']['name']
    my_output.default('\tName [%s]' % (domain_name))
    my_output.default('\tManaged mode [%s]' % (fabric['l3_domain']['managed']))
    if not fabric['l3_domain']['managed']:
        return True
    my_output.default('\tShared mode [%s]' % (fabric['l3_domain']['shared']))

    info = handler.get_domain_l3(
        domain_name,
        vlan_info=True,
        cache_enabled=False
    )
    if info is None:
        my_output.default('\t- already deleted')
        return True

    my_output.default('\t- checking vlan pool association')
    if info['vlan_info'] is not None:
        my_output.default('\t- VLAN Pool association [%s]' % (info['vlan_info']['name']))
        if info['vlan_info']['name'] != fabric['vlan_pool']['name']:
            my_output.error('Unexpected vlan pool association: [%s] vs [%s]' % (info['vlan_info']['name'], fabric['vlan_pool']['name']))
            return False

        my_output.default('\t- delete vlan pool association')
        success, error = handler.delete_domain_l3_vlan_pool(domain_name)
        if not success:
            my_output.error('Delete vlan pool association failed: %s' % (error))
            return False

    success, error = handler.delete_domain_l3(domain_name)
    if not success:
        my_output.error('L3 domain delete failed: %s' % (error))
        return False

    my_output.default('\t- l3 domain deleted')
    return True


def unconfigure_aae(handler, fabric, my_output):
    my_output.default('Attachable Access Entity Profile', before_newline=True)
    if not fabric['aaep']['enabled']:
        my_output.default('\tDisabled')
        return True

    policy_name = fabric['aaep']['name']
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (fabric['aaep']['managed']))
    if not fabric['aaep']['managed']:
        return True
    my_output.default('\tShared mode [%s]' % (fabric['aaep']['shared']))

    info = handler.get_policy_global_aae(
        policy_name,
        domain_info=True,
        cache_enabled=False
    )

    if info is None:
        my_output.default('\t- already deleted')
        return True

    if len(info['infraRsDomP']) == 0:
        my_output.default('\t- no domain association found')

    if len(info['infraRsDomP']) > 0:
        my_output.default('\t- domain associations found')
        for item in info['infraRsDomP']:
            my_output.default('\t\t %s [%s]' % (item['domainName'], item['domainType']))
            if item['tCl'] not in ['physDomP', 'l3extDomP']:
                my_output.error('Unsupported domain type: %s' % (item['tCl']))
                if fabric['aaep']['shared']:
                    continue

                return False

            if item['tCl'] == 'physDomP':
                if fabric['physical_domain']['name'] != item['domainName']:
                    my_output.error('Unexpected phys domain association: [%s] vs [%s]' % (info['physical_domain']['name'], item['domainName']))
                    if fabric['aaep']['shared']:
                        continue

                    return False

                success, error = handler.delete_policy_global_aae_domain_phy(
                    policy_name,
                    item['domainName']
                )
                if not success:
                    my_output.error('AAEP domain delete failed: %s' % (error))
                    return False

                my_output.default('\t\t- AAEP to phys domain [%s] association deleted' % (item['domainName']))

            if item['tCl'] == 'l3extDomP':
                if not fabric['l3_domain']['enabled']:
                    my_output.error('Unexpected l3 domain association: [%s]' % (item['domainName']))
                    if fabric['aaep']['shared']:
                        continue

                    return False
                
                if fabric['l3_domain']['name'] != item['domainName']:
                    my_output.error('Unexpected l3 domain association: [%s] vs [%s]' % (info['phyl3_domainsical_domain']['name'], item['domainName']))
                    if fabric['aaep']['shared']:
                        continue

                    return False

                success, error = handler.delete_policy_global_aae_domain_l3(
                    policy_name,
                    item['domainName']
                )
                if not success:
                    my_output.error('AAEP domain delete failed: %s' % (error))
                    return False

                my_output.default('\t\t- AAEP to l3 domain [%s] association deleted' % (item['domainName']))

    my_output.default('\t- checking relations')
    info = handler.get_policy_global_aae(
        policy_name,
        domain_info=True,
        cache_enabled=False
    )

    if len(info['infraRsDomP']) > 0:
        if fabric['aaep']['shared']:
            my_output.default('Domain associations exist')
            return True

        my_output.error('Unexpected domain associations')
        return False

    if len(info['infraRsFuncToEpg']) > 0:
        if fabric['aaep']['shared']:
            my_output.default('EPG associations exist')
            return True

        my_output.error('Unexpected epg associations')
        return False

    my_output.default('\t- no relations found')

    success, error = handler.delete_policy_global_aae(
        policy_name
    )
    if not success:
        my_output.error('Delete failed: %s' % (error))
        return False

    my_output.default('\t- aaep deleted')
    return True


def unconfigure_policy_group_vpc(handler, policy_name, managed, shared, my_output):
    my_output.default('Policy Group', before_newline=True)
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (managed))
    if not managed:
        return True
    my_output.default('\tShared mode [%s]' % (shared))

    info = handler.get_policy_group_access_interface_vpc(
        policy_name,
        node_info=True,
        cache_enabled=False
    )
    if info is None:
        my_output.default('\t- already deleted')
        return True

    if len(info['node']) > 0:
        my_output.error('Policy group configured on node: %s' % (info['node']))
        if shared:
            return True
        return False

    if len(info['interface']) > 0:
        my_output.error('Policy group configured on interface: %s' % (info['interface']))
        if shared:
            return True
        return False

    my_output.default('\t- policy group not configured on any node/interface and can be deleted')

    success, error = handler.delete_policy_group_access_interface_vpc(policy_name)
    if not success:
        my_output.error('Policy Group delete failed: %s' % (error))
        return False

    my_output.default('\t- policy group deleted')
    return True


def unconfigure_policy_group(handler, fabric, domain_servers, my_output):
    if fabric['policy_group']['type'] not in ['vpc']:
        my_output.default('Policy Group', before_newline=True)
        my_output.error('Unsupported policy group type: %s' % (fabric['policy_group']['type']))
        return False

    success = True

    if fabric['policy_group']['type'] == 'vpc':
        if len(domain_servers) == 1:
            success = unconfigure_policy_group_vpc(
                handler,
                fabric['policy_group']['name'],
                fabric['policy_group']['managed'],
                fabric['policy_group']['shared'],
                my_output
            )

        if len(domain_servers) > 1:
            index = 1
            success = True
            for server in domain_servers:
                success = success and unconfigure_policy_group_vpc(
                    handler,
                    '%s-%s' % (fabric['policy_group']['name'], index),
                    fabric['policy_group']['managed'],
                    fabric['policy_group']['shared'],
                    my_output
                )
                index += 1

    return success


def unconfigure_access_policy_vpc(handler, policy_name, my_output):
    my_output.default('Policy Group', before_newline=True)
    my_output.default('\tName [%s]' % (policy_name))

    info = handler.get_configuration_vpc(
        policy_name,
        cache_enabled=False
    )
    if info is None:
        my_output.default('\t- not configured on any interface')
        return True

    for interface in info['interfaces']:
        my_output.default('\t- pod [%s] node [%s] interface [%s]' % (
            interface['pod'],
            interface['node'],
            interface['interfaceId']
        ))
        success, error = handler.delete_leaf_interface_configuration(interface['node'], interface['interfaceId'])
        if not success:
            my_output.error('Interface configuration delete failed: %s' % (error))
            return False

        my_output.default('\t- configuration deleted')

    return True


def unconfigure_access_policy(handler, fabric, domain_servers, my_output):
    if not fabric['policy_group']['enabled']:
        my_output.default('Policy Group', before_newline=True)
        my_output.default('\tDisabled')
        return True

    if fabric['policy_group']['type'] not in ['vpc']:
        my_output.default('Policy Group', before_newline=True)
        my_output.error('Unsupported policy group type: %s' % (fabric['policy_group']['type']))
        return False

    success = True

    if fabric['policy_group']['type'] == 'vpc':
        if len(domain_servers) == 1:
            success = unconfigure_access_policy_vpc(
                handler,
                fabric['policy_group']['name'],
                my_output
            )

        if len(domain_servers) > 1:
            index = 1
            success = True
            for server in domain_servers:
                success = success and unconfigure_access_policy_vpc(
                    handler,
                    '%s-%s' % (fabric['policy_group']['name'], index),
                    my_output
                )
                index += 1

    return success


def unconfigure_policy_cdp(handler, fabric, my_output):
    if not fabric['cdp']['enabled']:
        my_output.default('Policy CDP', before_newline=True)
        my_output.default('\tDisabled')
        return True

    my_output.default('Policy CDP', before_newline=True)
    policy_name = fabric['cdp']['name']
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (fabric['cdp']['managed']))
    if not fabric['cdp']['managed']:
        return True
    my_output.default('\tShared mode [%s]' % (fabric['cdp']['shared']))

    info = handler.get_policy_interface_cdp(
        policy_name,
        reln_info=True,
        attachment_info=True,
        cache_enabled=False
    )

    if info is None:
        my_output.default('\t- already deleted')
        return True

    references = False

    if len(info['relnFrom']) == 0:
        my_output.default('\t- no policy relations found')
    else:
        references = True
        my_output.default('\t- policy relations')
        for reln in info['relnFrom']:
            my_output.default('\t\t[%s] [%s]' % (reln['policyType'], reln['policyName']))

    if len(info['l1RsCdpIfPolCons']) == 0:
        my_output.default('\t- no interface relations found')
    else:
        references = True
        my_output.default('\t- interface relations')
        for reln in info['l1RsCdpIfPolCons']:
            my_output.default('\t\t[%s] [%s]' % (reln['pod_node_name'], reln['interfaceId']))

    if references:
        if not fabric['cdp']['shared']:
            my_output.error('Unexpected policy usage')
            return False

        my_output.default('Policy not delete due to policy usage (shared mode)')
        return True

    success, error = handler.delete_policy_interface_cdp(
        policy_name
    )
    if not success:
        my_output.error('Policy CDP delete failed: %s' % (error))
        return False

    my_output.default('\t- policy cdp deleted')
    return True


def unconfigure_policy_lldp(handler, fabric, my_output):
    if not fabric['lldp']['enabled']:
        my_output.default('Policy LLDP', before_newline=True)
        my_output.default('\tDisabled')
        return True

    my_output.default('Policy LLDP', before_newline=True)
    policy_name = fabric['lldp']['name']
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (fabric['lldp']['managed']))
    if not fabric['lldp']['managed']:
        return True
    my_output.default('\tShared mode [%s]' % (fabric['lldp']['shared']))

    info = handler.get_policy_interface_lldp(
        policy_name,
        reln_info=True,
        attachment_info=True,
        cache_enabled=False
    )

    if info is None:
        my_output.default('\t- already deleted')
        return True

    references = False

    if len(info['relnFrom']) == 0:
        my_output.default('\t- no policy relations found')
    else:
        references = True
        my_output.default('\t- policy relations')
        for reln in info['relnFrom']:
            my_output.default('\t\t[%s] [%s]' % (reln['policyType'], reln['policyName']))

    if len(info['l1RsLldpIfPolCons']) == 0:
        my_output.default('\t- no interface relations found')
    else:
        references = True
        my_output.default('\t- interface relations')
        for reln in info['l1RsLldpIfPolCons']:
            my_output.default('\t\t[%s] [%s]' % (reln['pod_node_name'], reln['interfaceId']))

    if references:
        if not fabric['lldp']['shared']:
            my_output.error('Unexpected policy usage')
            return False

        my_output.default('Policy not delete due to policy usage (shared mode)')
        return True

    success, error = handler.delete_policy_interface_lldp(
        policy_name
    )
    if not success:
        my_output.error('Policy LLDP delete failed: %s' % (error))
        return False

    my_output.default('\t- policy lldp deleted')
    return True


def unconfigure_policy_link_level(handler, fabric, my_output):
    if not fabric['link_level']['enabled']:
        my_output.default('Policy Link Level', before_newline=True)
        my_output.default('\tDisabled')
        return True

    my_output.default('Policy Link Level', before_newline=True)
    policy_name = fabric['link_level']['name']
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (fabric['link_level']['managed']))
    if not fabric['link_level']['managed']:
        return True
    my_output.default('\tShared mode [%s]' % (fabric['link_level']['shared']))

    info = handler.get_policy_interface_link_level(
        policy_name,
        reln_info=True,
        attachment_info=True,
        cache_enabled=False
    )

    if info is None:
        my_output.default('\t- already deleted')
        return True

    references = False

    if len(info['relnFrom']) == 0:
        my_output.default('\t- no policy relations found')
    else:
        references = True
        my_output.default('\t- policy relations')
        for reln in info['relnFrom']:
            my_output.default('\t\t[%s] [%s]' % (reln['policyType'], reln['policyName']))

    if len(info['l1RsHIfPolCons']) == 0:
        my_output.default('\t- no interface relations found')
    else:
        references = True
        my_output.default('\t- interface relations')
        for reln in info['l1RsHIfPolCons']:
            my_output.default('\t\t[%s] [%s]' % (reln['pod_node_name'], reln['interfaceId']))

    if references:
        if not fabric['link_level']['shared']:
            my_output.error('Unexpected policy usage')
            return False

        my_output.default('Policy not delete due to policy usage (shared mode)')
        return True

    success, error = handler.delete_policy_interface_link_level(
        policy_name
    )
    if not success:
        my_output.error('Policy Link Level delete failed: %s' % (error))
        return False

    my_output.default('\t- policy link_level deleted')
    return True


def unconfigure_policy_l2(handler, fabric, my_output):
    if not fabric['l2']['enabled']:
        my_output.default('Policy L2', before_newline=True)
        my_output.default('\tDisabled')
        return True

    my_output.default('Policy L2', before_newline=True)
    policy_name = fabric['l2']['name']
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (fabric['l2']['managed']))
    if not fabric['l2']['managed']:
        return True
    my_output.default('\tShared mode [%s]' % (fabric['l2']['shared']))

    info = handler.get_policy_interface_l2(
        policy_name,
        reln_info=True,
        attachment_info=True,
        cache_enabled=False
    )

    if info is None:
        my_output.default('\t- already deleted')
        return True

    references = False

    if len(info['relnFrom']) == 0:
        my_output.default('\t- no policy relations found')
    else:
        references = True
        my_output.default('\t- policy relations')
        for reln in info['relnFrom']:
            my_output.default('\t\t[%s] [%s]' % (reln['policyType'], reln['policyName']))

    if len(info['l1RsL2IfPolCons']) == 0:
        my_output.default('\t- no interface relations found')
    else:
        references = True
        my_output.default('\t- interface relations')
        for reln in info['l1RsL2IfPolCons']:
            my_output.default('\t\t[%s] [%s]' % (reln['pod_node_name'], reln['interfaceId']))

    if references:
        if not fabric['l2']['shared']:
            my_output.error('Unexpected policy usage')
            return False

        my_output.default('Policy not delete due to policy usage (shared mode)')
        return True

    success, error = handler.delete_policy_interface_l2(
        policy_name
    )
    if not success:
        my_output.error('Policy L2 delete failed: %s' % (error))
        return False

    my_output.default('\t- policy l2 deleted')
    return True


def unconfigure_policy_port_channel(handler, fabric, my_output):
    if not fabric['port_channel']['enabled']:
        my_output.default('Policy Port Channel', before_newline=True)
        my_output.default('\tDisabled')
        return True

    my_output.default('Policy Port Channel', before_newline=True)
    policy_name = fabric['port_channel']['name']
    my_output.default('\tName [%s]' % (policy_name))
    my_output.default('\tManaged mode [%s]' % (fabric['port_channel']['managed']))
    if not fabric['port_channel']['managed']:
        return True
    my_output.default('\tShared mode [%s]' % (fabric['port_channel']['shared']))

    info = handler.get_policy_interface_port_channel(
        policy_name,
        reln_info=True,
        attachment_info=True,
        cache_enabled=False
    )

    if info is None:
        my_output.default('\t- already deleted')
        return True

    references = False

    if len(info['relnFrom']) == 0:
        my_output.default('\t- no policy relations found')
    else:
        references = True
        my_output.default('\t- policy relations')
        for reln in info['relnFrom']:
            my_output.default('\t\t[%s] [%s]' % (reln['policyType'], reln['policyName']))

    if len(info['l1RsLacpIfPolCons']) == 0:
        my_output.default('\t- no interface relations found')
    else:
        references = True
        my_output.default('\t- interface relations')
        for reln in info['l1RsLacpIfPolCons']:
            my_output.default('\t\t[%s] [%s]' % (reln['pod_node_name'], reln['interfaceId']))

    if references:
        if not fabric['port_channel']['shared']:
            my_output.error('Unexpected policy usage')
            return False

        my_output.default('Policy not delete due to policy usage (shared mode)')
        return True

    success, error = handler.delete_policy_interface_port_channel(
        policy_name
    )
    if not success:
        my_output.error('Policy Port Channel delete failed: %s' % (error))
        return False

    my_output.default('\t- policy port_channel deleted')
    return True


def unconfigure_bgp(handler, fabric, my_output):
    if not fabric['bgp']['enabled']:
        my_output.default('BGP', before_newline=True)
        my_output.default('\tDisabled')
        return True

    my_output.default('BGP', before_newline=True)
    my_output.default('\tManaged mode [%s]' % (fabric['bgp']['managed']))
    if not fabric['bgp']['managed']:
        return True
    my_output.default('\tShared mode [%s]' % (fabric['bgp']['shared']))

    subnet = ip_helper.get_network_cidr_from_cidr(fabric['bgp']['gateway'])
    exists = handler.is_l3out_external_epg_subnet(
        fabric['l3out_tenant'],
        fabric['l3out'],
        fabric['external_epg'],
        subnet,
        cache_enabled=False
    )
    if exists:
        my_output.default('\t- subnet [%s] must be deleted from L3out [%s/%s] external epg [%s]' % (subnet, fabric['l3out_tenant'], fabric['l3out'], fabric['external_epg']))
        success, error = handler.delete_l3out_external_epg_subnet(
            fabric['l3out_tenant'],
            fabric['l3out'],
            fabric['external_epg'],
            subnet
        )
        if not success:
            my_output.error('Subnet delete from l3out external epg failed: %s' % (error))
            return False
        my_output.default('\t- delete successful')

    else:
        my_output.default('\t- subnet [%s] already deleted from L3out [%s/%s] external epg [%s]' % (subnet, fabric['l3out_tenant'], fabric['l3out'], fabric['external_epg']))

    if handler.is_l3out(fabric['tenant'], fabric['bgp']['l3out']['name'], cache_enabled=False):
        my_output.default('\t- l3out [%s/%s] will be deleted' % (fabric['tenant'], fabric['bgp']['l3out']['name']))
        success, error = handler.delete_l3out(
            fabric['tenant'],
            fabric['bgp']['l3out']['name']
        )
        if not success:
            my_output.error('L3out delete failed: %s' % (error))
            return False
        my_output.default('\t- delete successful')
    else:
        my_output.default('\t- l3out [%s/%s] already deleted' % (fabric['tenant'], fabric['bgp']['l3out']['name']))

    return True


def run(fabric, servers, my_output, log_id):
    my_output.default('\nApic [%s] domain [%s] configuration cleanup' % (fabric['apic'], fabric['domain']), underline=True)

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

    if fabric['bgp']['enabled']:
        if not unconfigure_bgp(handler, fabric, my_output):
            return False

    if not fabric['bgp']['enabled']:
        if not unconfigure_epg(handler, fabric, my_output):
            return False

        if not unconfigure_ap(handler, fabric, my_output):
            return False

        if not unconfigure_bd(handler, fabric, my_output):
            return False

    if not unconfigure_access_policy(handler, fabric, domain_servers, my_output):
        return False

    if not unconfigure_policy_group(handler, fabric, domain_servers, my_output):
        return False

    if not unconfigure_policy_cdp(handler, fabric, my_output):
        return False

    if not unconfigure_policy_lldp(handler, fabric, my_output):
        return False

    if not unconfigure_policy_link_level(handler, fabric, my_output):
        return False

    if not unconfigure_policy_l2(handler, fabric, my_output):
        return False

    if not unconfigure_policy_port_channel(handler, fabric, my_output):
        return False

    if not unconfigure_aae(handler, fabric, my_output):
        return False

    if not unconfigure_physical_domain(handler, fabric, my_output):
        return False

    if not unconfigure_l3_domain(handler, fabric, my_output):
        return False

    if not unconfigure_vlan_pool(handler, fabric, my_output):
        return False

    return True
