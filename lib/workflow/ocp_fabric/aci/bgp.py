from lib import ip_helper


def get_bgp_enabled(fabric):
    body = {}
    body['bgpExtP'] = {}
    body['bgpExtP']['attributes'] = {}
    body['bgpExtP']['attributes']['dn'] = 'uni/tn-%s/out-%s/bgpExtP' % (
        fabric['tenant'],
        fabric['bgp']['l3out']['name']
    )
    body['bgpExtP']['attributes']['status'] = 'created'
    body['bgpExtP']['children'] = []
    return body


def get_external_epg(fabric):
    body = {}
    body['l3extInstP'] = {}
    body['l3extInstP']['attributes'] = {}
    body['l3extInstP']['attributes']['dn'] = 'uni/tn-%s/out-%s/instP-%s' % (
        fabric['tenant'],
        fabric['bgp']['l3out']['name'],
        fabric['bgp']['epg']['name']
    )
    body['l3extInstP']['attributes']['rn'] = fabric['bgp']['epg']['name']
    body['l3extInstP']['attributes']['status'] = 'created'
    body['l3extInstP']['children'] = []

    for subnet in fabric['bgp']['epg']['subnet']:
        subnet_mo = {}
        subnet_mo['l3extSubnet'] = {}
        subnet_mo['l3extSubnet']['attributes'] = {}
        subnet_mo['l3extSubnet']['attributes']['dn'] = 'uni/tn-%s/out-%s/instP-%s/extsubnet-[%s]' % (
            fabric['tenant'],
            fabric['bgp']['l3out']['name'],
            fabric['bgp']['epg']['name'],
            subnet['ip']
        )
        subnet_mo['l3extSubnet']['attributes']['ip'] = subnet['ip']
        if subnet['scope'] is not None and len(subnet['scope']) > 0:
            subnet_mo['l3extSubnet']['attributes']['scope'] = '%s,' % (','.join(subnet['scope']))
        subnet_mo['l3extSubnet']['attributes']['status'] = 'created'
        subnet_mo['l3extSubnet']['attributes']['rn'] = 'extsubnet-[%s]' % (
            subnet['ip']
        )
        subnet_mo['l3extSubnet']['children'] = []
        body['l3extInstP']['children'].append(
            subnet_mo
        )

    return body


def get_node(fabric, leaf_key):
    body = {}
    body['l3extRsNodeL3OutAtt'] = {}
    body['l3extRsNodeL3OutAtt']['attributes'] = {}
    body['l3extRsNodeL3OutAtt']['attributes']['dn'] = 'uni/tn-%s/out-%s/lnodep-%s/rsnodeL3OutAtt-[topology/pod-%s/node-%s]' % (
        fabric['tenant'],
        fabric['bgp']['l3out']['name'],
        fabric['bgp']['lnp']['name'],
        fabric['bgp'][leaf_key]['pod'],
        fabric['bgp'][leaf_key]['id']
    )
    body['l3extRsNodeL3OutAtt']['attributes']['tDn'] = 'topology/pod-%s/node-%s' % (
        fabric['bgp'][leaf_key]['pod'],
        fabric['bgp'][leaf_key]['id']
    )
    body['l3extRsNodeL3OutAtt']['attributes']['rtrId'] = fabric['bgp'][leaf_key]['rtr_id']
    body['l3extRsNodeL3OutAtt']['attributes']['rtrIdLoopBack'] = str(fabric['bgp'][leaf_key]['loopback']).lower()
    body['l3extRsNodeL3OutAtt']['attributes']['status'] = 'created'
    body['l3extRsNodeL3OutAtt']['attributes']['rn'] = 'rsnodeL3OutAtt-[topology/pod-%s/node-%s]' % (
        fabric['bgp'][leaf_key]['pod'],
        fabric['bgp'][leaf_key]['id']
    )
    body['l3extRsNodeL3OutAtt']['children'] = []
    return body


def get_server_svi_member(fabric, key, tdn):
    body = {}
    body['l3extMember'] = {}
    body['l3extMember']['attributes'] = {}
    body['l3extMember']['attributes']['dn'] = 'uni/tn-%s/out-%s/lnodep-%s/lifp-%s/rspathL3OutAtt-[%s]/mem-%s' % (
        fabric['tenant'],
        fabric['bgp']['l3out']['name'],
        fabric['bgp']['lnp']['name'],
        fabric['bgp']['lnp']['lip'],
        tdn,
        key
    )
    body['l3extMember']['attributes']['addr'] = fabric['bgp']['leaf_%s' % (key)]['cidr']
    body['l3extMember']['attributes']['status'] = 'created'
    body['l3extMember']['attributes']['rn'] = 'mem-%s' % (key)
    body['l3extMember']['children'] = []

    ext_ip_mo = {}
    ext_ip_mo['l3extIp'] = {}
    ext_ip_mo['l3extIp']['attributes'] = {}
    ext_ip_mo['l3extIp']['attributes']['dn'] = 'uni/tn-%s/out-%s/lnodep-%s/lifp-%s/rspathL3OutAtt-[%s]/mem-%s/addr-[%s]' % (
        fabric['tenant'],
        fabric['bgp']['l3out']['name'],
        fabric['bgp']['lnp']['name'],
        fabric['bgp']['lnp']['lip'],
        tdn,
        key,
        fabric['bgp']['gateway']
    )
    ext_ip_mo['l3extIp']['attributes']['addr'] = fabric['bgp']['gateway']
    ext_ip_mo['l3extIp']['attributes']['status'] = 'created'
    ext_ip_mo['l3extIp']['attributes']['rn'] = 'addr-[%s]' % (fabric['bgp']['gateway'])
    ext_ip_mo['l3extIp']['children'] = []

    body['l3extMember']['children'].append(
        ext_ip_mo
    )

    return body


