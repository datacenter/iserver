class PolicyGroupAccessInterfacePortOutput():
    def __init__(self):
        pass

    def print_policy_groups_access_interface_port_policies(self, info):
        order = [
            'name',
            'aaep_name',
            'policy.infraRsHIfPol',
            'policy.infraRsLinkFlapPol',
            'policy.infraRsCdpIfPol',
            'policy.infraRsMcpIfPol',
            'policy.infraRsLldpIfPol',
            'policy.infraRsStpIfPol',
            'policy.infraRsStormctrlIfPol'
        ]

        headers = [
            'Name',
            'Attached Entity Profile',
            'Link Level',
            'Link Flap',
            'CDP',
            'MCP',
            'LLDP',
            'STP',
            'Storm Control'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policy_groups_access_interface_port_aaep(self, info):
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
