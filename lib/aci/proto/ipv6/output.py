class ProtocolIpv6Output():
    def __init__(self):
        pass

    def print_proto_ipv6_instances(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol IPv6 - Instance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'adminSt',
            'health',
            'faults',
            'domains',
            'summary.count',
            'summary.default',
            'summary.direct',
            'summary.local',
            'summary.bgp',
            'summary.ibgp',
            'summary.ebgp'
        ]

        headers = [
            'Node',
            'Admin State',
            'Health',
            'Faults',
            'Domain',
            'Route',
            'Default',
            'Direct',
            'Local',
            'BGP',
            'iBGP',
            'eBGP'
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

    def print_proto_ipv6_domains(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol IPv6 - Domain (VRF) [#%s]' % (len(info)),
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
            'faults',
            'operSt',
            'summary.count',
            'summary.default',
            'summary.direct',
            'summary.local',
            'summary.bgp',
            'summary.ibgp',
            'summary.ebgp'
        ]

        headers = [
            'Node',
            'VRF',
            'Faults',
            'OperSt',
            'Route',
            'Default',
            'Direct',
            'Local',
            'BGP',
            'iBGP',
            'eBGP'
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

    def print_proto_ipv6_routes(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol IPv6 - Route [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'vrf',
            'prefix',
            'health',
            'faults',
            'next_hop.addr',
            'next_hop.routeType',
            'next_hop.owner',
            'next_hop.if',
            'next_hop.vrf',
            'next_hop.mplsLabel',
            'next_hop.active',
            'next_hop.pref',
        ]

        headers = [
            'Node',
            'VRF',
            'Prefix',
            'Health',
            'Faults',
            'Next Hop',
            'Type',
            'Source',
            'Interface',
            'NH VRF',
            'MPLS Label',
            'Active',
            'Preference'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['next_hop']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_proto_ipv6_routes_summary(self, info):
        order = [
            'count',
            'default',
            'direct',
            'local',
            'bgp',
            'ibgp',
            'ebgp'
        ]

        headers = [
            'Routes',
            'Default',
            'Direct',
            'Local',
            'BGP',
            'iBGP',
            'eBGP'
        ]

        self.my_output.dictionary(
            info,
            title='IPv6 Routes Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_ipv6_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol IPv6 - Faults [#%s]' % (len(info)),
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
            'interfaceIdT',
            'addressT',
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
            'Interface',
            'Address',
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

    def print_proto_ipv6_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol IPv6 - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol IPv6 - Fault Records last %s [#%s]' % (when, len(info)),
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
            'interfaceIdT',
            'addressT',
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
            'Interface',
            'Address',
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

    def print_proto_ipv6_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol IPv6 - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol IPv6 - Event Logs last %s [#%s]' % (when, len(info)),
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
            'domainNameT',
            'interfaceIdT',
            'addressT',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Node',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Domain',
            'Interface',
            'Address',
            'Description',
            'Change Set'
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