def get_server_svi_peer(fabric, tdn):
    body = {}
    body['bgpPeerP'] = {}
    body['bgpPeerP']['attributes'] = {}
    body['bgpPeerP']['attributes']['dn'] = 'uni/tn-%s/out-%s/lnodep-%s/lifp-%s/rspathL3OutAtt-[%s]/peerP-[%s]' % (
        fabric['tenant'],
        fabric['bgp']['l3out']['name'],
        fabric['bgp']['lnp']['name'],
        fabric['bgp']['lnp']['lip'],
        tdn,
        ip_helper.get_network_cidr_from_cidr(fabric['bgp']['gateway'])
    )
    body['bgpPeerP']['attributes']['addr'] = ip_helper.get_network_cidr_from_cidr(fabric['bgp']['gateway'])
    body['bgpPeerP']['attributes']['ttl'] = str(fabric['bgp']['ttl'])
    body['bgpPeerP']['attributes']['status'] = 'created'

    body['bgpPeerP']['children'] = []

    asn_mo = {}
    asn_mo['bgpAsP'] = {}
    asn_mo['bgpAsP']['attributes'] = {}
    asn_mo['bgpAsP']['attributes']['dn'] = 'uni/tn-%s/out-%s/lnodep-%s/lifp-%s/rspathL3OutAtt-[%s]/peerP-[%s]/as' % (
        fabric['tenant'],
        fabric['bgp']['l3out']['name'],
        fabric['bgp']['lnp']['name'],
        fabric['bgp']['lnp']['lip'],
        tdn,
        ip_helper.get_network_cidr_from_cidr(fabric['bgp']['gateway'])
    )
    asn_mo['bgpAsP']['attributes']['asn'] = str(fabric['bgp']['asn'])
    asn_mo['bgpAsP']['attributes']['status'] = 'created'
    asn_mo['bgpAsP']['children'] = []

    body['bgpPeerP']['children'].append(
        asn_mo
    )

    return body


def get_server_svi(fabric, server, tdn):
    body = {}
    body['l3extRsPathL3OutAtt'] = {}
    body['l3extRsPathL3OutAtt']['attributes'] = {}
    body['l3extRsPathL3OutAtt']['attributes']['dn'] = 'uni/tn-%s/out-%s/lnodep-%s/lifp-%s/rspathL3OutAtt-[%s]' % (
        fabric['tenant'],
        fabric['bgp']['l3out']['name'],
        fabric['bgp']['lnp']['name'],
        fabric['bgp']['lnp']['lip'],
        tdn
    )
    body['l3extRsPathL3OutAtt']['attributes']['tDn'] = tdn
    body['l3extRsPathL3OutAtt']['attributes']['rn'] = 'rspathL3OutAtt-[%s]' % (tdn)
    body['l3extRsPathL3OutAtt']['attributes']['ifInstT'] = 'ext-svi'
    body['l3extRsPathL3OutAtt']['attributes']['mtu'] = server['interface'][0]['mtu']
    body['l3extRsPathL3OutAtt']['attributes']['encap'] = 'vlan-%s' % (server['interface'][0]['vlan'])
    body['l3extRsPathL3OutAtt']['attributes']['status'] = 'created'
    body['l3extRsPathL3OutAtt']['children'] = []

    body['l3extRsPathL3OutAtt']['children'].append(
        get_server_svi_member(
            fabric,
            'A',
            tdn
        )
    )

    body['l3extRsPathL3OutAtt']['children'].append(
        get_server_svi_member(
            fabric,
            'B',
            tdn
        )
    )

    body['l3extRsPathL3OutAtt']['children'].append(
        get_server_svi_peer(
            fabric,
            tdn
        )
    )

    return body


