from lib import ip_helper


class AciMac():
    def __init__(self):
        pass

    def get_aci_mac_info(self, mac_address):
        info = {}
        info['src'] = []
        info['intf'] = []

        info['ep'] = []
        for controller in self.aci_ep:
            for endpoint in self.aci_ep[controller]:
                if ip_helper.is_mac_equal(endpoint['mac'], mac_address):
                    ep_info = {}
                    ep_info['apic'] = endpoint['apic']
                    ep_info['dn'] = endpoint['dn']
                    ep_info['bd'] = endpoint['bdNameTenant']
                    ep_info['vrf'] = endpoint['vrfNameTenant']
                    ep_info['epg'] = endpoint['epgNameApTenant']
                    ep_info['mac'] = endpoint['mac']
                    ep_info['ip'] = endpoint['ip']
                    for fabric_info in endpoint['fabric']:
                        ep_info['node'] = fabric_info['node_id']
                        ep_info['interface'] = fabric_info['port_id']
                        info['ep'].append(
                            ep_info
                        )

                        iinfo = '%s:%s:%s' % (
                            ep_info['apic'],
                            ep_info['node'],
                            ep_info['interface']
                        )

                        if iinfo not in info['intf']:
                            info['intf'].append(
                                iinfo
                            )

                        if 'ep' not in info['src']:
                            info['src'].append('ep')

        info['lldp'] = []
        for apic in self.aci_lldp:
            for adjacency in self.aci_lldp[apic]:
                if ip_helper.is_mac_equal(adjacency['mac'], mac_address):
                    info['lldp'].append(
                        adjacency
                    )

                    iinfo = '%s:%s:%s' % (
                        adjacency['apic'],
                        adjacency['node_id'],
                        adjacency['interface_id']
                    )

                    if iinfo not in info['intf']:
                        info['intf'].append(
                            iinfo
                        )

                    if 'lldp' not in info['src']:
                        info['src'].append('lldp')

        info['lacp'] = []

        return info
