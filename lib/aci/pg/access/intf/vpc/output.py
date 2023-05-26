class PolicyGroupAccessInterfaceVpcOutput():
    def __init__(self):
        pass

    def print_policy_groups_access_interface_vpc_policies(self, info):
        order = [
            'name',
            'aaep_name',
            'policy.infraRsCdpIfPol',
            'policy.infraRsHIfPol',
            'policy.infraRsLldpIfPol',
            'policy.infraRsLacpPol',
            'policy.infraRsLinkFlapPol',
            'policy.infraRsMcpIfPol',
            'policy.infraRsStpIfPol',
            'policy.infraRsL2IfPol',
            'policy.infraRsStormctrlIfPol',
            'policy.infraRsL2PortSecurityPol'
        ]

        headers = [
            'Name',
            'Attached Entity Profile',
            'CDP',
            'Link Level',
            'LLDP',
            'LACP',
            'Link Flap',
            'MCP',
            'STP',
            'L2',
            'Storm Control',
            'Port Security'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policy_groups_access_interface_vpc_nodes(self, info):
        order = [
            'name',
            'aaep_name',
            'nodes.name'
        ]

        headers = [
            'Name',
            'Attached Entity Profile',
            'Deployed Node Name'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['nodes']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_policy_groups_access_interface_vpc_ports(self, info):
        order = [
            'name',
            'aaep_name',
            'ports.node_name',
            'ports.port_id'
        ]

        headers = [
            'Name',
            'Attached Entity Profile',
            'Deployed Node Name',
            'Deployed Port'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['ports']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_policy_groups_access_interface_vpc_aaep(self, info):
        order = [
            'name',
            'aaep_name',
            'infraRsDomP.domainType',
            'infraRsDomP.domainName'
        ]

        headers = [
            'Name',
            'Attached Entity Profile',
            'Domain Type',
            'Domain Name'
        ]

        for item in info:
            item['infraRsDomP'] = None
            if item['aaep'] is not None:
                item['infraRsDomP'] = item['aaep']['infraRsDomP']

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['infraRsDomP']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
