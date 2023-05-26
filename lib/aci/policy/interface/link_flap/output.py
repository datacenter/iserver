class PolicyInterfaceLinkFlapOutput():
    def __init__(self):
        pass

    def print_policy_interface_link_flap(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'linkFlapErrorMax',
            'linkFlapErrorSeconds',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Max Flaps',
            'Max Flaps Duration [sec]',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'Link Flap Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_link_flap(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'linkFlapErrorMax',
            'linkFlapErrorSeconds'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Max Flaps',
            'Max Flaps Duration [sec]'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_link_flap_node(self, info):
        order = [
            'policy.name',
            'policy.linkFlapErrorMax',
            'policy.linkFlapErrorSeconds'
        ]

        headers = [
            'Link Flap Policy Name',
            'Max Flaps',
            'Max Flaps Duration [sec]'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
