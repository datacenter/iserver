class ProtocolIpv4Output():
    def __init__(self):
        pass

    def print_protocol_ipv4(self, info):
        self.print_protocol_ipv4_domains(
            info['domains']
        )

    def print_protocol_ipv4_domains(self, info):
        order = [
            'pod_node_name',
            'name',
            'operSt',
            'routes_summary.count',
            'routes_summary.default',
            'routes_summary.direct',
            'routes_summary.local',
            'routes_summary.bgp',
            'routes_summary.ibgp',
            'routes_summary.ebgp'
        ]

        headers = [
            'Node',
            'VRF',
            'State',
            'Routes',
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

    def print_protocol_ipv4_domain(self, info):
        order = [
            'name',
            'operSt',
            'routes_summary.count',
            'routes_summary.default',
            'routes_summary.direct',
            'routes_summary.local',
            'routes_summary.bgp',
            'routes_summary.ibgp',
            'routes_summary.ebgp'
        ]

        headers = [
            'VRF',
            'State',
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
            title='IPv4 VRF',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        self.print_protocol_ipv4_routes(
            info['routes']
        )

    def print_protocol_ipv4_routes(self, info):
        if info is None or len(info) == 0:
            self.my_output.default(
                'No IPv4 routes'
            )
            return

        order = [
            'pod_node_name',
            'vrf',
            'prefix',
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
            underline=True,
            table=True
        )

    def print_protocol_ipv4_routes_summary(self, info):
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
            title='IPv4 Routes Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
