class PolicyInterfaceSlowDrainOutput():
    def __init__(self):
        pass

    def print_policy_interface_slow_drain(self, info, verbose=False):
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

        self.print_policy_interface(
            info,
            'Slow Drain Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_slow_drain(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'congClearAction',
            'congDetectMult',
            'flushAdminSt',
            'flushIntvl'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Action',
            'Multiplier',
            'Admin State',
            'Flush Timeout [msec]'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_slow_drain_node(self, info):
        order = [
            'policy.name',
            'policy.congClearAction',
            'policy.congDetectMult',
            'policy.flushAdminSt',
            'policy.flushIntvl'
        ]

        headers = [
            'Link Flap Policy Name',
            'Action',
            'Multiplier',
            'Admin State',
            'Flush Timeout [msec]'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
