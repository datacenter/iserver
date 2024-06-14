class ProtocolBgpOutput():
    def __init__(self):
        pass

    def print_proto_bgp_instances(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol BGP - Instance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'health',
            'faults',
            'adminSt',
            'asn',
            'summary.domains',
            'summary.neighbors',
            'numAsPath',
            'numRtAttrib',
            'memAlert',
            'snmpTrapSt',
            'syslogLvl'
        ]

        headers = [
            'Node',
            'Health',
            'Faults',
            'Admin',
            'ASN',
            'Domain (VRF)',
            'Neighbor',
            'AS Path',
            'Attribute',
            'Mem Status',
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

    def print_proto_bgp_domains(self, info, show_no_peers=False, title=False):
        domains = []
        for item in info:
            if show_no_peers:
                domains.append(item)
                continue

            if item['isPeer']:
                domains.append(item)
                continue

        if title:
            self.my_output.default(
                'Protocol BGP - Domain (VRF) [#%s]' % (len(domains)),
                underline=True,
                before_newline=True
            )

        if len(domains) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'name',
            'health',
            'faults',
            'operSt',
            'mode',
            'operRtrId',
            'rd',
            'peerSummary'
        ]

        headers = [
            'Node',
            'Domain (VRF)',
            'Health',
            'Faults',
            'BGP State',
            'Mode',
            'Router ID',
            'RD',
            'Neighbors'
        ]

        self.my_output.my_table(
            domains,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_bgp_peers(self, info):
        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            order = [
                'bgpDomainName',
                'state.addr',
                'state.rtrId',
                'state.localPort',
                'state.remotePort',
                'adminSt',
                'state.operSt',
                'state.lastFlapTs',
                'bfdTick',
                'asn',
                'localAsn',
                'asnPropagate',
                'state.type',
                'ttl',
                'srcIf',
                'state.localIp',
                'state.holdIntvl',
                'state.kaIntvl',
                'state.passwdSet',
                'state.connAttempts',
                'state.connDrop',
                'state.connEst',
                'state.advCap',
                'state.rcvCap',
                'l3out',
                'lnodep',
                'lifp'
            ]

            headers = [
                'Domain (VRF)',
                'Neighbor Address',
                'Remote Router Id',
                'Local Port',
                'Remote Port',
                'Admin State',
                'Session State',
                'Last Flap',
                'BFD',
                'Remote ASN',
                'Local ASN',
                'ASN Propagate',
                'Type',
                'TTL',
                'Source Intf',
                'Local IP',
                'Hold Interval',
                'Keepalive Interval',
                'MD5 Authentication',
                'Connection Attempts',
                'Connection Dropped',
                'Connection Established',
                'Capabilities Advertised',
                'Capabilities Received',
                'L3Out',
                'Logical Node Profile',
                'Logical Interface Profile'
            ]

            self.my_output.dictionary(
                item,
                title='Protocol BGP - Node %s - Peer %s' % (item['pod_node_name'], item['state']['addr']),
                keys=order,
                title_keys=headers,
                justify=True
            )

            stats = []
            stats.append(
                dict(
                    type='Opens',
                    sent=item['stats']['openSent'],
                    rcvd=item['stats']['openRcvd']
                )
            )

            stats.append(
                dict(
                    type='Notifications',
                    sent=item['stats']['notifSent'],
                    rcvd=item['stats']['notifRcvd']
                )
            )

            stats.append(
                dict(
                    type='Updates',
                    sent=item['stats']['updateSent'],
                    rcvd=item['stats']['updateRcvd']
                )
            )

            stats.append(
                dict(
                    type='Keepalives',
                    sent=item['stats']['kaSent'],
                    rcvd=item['stats']['kaRcvd']
                )
            )

            stats.append(
                dict(
                    type='Route Refresh',
                    sent=item['stats']['routeRefreshSent'],
                    rcvd=item['stats']['routeRefreshRcvd']
                )
            )

            stats.append(
                dict(
                    type='Capability',
                    sent=item['stats']['capSent'],
                    rcvd=item['stats']['capRcvd']
                )
            )

            stats.append(
                dict(
                    type='Total',
                    sent=item['stats']['msgSent'],
                    rcvd=item['stats']['msgRcvd']
                )
            )

            stats.append(
                dict(
                    type='Total Bytes',
                    sent=item['stats']['byteSent'],
                    rcvd=item['stats']['byteRcvd']
                )
            )

            stats.append(
                dict(
                    type='Bytes in Queue',
                    sent=item['stats']['byteInSendQ'],
                    rcvd=item['stats']['byteInRecvQ']
                )
            )

            self.my_output.my_table(
                stats,
                order=['type', 'sent', 'rcvd'],
                headers=['Message Type', 'Sent', 'Received'],
                allow_order_subkeys=True,
                remove_empty_columns=True,
                underline=True,
                table=True
            )

            for address_family in ['af-ipv4-ucast', 'af-ipv4-lu', 'af-l2vpn-evpn']:
                if 'state' in item and address_family in item['state']:
                    self.my_output.dictionary(
                        item['state'][address_family],
                        title='AF %s' % (address_family),
                        keys=['acceptedPaths', 'pfxFlushed', 'pfxSaved', 'pfxSent', 'tblSt', 'tblVer'],
                        title_keys=['acceptedPaths', 'pfxFlushed', 'pfxSaved', 'pfxSent', 'tblSt', 'tblVer'],
                        justify=True
                    )

    def print_proto_bgp_neighbors(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol BGP - Neighbor [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'bgpDomainName',
            'state.addr',
            'state.rtrId',
            'adminSt',
            'state.operSt',
            'bfdTick',
            'asn',
            'state.type',
            'ttl',
            'srcIf',
            'state.localIp',
            'state.connSummary',
            'paths'
        ]

        headers = [
            'Node',
            'Domain (VRF)',
            'Nbr Address',
            'Router Id',
            'Admin',
            'Session',
            'BFD',
            'ASN',
            'Type',
            'TTL',
            'Src Intf',
            'Local IP',
            'Conns (A/D/E)',
            'Paths'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['paths']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_bgp_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol BGP - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'domainNameT',
            'neiT',
            'descrT'
        ]

        headers = [
            'Node',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Lifecycle',
            'Domain (VRF)',
            'Nbr',
            'Description'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_bgp_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol BGP - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol BGP - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'domainNameT',
            'neiT',
            'descrT'
        ]

        headers = [
            'Node',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Lifecycle',
            'Domain (VRF)',
            'Nbr',
            'Description'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_bgp_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol BGP - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol BGP - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT',
            'domainNameT',
            'neiT'
        ]

        headers = [
            'Node',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Description',
            'Change Set',
            'Domain (VRF)',
            'Nbr',
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT', 'changeSetT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            row_separator=True,
            underline=True,
            table=True
        )
