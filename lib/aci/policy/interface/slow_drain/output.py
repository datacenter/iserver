class PolicyInterfaceSlowDrainOutput():
    def __init__(self):
        pass

    def print_policy_interface_slow_drain(self, info):
        self.print_policy_interface_slow_drain_properties(
            info
        )

        self.print_policy_interface_slow_drain_interfaces(
            info['l1RsQosSdIfPolCons']
        )

        self.print_policy_interface_slow_drain_references(
            info['relnFrom']
        )

    def print_policy_interface_slow_drain_properties(self, info):
        order = [
            'name',
            'tf',
            'congClearAction',
            'congDetectMult',
            'flushAdminSt',
            'flushIntvl',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Congestion Clear Action',
            'Congestion Detect Multiplier',
            'Flush Admin State',
            'Flush Timeout [msec]',
            'Interfaces',
            'Ref Policies'
        ]

        self.my_output.dictionary(
            info,
            title='Slow Drain Policy Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_policy_interface_slow_drain_interfaces(self, info):
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

    def print_policy_interface_slow_drain_references(self, info):
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

    def print_policies_interface_slow_drain_summary(self, info):
        order = [
            'name',
            'tfTick',
            'congClearAction',
            'congDetectMult',
            'flushAdminSt',
            'flushIntvl',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Congestion Clear Action',
            'Congestion Detect Multiplier',
            'Flush Admin State',
            'Flush Timeout [msec]',
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

    def print_policies_interface_slow_drain_usage(self, info):
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

    def print_policies_interface_slow_drain_interfaces(self, info):
        order = [
            'name',
            'l1RsQosSdIfPolCons.pod_node_name',
            'l1RsQosSdIfPolCons.interfaceId'
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
                ['l1RsQosSdIfPolCons']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
