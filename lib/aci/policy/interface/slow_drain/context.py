class PolicyInterfaceSlowDrainContext():
    def __init__(self):
        pass

    def set_policy_interface_slow_drain_context(self, policies):
        # Interface
        # "podId": "1",
        # "nodeId": "2207",
        # "nodeName": "cl2207-eu-spdc",
        # "apic": "apic21",
        # "pod_node_name": "pod-1/cl2207-eu-spdc",
        # "interfaceId": "eth1/1/1",
        # "policyType": "qosSdIfPol",
        # "policyDn": "uni/infra/slow_drainIfP-k8s_slow_drain_enable",
        # "policyName": "k8s_slow_drain_enable"
        #
        # Context
        # "slow_drain": {
        #     "apic": [
        #         "apic11"
        #     ],
        #     "node": {
        #         "apic11": [
        #             "cl202-eu-spdc",
        #             "cl201-eu-spdc"
        #         ]
        #     },
        #     "interface": {
        #         "apic11": [
        #             "pod-1:node-202:eth1/61",
        #             "pod-1:node-201:eth1/61"
        #         ]
        #     }
        # }

        if policies is None or len(policies) == 0:
            return None

        intf_context = {}
        intf_context['apic'] = []
        intf_context['node'] = {}
        intf_context['interface'] = {}
        interface_count = 0

        for policy in policies:
            for interface_info in policy['l1RsQosSdIfPolCons']:
                if interface_info['apic'] not in intf_context['apic']:
                    intf_context['apic'].append(
                        interface_info['apic']
                    )
                    intf_context['node'][interface_info['apic']] = []
                    intf_context['interface'][interface_info['apic']] = []

                if interface_info['nodeName'] not in intf_context['node'][interface_info['apic']]:
                    intf_context['node'][interface_info['apic']].append(
                        interface_info['nodeName']
                    )

                interface_name = 'pod-%s:node-%s:%s' % (
                    interface_info['podId'],
                    interface_info['nodeId'],
                    interface_info['interfaceId']
                )
                if interface_name not in intf_context['interface'][interface_info['apic']]:
                    intf_context['interface'][interface_info['apic']].append(
                        interface_name
                    )
                    interface_count = interface_count + 1

        if interface_count == 0:
            return None

        success = self.context_handler.set(
            'pol-slow_drain-phy',
            intf_context
        )
        if not success:
            self.log.error(
                'set_policy_interface_slow_drain_context',
                'Context set failed'
            )

        success = self.context_handler.set(
            'phy',
            intf_context
        )
        if not success:
            self.log.error(
                'set_policy_interface_slow_drain_context',
                'Context set failed'
            )

        return 'phy'
