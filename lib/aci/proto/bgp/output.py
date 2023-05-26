class ProtocolBgpOutput():
    def __init__(self):
        pass

    def print_proto_bgp(self, info):
        self.print_proto_bgp_instance(
            info['instance']
        )

        self.print_proto_bgp_domains(
            info['domains']
        )

        self.print_proto_bgp_neighbors(
            info['neighbors']
        )

    def print_proto_bgp_instances(self, info):
        if len(info) == 0:
            return

        order = [
            'instance.pod_node_name',
            'instance.adminSt',
            'instance.asn',
            'instance.summary.domains',
            'instance.summary.neighbors',
            'instance.numAsPath',
            'instance.numRtAttrib',
            'instance.memAlert',
            'instance.snmpTrapSt',
            'instance.syslogLvl'
        ]

        headers = [
            'Node',
            'Admin State',
            'ASN',
            'VRF (Up/Count)',
            'Neighbors (Up/Count)',
            'AS Path Entries',
            'Attribute Entries',
            'Memory Status',
            'SNMP Trap',
            'Syslog Level'
        ]

        self.my_output.my_table(
            info,
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_bgp_instance(self, info):
        order = [
            'pod_node_name',
            'adminSt',
            'asn',
            'numAsPath',
            'asPathDbSz',
            'numRtAttrib',
            'attribDbSz',
            'memAlert',
            'snmpTrapSt',
            'syslogLvl',
            'createTs',
            'activateTs',
            'waitDoneTs'
        ]

        headers = [
            'Admin State',
            'ASN',
            'AS Path Entries',
            'Bytes in AS Path Entries',
            'Attribute Entries',
            'Bytes in Attribute Entries',
            'Memory Status',
            'SNMP Trap',
            'Syslog Level',
            'Created',
            'Activated',
            'Out of Wait'
        ]

        self.my_output.dictionary(
            info,
            title='BGP Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_bgp_domains(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'name',
            'operSt',
            'mode',
            'operRtrId',
            'rd',
            'numPeers',
            'numEstPeers'
        ]

        headers = [
            'Node',
            'VRF',
            'BGP State',
            'Mode',
            'Router ID',
            'RD',
            'Neighbors',
            'Established'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_bgp_domain(self, info):
        order = [
            'name',
            'operSt',
            'mode',
            'operRtrId',
            'rd',
            'numPeers',
            'numEstPeers'
        ]

        headers = [
            'VRF',
            'BGP State',
            'Mode',
            'Router ID',
            'RD',
            'Neighbors',
            'Established'
        ]

        self.my_output.dictionary(
            info,
            title='BGP VRF',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        if 'neighbors' in info:
            self.print_proto_bgp_domain_neighbors(
                info['neighbors']
            )

    def print_proto_bgp_domain_neighbors(self, info):
        if len(info) == 0:
            return

        order = [
            'state.addr',
            'state.rtrId',
            'adminSt',
            'state.operSt',
            'asn',
            'state.type',
            'ttl',
            'srcIf',
            'state.localIp',
            'state.connSummary',
            'state.af-ipv4-ucast.acceptedPaths'
        ]

        headers = [
            'Neighbor Address',
            'Router Id',
            'Admin State',
            'BGP State',
            'ASN',
            'Type',
            'TTL',
            'Source Intf',
            'Local IP',
            'Connections (A/D/E)',
            'Accepted Paths'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_bgp_neighbors_transport(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'bgpDomainName',
            'state.addr',
            'state.rtrId',
            'adminSt',
            'state.operSt',
            'asn',
            'state.type',
            'ttl',
            'srcIf',
            'state.localIp'
        ]

        headers = [
            'Node',
            'VRF',
            'Neighbor Address',
            'Router Id',
            'Admin State',
            'BGP State',
            'ASN',
            'Type',
            'TTL',
            'Source Intf',
            'Local IP'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_bgp_neighbors_summary(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'bgpDomainName',
            'state.addr',
            'state.operSt',
            'asn',
            'state.type',
            'ttl',
            'state.af-ipv4-ucast.acceptedPaths'
        ]

        headers = [
            'Node',
            'VRF',
            'Neighbor Address',
            'BGP State',
            'ASN',
            'Type',
            'TTL',
            'Paths (AF IPv4)'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_bgp_neighbors_connections(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'bgpDomainName',
            'state.addr',
            'state.operSt',
            'asn',
            'state.type',
            'ttl',
            'state.connAttempts',
            'state.connDrop',
            'state.connEst'
        ]

        headers = [
            'Node',
            'VRF',
            'Neighbor Address',
            'BGP State',
            'ASN',
            'Type',
            'TTL',
            'Attempts',
            'Drops',
            'Established'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_bgp_neighbors_af(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'bgpDomainName',
            'state.addr',
            'state.operSt',
            'asn',
            'state.type',
            'ttl',
            'state.af-ipv4-ucast.acceptedPaths',
            'state.af-vpnv4-ucast.acceptedPaths',
            'state.af-vpnv6-ucast.acceptedPaths'
        ]

        headers = [
            'Node',
            'VRF',
            'Neighbor Address',
            'BGP State',
            'ASN',
            'Type',
            'TTL',
            'AF IPv4',
            'AF VPNv4',
            'AF VPNv6'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_bgp_neighbor(self, info):
        order = [
            'bgpDomainName',
            'adminSt',
            'state.operSt',
            'state.addr',
            'state.rtrId',
            'state.remotePort',
            'asn',
            'state.rcvCap',
            'state.type',
            'ttl',
            'state.peerIdx',
            'srcIf',
            'state.localIp',
            'state.localPort',
            'state.advCap',
            'state.holdIntvl',
            'state.kaIntvl',
            'state.connAttempts',
            'state.connEst',
            'state.connDrop',
            'state.af-ipv4-ucast.acceptedPaths'
        ]

        headers = [
            'VRF',
            'Admin State',
            'BGP State',
            'Neighbor Address',
            'Remote Router Id',
            'Remote Port',
            'Remote ASN',
            'Received Capabilities',
            'Session Type',
            'TTL',
            'Peer Index',
            'Update Source Intf',
            'Local IP',
            'Local Port',
            'Advertised Capabilities',
            'Hold Timer',
            'Keepalive Timer',
            'Connection Attempts',
            'Connection Established',
            'Connection Dropped',
            'Accepted IPv4 Unicast Paths'
        ]

        self.my_output.dictionary(
            info,
            title='BGP Neighbor',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        if 'stats' in info and info['stats'] is not None:
            self.print_proto_bgp_neighbor_stats(
                info['stats']
            )

        if 'routes' in info and info['routes'] is not None and len(info['routes']) > 0:
            self.print_protocol_ipv4_routes(
                info['routes']
            )

    def print_proto_bgp_neighbor_stats(self, info):
        order = [
            'type',
            'sent',
            'rcvd'
        ]

        headers = [
            'Message Type',
            'Sent',
            'Received'
        ]

        stats = []

        stat_entry = {}
        stat_entry['type'] = 'Opens'
        stat_entry['sent'] = info['openSent']
        stat_entry['rcvd'] = info['openRcvd']
        stats.append(stat_entry)

        stat_entry = {}
        stat_entry['type'] = 'Notifications'
        stat_entry['sent'] = info['notifSent']
        stat_entry['rcvd'] = info['notifRcvd']
        stats.append(stat_entry)

        stat_entry = {}
        stat_entry['type'] = 'Updates'
        stat_entry['sent'] = info['updateSent']
        stat_entry['rcvd'] = info['updateRcvd']
        stats.append(stat_entry)

        stat_entry = {}
        stat_entry['type'] = 'Keepalives'
        stat_entry['sent'] = info['kaSent']
        stat_entry['rcvd'] = info['kaRcvd']
        stats.append(stat_entry)

        stat_entry = {}
        stat_entry['type'] = 'Route Refresh'
        stat_entry['sent'] = info['routeRefreshSent']
        stat_entry['rcvd'] = info['routeRefreshRcvd']
        stats.append(stat_entry)

        stat_entry = {}
        stat_entry['type'] = 'Capability'
        stat_entry['sent'] = info['capSent']
        stat_entry['rcvd'] = info['capRcvd']
        stats.append(stat_entry)

        stat_entry = {}
        stat_entry['type'] = 'Total'
        stat_entry['sent'] = info['msgSent']
        stat_entry['rcvd'] = info['msgRcvd']
        stats.append(stat_entry)

        stat_entry = {}
        stat_entry['type'] = 'Total Bytes'
        stat_entry['sent'] = info['byteSent']
        stat_entry['rcvd'] = info['byteRcvd']
        stats.append(stat_entry)

        stat_entry = {}
        stat_entry['type'] = 'Bytes in Queue'
        stat_entry['sent'] = info['byteInSendQ']
        stat_entry['rcvd'] = info['byteInRecvQ']
        stats.append(stat_entry)

        self.my_output.my_table(
            stats,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )
