class PolicyGeneralAaeOutput():
    def __init__(self):
        pass

    def print_policies_global_aae(self, info, verbose=False):
        if len(info) == 0:
            self.my_output.default('No policy found')
            return

        if verbose:
            for item in info:
                self.print_policy_global_aae(item)
            return

        order = [
            'name',
            'infraVlanEnabledTick',
            'infraRsDomP.domainName',
            'infraRsDomP.domainType',
            'infraRsDomP.state',
            'infraRtAttEntP.name',
            'infraRtAttEntP.typeName'
        ]

        headers = [
            'Attachable Access Entity Profile',
            'Infra VLAN',
            'Domain Name',
            'Domain Type',
            'Domain State',
            'Policy Group Name',
            'Policy Group Interface Type'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['infraRsDomP', 'infraRtAttEntP']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
