class PolicyInterfaceLinkLevelContext():
    def __init__(self):
        pass

    def set_policy_interface_link_level_context(self, policies):
        if policies is None or len(policies) == 0:
            return None

        intf_context = {}
        intf_context['apic'] = []
        intf_context['node'] = {}
        intf_context['interface'] = {}
        interface_count = 0

        for policy in policies:
            for interface_info in policy['l1RsHIfPolCons']:
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
            'pol-link_level-phy',
            intf_context
        )
        if not success:
            self.log.error(
                'set_policy_interface_link_level_context',
                'Context set failed'
            )

        success = self.context_handler.set(
            'phy',
            intf_context
        )
        if not success:
            self.log.error(
                'set_policy_interface_link_level_context',
                'Context set failed'
            )

        return 'phy'
