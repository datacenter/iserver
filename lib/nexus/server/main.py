from lib import ip_helper


class Server():
    def __init__(self):
        pass

    def get_server_mac(self, server):
        mac_filter = []
        for mac_info in server['MacAddressInfo']:
            if 'mac' not in mac_info:
                mac_info['mac'] = None
            mac_filter.append(
                mac_info['MacAddress']
            )

        object_filter = []
        object_filter.append(
            'mac:%s' % (','.join(mac_filter))
        )

        device_macs = self.get_macs(
            object_filter=object_filter
        )

        if device_macs is None:
            self.log.error(
                'get_server_mac',
                'MAC info failed: %s' % (self.nexus_name)
            )
            return server

        if device_macs is not None:
            for mac_info in server['MacAddressInfo']:
                for device_mac in device_macs:
                    if ip_helper.is_mac_equal(mac_info['MacAddress'], device_mac['mac_addr']):
                        mac_info['mac'] = device_mac

        return server

    def get_server_lacp(self, server):
        mac_filter = []
        for mac_info in server['MacAddressInfo']:
            if 'interface' not in mac_info:
                mac_info['interface'] = None

            mac_filter.append(
                mac_info['MacAddress']
            )

        object_filter = []
        object_filter.append(
            'mac:%s' % (','.join(mac_filter))
        )

        device_interfaces = self.get_lacps(
            object_filter=object_filter
        )

        if device_interfaces is None:
            self.log.error(
                'get_server_lacp',
                'LACP info failed: %s' % (self.nexus_name)
            )
            return server

        for mac_info in server['MacAddressInfo']:
            for device_interface in device_interfaces:
                port_match = False
                for port_info in device_interface['port']:
                    if ip_helper.is_mac_equal(mac_info['MacAddress'], port_info['partner_mac']):
                        port_match = True

                if port_match:
                    mac_info['interface'] = device_interfaces

        return server

    def get_server_lldp(self, server):
        mac_filter = []
        for mac_info in server['MacAddressInfo']:
            if 'adjacency' not in mac_info:
                mac_info['adjacency'] = None
            mac_filter.append(
                mac_info['MacAddress']
            )

        object_filter = []
        object_filter.append(
            'mac:%s' % (','.join(mac_filter))
        )

        device_neighbors = self.get_lldps(
            object_filter=object_filter
        )

        if device_neighbors is None:
            self.log.error(
                'get_server_lldp',
                'LLDP info failed: %s' % (self.nexus_name)
            )
            return server

        for mac_info in server['MacAddressInfo']:
            for device_neighbor in device_neighbors:
                if ip_helper.is_mac_equal(mac_info['MacAddress'], device_neighbor['port_id']):
                    mac_info['adjacency'] = device_neighbor

        return server

    def get_server_connectivity(self, server, mac_info=True, lacp_info=True, lldp_info=True):
        if mac_info:
            server = self.get_server_mac(
                server
            )

        if lacp_info:
            server = self.get_server_lacp(
                server
            )

        if lldp_info:
            server = self.get_server_lldp(
                server
            )

        return server
