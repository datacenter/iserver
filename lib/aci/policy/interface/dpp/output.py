class PolicyInterfaceDppOutput():
    def __init__(self):
        pass

    def print_policy_interface_dpp(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'adminSt',
            'type',
            'conformAction',
            'violateAction',
            'sharingMode',
            'burstT',
            'beT',
            'rateT',
            'pirT',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Type',
            'Conform Action',
            'Violate Action',
            'Sharing Mode',
            'Burst',
            'Excessive Burst',
            'Rate',
            'Peak Rate',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'Data Plane Policing Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_dpp(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'type',
            'conformAction',
            'violateAction',
            'sharingMode',
            'burstT',
            'beT',
            'rateT',
            'pirT'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Type',
            'Conform Action',
            'Violate Action',
            'Sharing Mode',
            'Burst',
            'Excessive Burst',
            'Rate',
            'Peak Rate'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_dpp_node(self, info):
        order = [
            'policy.name',
            'policy.adminSt',
            'policy.type',
            'policy.conformAction',
            'policy.violateAction',
            'policy.sharingMode',
            'policy.burstT',
            'policy.beT',
            'policy.rateT',
            'policy.pirT'
        ]

        headers = [
            'DPP Policy Name',
            'Admin State',
            'Type',
            'Conform Action',
            'Violate Action',
            'Sharing Mode',
            'Burst',
            'Excessive Burst',
            'Rate',
            'Peak Rate'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
