class InterfacePolicyGroupInfo():
    def __init__(self):
        pass

    def get_interface_policy_group_selector(self, pod_id, node_id, interface_id, group_info=False):
        node_profiles = self.get_node_interface_policy_profiles(pod_id, node_id)
        if node_profiles is None:
            return None

        for node_profile in node_profiles:
            selector_info = self.get_interface_policy_profile_selectors(node_profile['name'], interface_id)
            if selector_info is not None:
                if group_info:
                    selector_info['policy_group_info'] = None

                    if selector_info['policy_group_type'] == 'infraAccBndlGrp':
                        info = self.get_policy_groups_access_interface_vpc(
                            policy_group_filter=['name:%s' % (selector_info['policy_group_name'])],
                            aaep_info=True
                        )
                        if info is not None and len(info) == 1:
                            selector_info['policy_group_info'] = info[0]

                    if selector_info['policy_group_type'] == 'infraAccPortGrp':
                        info = self.get_policy_groups_access_interface_port(
                            policy_group_filter=['name:%s' % (selector_info['policy_group_name'])],
                            aaep_info=True
                        )
                        if info is not None and len(info) == 1:
                            selector_info['policy_group_info'] = info[0]

                    if selector_info['policy_group_type'] == 'infraBrkoutPortGrp':
                        info = self.get_policy_groups_access_interface_breakout(
                            policy_group_filter=['name:%s' % (selector_info['policy_group_name'])]
                        )
                        if info is not None and len(info) == 1:
                            selector_info['policy_group_info'] = info[0]

                    if selector_info['policy_group_type'] not in ['infraAccBndlGrp', 'infraAccPortGrp', 'infraBrkoutPortGrp']:
                        self.log.error(
                            'get_interface_policy_group_selector',
                            'Unsupported: %s' % (selector_info['policy_group_type'])
                        )

                return selector_info

        return None
