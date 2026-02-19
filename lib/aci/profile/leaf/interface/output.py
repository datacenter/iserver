class ProfileLeafInterfaceOutput():
    def __init__(self):
        pass

    def print_profiles_leaf_interface(self, info, title=False):
        if title:
            self.my_output.default(
                'Leaf Interfaces Profiles [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'selector.name',
            'selector.block',
            'selector.policyGroupType',
            'selector.policyGroupName'
        ]

        headers = [
            'Name',
            'Selector',
            'Block',
            'Policy Group Type',
            'Policy Group Name'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['selector']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_profiles_leaf_interface_usage(self, info, title=False):
        if title:
            self.my_output.default(
                'Leaf Interfaces Profiles - Usage [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'node_interfaces.podId',
            'node_interfaces.nodeId',
            'node_interfaces.interfaceId'
        ]

        headers = [
            'Name',
            'Pod',
            'Node',
            'Interface'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['node_interfaces'],
                cast_empty=True
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            cast_none=True,
            table=True
        )
