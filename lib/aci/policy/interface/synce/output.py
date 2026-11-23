class PolicyInterfaceSynceOutput():
    def __init__(self):
        pass

    def print_policy_interface_synce(self, info):
        self.print_policy_interface_synce_properties(
            info
        )

        self.print_policy_interface_synce_interfaces(
            info['l1RsSynceEthIfPolCons']
        )

        self.print_policy_interface_synce_references(
            info['relnFrom']
        )

    def print_policy_interface_synce_properties(self, info):
        order = [
            'name',
            'tf',
            'adminSt',
            'selinput',
            'srcpriority',
            'ssm',
            'wtr',
            'qlrcvlval',
            'qlrcvexactval',
            'qlrcvhval',
            'qltxlval',
            'qltxexactval',
            'qltxhval'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Input Selection',
            'Source Priority',
            'Sync Status Msg',
            'Wait-To-Restore',
            'Rx Qual Min',
            'Rx Qual Eq',
            'Rx Qual Max',
            'Tx Qual Min',
            'Tx Qual Eq',
            'Tx Qual Max'
        ]

        self.my_output.dictionary(
            info,
            title='SyncE Policy Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_policy_interface_synce_interfaces(self, info):
        if info is None or len(info) == 0:
            return

        order = [
            'pod_node_name',
            'interfaceId'
        ]

        headers = [
            'Node',
            'Interface'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policy_interface_synce_references(self, info):
        if info is None or len(info) == 0:
            return

        order = [
            'policyName',
            'policyType',
            'tCl'
        ]

        headers = [
            'Policy Name',
            'Policy Type',
            'Policy Class'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policies_interface_synce_summary(self, info):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'selinput',
            'srcpriority',
            'ssm',
            'wtr',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Input Selection',
            'Source Priority',
            'Sync Status Msg',
            'Wait-To-Restore',
            'Interfaces',
            'Ref Policies'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policies_interface_synce_usage(self, info):
        order = [
            'name',
            'nodeInterfaces.pod_node_name',
            'nodeInterfaces.interfaces',
            'relnFrom.policyType',
            'relnFrom.policyName'
        ]

        headers = [
            'Policy Name',
            'Node',
            'Interface Count',
            'Ref Policy Type',
            'Ref Policy Name'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['nodeInterfaces', 'relnFrom']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policies_interface_synce_interfaces(self, info):
        order = [
            'name',
            'l1RsSynceEthIfPolCons.pod_node_name',
            'l1RsSynceEthIfPolCons.interfaceId'
        ]

        headers = [
            'Policy Name',
            'Node',
            'Interface'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['l1RsSynceEthIfPolCons']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
