from lib import ip_helper


class Server():
    def __init__(self):
        pass

    def get_macs_lacp(self, mac_address, nodes):
        interface_filter = []
        if len(mac_address) > 0:
            interface_filter.append(
                'mac:%s' % (','.join(mac_address))
            )

        interfaces = []
        for node_info in nodes:
            proto_info = self.get_protocol_lacp(
                node_info['podId'],
                node_info['id'],
                instance_info=False,
                interface_info=True,
                interface_filter=interface_filter,
                event_info=False,
                event_filter=False
            )

            if proto_info is None:
                continue

            if 'interfaces' in proto_info:
                if proto_info['interfaces'] is not None:
                    interfaces = interfaces + proto_info['interfaces']

        lacp = []
        for interface_info in interfaces:
            for lacp_interface_info in interface_info['lacp']:
                lacp.append(
                    lacp_interface_info
                )

        return lacp

    def get_server_endpoint(self, server):
        endpoint_filter = []
        for mac_info in server['MacAddressInfo']:
            endpoint_filter.append(
                'mac:%s' % (mac_info['MacAddress'])
            )

        endpoints_info = self.get_endpoints(
            endpoint_filter=endpoint_filter,
            fabric_info=True
        )

        for mac_info in server['MacAddressInfo']:
            mac_info['endpoint'] = None
            for endpoint_info in endpoints_info:
                if ip_helper.is_mac_equal(mac_info['MacAddress'], endpoint_info['mac']):
                    mac_info['endpoint'] = endpoint_info

        return server

    def get_server_lacp(self, server, nodes):
        mac_address = []
        for mac_info in server['MacAddressInfo']:
            mac_address.append(
                mac_info['MacAddress']
            )

        interface_filter = []
        if len(mac_address) > 0:
            interface_filter.append(
                'mac:%s' % (','.join(mac_address))
            )

        interfaces = []
        for node_info in nodes:
            proto_info = self.get_protocol_lacp(
                node_info['podId'],
                node_info['id'],
                instance_info=False,
                interface_info=True,
                interface_filter=interface_filter,
                event_info=False,
                event_filter=False
            )

            if proto_info is None:
                continue

            if 'interfaces' in proto_info:
                if proto_info['interfaces'] is not None:
                    interfaces = interfaces + proto_info['interfaces']

        for mac_info in server['MacAddressInfo']:
            mac_info['lacp'] = []
            for interface_info in interfaces:
                for lacp_interface_info in interface_info['lacp']:
                    if ip_helper.is_mac_equal(mac_info['MacAddress'], lacp_interface_info['adjacency']['sysId']):
                        mac_info['lacp'].append(
                            lacp_interface_info
                        )

        return server

    def get_server_lldp(self, server, nodes):
        adjacency_filter = []
        for mac_info in server['MacAddressInfo']:
            adjacency_filter.append(
                'mac:%s' % (mac_info['MacAddress'])
            )

        adjacency = []

        for node_info in nodes:
            proto_info = self.get_protocol_lldp(
                node_info['podId'],
                node_info['id'],
                adjacency_filter=adjacency_filter,
                instance_info=True,
                stats_info=False,
                adjacency_info=True,
                fault_info=False,
                hfault_info=False,
                hfault_filter=None,
                event_info=False,
                event_filter=None
            )

            if proto_info is None:
                continue

            if proto_info['adjacency'] is not None:
                adjacency = adjacency + proto_info['adjacency']

        for mac_info in server['MacAddressInfo']:
            mac_info['adjacency'] = None
            for adj_info in adjacency:
                if ip_helper.is_mac_equal(mac_info['MacAddress'], adj_info['mac']):
                    mac_info['adjacency'] = adj_info

        return server

    def get_server_connectivity(self, server, nodes, ep_info=True, lacp_info=True, lldp_info=True):
        if ep_info:
            server = self.get_server_endpoint(
                server
            )

        if lacp_info:
            server = self.get_server_lacp(
                server,
                nodes
            )

        if lldp_info:
            server = self.get_server_lldp(
                server,
                nodes
            )

        return server