def get_lip(handler, fabric, server, my_output):
    body = {}
    body['l3extLIfP'] = {}
    body['l3extLIfP']['attributes'] = {}
    body['l3extLIfP']['attributes']['dn'] = 'uni/tn-%s/out-%s/lnodep-%s/lifp-%s' % (
        fabric['tenant'],
        fabric['bgp']['l3out']['name'],
        fabric['bgp']['lnp']['name'],
        fabric['bgp']['lnp']['lip']
    )
    body['l3extLIfP']['attributes']['name'] = fabric['bgp']['lnp']['lip']
    body['l3extLIfP']['attributes']['rn'] = 'lifp-%s' % (fabric['bgp']['lnp']['lip'])
    body['l3extLIfP']['attributes']['status'] = 'created,modified'
    body['l3extLIfP']['children'] = []

    if len(server) == 1:
        policy_name = fabric['policy_group']['name']
        configuration_info = handler.get_configuration_vpc(
            policy_name,
            cache_enabled=False
        )
        if configuration_info is None:
            my_output.error('Unexpected failure in getting configuration details: %s' % (policy_name))
            return None

        if fabric['bgp']['type'] == 'svi':
            body['l3extLIfP']['children'].append(
                get_server_svi(
                    fabric,
                    server[0],
                    configuration_info['pcPortDn']
                )
            )
    else:
        index = 1
        for item in server:
            policy_name = '%s-%s' % (fabric['policy_group']['name'], index)
            configuration_info = handler.get_configuration_vpc(
                policy_name,
                cache_enabled=False
            )
            if configuration_info is None:
                my_output.error('Unexpected failure in getting configuration details: %s' % (policy_name))
                return False

            if fabric['bgp']['type'] == 'svi':
                body['l3extLIfP']['children'].append(
                    get_server_svi(
                        fabric,
                        item,
                        configuration_info['pcPortDn']
                    )
                )

            index += 1

    return body


def get_lnp(handler, fabric, server, my_output):
    body = {}
    body['l3extLNodeP'] = {}
    body['l3extLNodeP']['attributes'] = {}
    body['l3extLNodeP']['attributes']['dn'] = 'uni/tn-%s/out-%s/lnodep-%s' % (
        fabric['tenant'],
        fabric['bgp']['l3out']['name'],
        fabric['bgp']['lnp']['name']
    )
    body['l3extLNodeP']['attributes']['name'] = fabric['bgp']['lnp']['name']
    body['l3extLNodeP']['attributes']['rn'] = 'lnodep-%s' % (
        fabric['bgp']['lnp']['name']
    )
    body['l3extLNodeP']['attributes']['status'] = 'created'
    body['l3extLNodeP']['children'] = []

    lip = get_lip(handler, fabric, server, my_output)
    if lip is None:
        return None

    body['l3extLNodeP']['children'].append(
        lip
    )
    body['l3extLNodeP']['children'].append(
        get_node(fabric, 'leaf_A')
    )
    body['l3extLNodeP']['children'].append(
        get_node(fabric, 'leaf_B')
    )

    return body


def get_l3out(handler, fabric, server, my_output):
    body = {}
    body['l3extOut'] = {}
    body['l3extOut']['attributes'] = {}
    body['l3extOut']['attributes']['dn'] = 'uni/tn-%s/out-%s' % (
        fabric['tenant'],
        fabric['bgp']['l3out']['name']
    )
    body['l3extOut']['attributes']['name'] = fabric['bgp']['l3out']['name']
    body['l3extOut']['attributes']['status'] = 'created,modified'
    body['l3extOut']['attributes']['rn'] = 'out-%s' % (fabric['bgp']['l3out']['name'])
    body['l3extOut']['children'] = []

    body['l3extOut']['children'].append(
        get_bgp_enabled(fabric)
    )
    body['l3extOut']['children'].append(
        get_external_epg(fabric)
    )

    lnp = get_lnp(handler, fabric, server, my_output)
    if lnp is None:
        return None

    body['l3extOut']['children'].append(
        lnp
    )

    vrf_mo = {}
    vrf_mo['l3extRsEctx'] = {}
    vrf_mo['l3extRsEctx']['attributes'] = {}
    vrf_mo['l3extRsEctx']['attributes']['tnFvCtxName'] = fabric['vrf']
    vrf_mo['l3extRsEctx']['attributes']['status'] = 'created,modified'
    vrf_mo['l3extRsEctx']['children'] = []
    body['l3extOut']['children'].append(
        vrf_mo
    )

    l3out_mo = {}
    l3out_mo['l3extRsL3DomAtt'] = {}
    l3out_mo['l3extRsL3DomAtt']['attributes'] = {}
    l3out_mo['l3extRsL3DomAtt']['attributes']['tDn'] = 'uni/l3dom-%s' % (fabric['bgp']['l3out']['name'])
    l3out_mo['l3extRsL3DomAtt']['attributes']['status'] = 'created'
    l3out_mo['l3extRsL3DomAtt']['children'] = []
    body['l3extOut']['children'].append(
        l3out_mo
    )

    return body


def get_body(handler, fabric, server, my_output):
    body = {}
    body['fvTenant'] = {}
    body['fvTenant']['attributes'] = {}
    body['fvTenant']['attributes']['dn'] = 'uni/tn-%s' % (fabric['tenant'])
    body['fvTenant']['attributes']['name'] = fabric['tenant']
    body['fvTenant']['attributes']['status'] = 'created,modified'
    body['fvTenant']['attributes']['rn'] = 'tn-%s' % (fabric['tenant'])
    l3out = get_l3out(handler, fabric, server, my_output)
    if l3out is None:
        return None

    body['fvTenant']['children'] = [l3out]
    return body