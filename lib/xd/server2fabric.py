from lib import ip_helper
from lib.xd import aci as aci_helper
from lib.xd import nexus as nexus_helper


def get_server_macs(server_info):
    macs = []
    for mac_address_info in server_info['MacAddressInfo']:
        macs.append(mac_address_info['MacAddress'])
    return macs


def add_server_fabric_aci_lldp_info(server_info, log_id=None):
    lldp_info = aci_helper.get_aci_lldp_info(
        log_id=log_id
    )

    server_info['lldpSysName'] = None
    for mac_address in server_info['MacAddressInfo']:
        for node_info in lldp_info:
            for adjacency in node_info['adjacency']:
                if ip_helper.is_mac_equal(mac_address['MacAddress'], adjacency['portIdV']):
                    mac_address['Fabric']['Type'] = 'ACI'
                    mac_address['Fabric']['Controller'] = node_info['apic']
                    mac_address['Fabric']['Node'] = '%s/%s' % (
                        adjacency['pod_id'],
                        adjacency['node_id']
                    )
                    mac_address['Fabric']['Port'] = adjacency['interface_id']
                    mac_address['Fabric']['Source'] = 'lldp'
                    server_info['lldpSysName'] = adjacency['sysName']

    return server_info


def add_server_fabric_aci_cdp_info(server_info, log_id=None):
    cdp_info = aci_helper.get_aci_cdp_info(
        log_id=log_id
    )

    for mac_address in server_info['MacAddressInfo']:
        if len(mac_address['Fabric']) == 0:
            for node_info in cdp_info:
                for adjacency in node_info['neighbors']:
                    if adjacency['sysName'] == server_info['lldpSysName']:
                        mac_address['Fabric']['Type'] = 'ACI'
                        mac_address['Fabric']['Controller'] = node_info['apic']
                        mac_address['Fabric']['Node'] = '%s/%s' % (
                            adjacency['dn'].split('/')[1],
                            adjacency['dn'].split('/')[2]
                        )
                        mac_address['Fabric']['Port'] = adjacency['interfaceId']
                        mac_address['Fabric']['Source'] = 'cdp'

    return server_info


def add_server_fabric_aci_info(server_info, log_id=None, include_cdp=True):
    server_info = add_server_fabric_aci_lldp_info(
        server_info,
        log_id=log_id
    )

    if include_cdp:
        if server_info['lldpSysName'] is not None:
            server_info = add_server_fabric_aci_cdp_info(
                server_info,
                log_id=log_id
            )

    return server_info


def add_server_fabric_nexus_lldp_info(server_info, log_id=None):
    lldp_info = nexus_helper.get_nexus_lldp_info(
        log_id=log_id
    )

    for mac_address in server_info['MacAddressInfo']:
        for switch_info in lldp_info:
            for adjacency in switch_info['neighbors']:
                if ip_helper.is_mac_equal(mac_address['MacAddress'], adjacency['port_id']):
                    mac_address['Fabric']['Type'] = 'Nexus'
                    mac_address['Fabric']['Controller'] = '-'
                    mac_address['Fabric']['Node'] = switch_info['name']
                    mac_address['Fabric']['Port'] = adjacency['l_port_id']
                    mac_address['Fabric']['Source'] = 'lldp'

    return server_info


def add_server_fabric_nexus_info(server_info, log_id=None):
    server_info = add_server_fabric_nexus_lldp_info(
        server_info,
        log_id=log_id
    )

    return server_info


def add_server_fabric_info(iaccount, server_info, log_id=None, include_cdp=True):
    if 'MacAddressInfo' not in server_info:
        return server_info

    for mac_address_info in server_info['MacAddressInfo']:
        mac_address_info['Fabric'] = {}

    server_info = add_server_fabric_aci_info(
        server_info,
        log_id=log_id,
        include_cdp=include_cdp
    )

    server_info = add_server_fabric_nexus_info(
        server_info,
        log_id=log_id
    )

    return server_info
