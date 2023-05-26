class PolicyInterfacePortChannelOutput():
    def __init__(self):
        pass

    def print_policy_interface_port_channel(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'mode',
            'ctrlT',
            'minLinks',
            'maxLinks',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Mode',
            'Control',
            'Min Links',
            'Max Links',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'Port Channel Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_port_channel(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'mode',
            'ctrlT',
            'minLinks',
            'maxLinks'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Mode',
            'Control',
            'Min Links',
            'Max Links'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose,
            expand_lists=['ctrlT']
        )

    def print_policy_interface_port_channel_node(self, info):
        for item in info:
            if 'ctrlT' in item['policy']:
                item['ctrlT'] = item['policy']['ctrlT']
            else:
                item['ctrlT'] = []

        order = [
            'policy.name',
            'policy.mode',
            'ctrlT',
            'policy.minLinks',
            'policy.maxLinks'
        ]

        headers = [
            'Port Channel Policy Name',
            'Mode',
            'Control',
            'Min Links',
            'Max Links'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers,
            expand_lists=['ctrlT']
        )
