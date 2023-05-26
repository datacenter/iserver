class PolicyInterfaceLinkLevelOutput():
    def __init__(self):
        pass

    def print_policy_interface_link_level(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'portPhyMediaType',
            'autoNeg',
            'speed',
            'dfeDelayMs',
            'linkDebounce',
            'fecMode',
            'emiRetrain',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'PHY Type',
            'Auto Neg',
            'Speed',
            'Delay [msec]',
            'Link Debounce [msec]',
            'FEC Mode',
            'EMI Retrain',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'Link Level Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_link_level(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'portPhyMediaType',
            'autoNeg',
            'speed',
            'dfeDelayMs',
            'linkDebounce',
            'fecMode',
            'emiRetrain'
        ]

        headers = [
            'Policy Name',
            'TF',
            'PHY Type',
            'Auto Neg',
            'Speed',
            'Delay [msec]',
            'Link Debounce [msec]',
            'FEC Mode',
            'EMI Retrain'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_link_level_node(self, info):
        order = [
            'policy.name',
            'policy.portPhyMediaType',
            'policy.autoNeg',
            'policy.speed',
            'policy.dfeDelayMs',
            'policy.linkDebounce',
            'policy.fecMode',
            'policy.emiRetrain'
        ]

        headers = [
            'Link Level Policy Name',
            'PHY Type',
            'Auto Neg',
            'Speed',
            'Delay [msec]',
            'Link Debounce [msec]',
            'FEC Mode',
            'EMI Retrain'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
