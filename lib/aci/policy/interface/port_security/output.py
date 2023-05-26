class PolicyInterfacePortSecurityOutput():
    def __init__(self):
        pass

    def print_policy_interface_port_security(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'timeout',
            'maximum',
            'violation',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Timeout',
            'Maximum Endpoints',
            'Violation Action',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'Port Security Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_port_security(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'timeout',
            'maximum',
            'violation',
        ]

        headers = [
            'Policy Name',
            'TF',
            'Timeout',
            'Maximum Endpoints',
            'Violation Action'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_port_security_node(self, info):
        order = [
            'policy.name',
            'policy.timeout',
            'policy.maximum',
            'policy.violation',
        ]

        headers = [
            'Port Security Policy Name',
            'Timeout',
            'Maximum Endpoints',
            'Violation Action'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
