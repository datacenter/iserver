class Context():
    def __init__(self):
        pass

    def get_context_server_connectivity_interface(self, servers_connectivity_info):
        interfaces = []

        for server_connectivity_info in servers_connectivity_info:
            if 'MacAddressInfo' not in server_connectivity_info:
                continue

            for mac_address_info in server_connectivity_info['MacAddressInfo']:
                if mac_address_info['endpoint'] is not None:
                    for fabric_info in mac_address_info['endpoint']['fabric']:
                        interface_label = 'aci:%s:pod-%s:node-%s:%s' % (
                            mac_address_info['endpoint']['apic'],
                            fabric_info['pod_id'],
                            fabric_info['node_id'],
                            fabric_info['port_id']
                        )
                        if interface_label not in interfaces:
                            interfaces.append(interface_label)

                if mac_address_info['lacp'] is not None:
                    for lacp_info in mac_address_info['lacp']:
                        interface_label = 'aci:%s:pod-%s:node-%s:%s' % (
                            lacp_info['apic'],
                            lacp_info['podId'],
                            lacp_info['nodeId'],
                            lacp_info['id']
                        )
                        if interface_label not in interfaces:
                            interfaces.append(interface_label)

                if mac_address_info['adjacency'] is not None:
                    interface_label = 'aci:%s:%s:%s:%s' % (
                        mac_address_info['adjacency']['apic'],
                        mac_address_info['adjacency']['pod_id'],
                        mac_address_info['adjacency']['node_id'],
                        mac_address_info['adjacency']['interface_id']
                    )
                    if interface_label not in interfaces:
                        interfaces.append(interface_label)

        return interfaces
