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

    def print_proto_bgp_domains(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol BGP - Domain (VRF) [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
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
            'numPeers',
            'numEstPeers'
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
            'VRF',
            'Nbr Address',
            'Router Id',
            'Admin',
            'BGP',
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
            'Domain',
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
            'Domain',
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
            'Domain',
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
