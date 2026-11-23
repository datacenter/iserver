class InterfacePortChannelMembers():
    def __init__(self):
        pass

    def get_interface_port_channel_member_phy_info(self, pod_id, node_id, member_info):
        inteface_phy_info = self.get_interface_phy(
            pod_id,
            node_id,
            member_info['tSKey']
        )
        if inteface_phy_info is not None:
            member_info['adminSt'] = inteface_phy_info['adminSt']
            member_info['__Output']['adminSt'] = inteface_phy_info['__Output']['adminSt']
            member_info['operSt'] = inteface_phy_info['stats']['operSt']
            member_info['__Output']['operSt'] = inteface_phy_info['__Output']['stats.operSt']
            member_info['operMode'] = inteface_phy_info['stats']['operMode']
            member_info['operDuplex'] = inteface_phy_info['stats']['operDuplex']
            member_info['operSpeed'] = inteface_phy_info['stats']['operSpeed']
            member_info['operVlans'] = inteface_phy_info['stats']['operVlans']

        return member_info

    def get_interface_port_channel_lacp_members(self, pod_id, node_id, interface_info):
        lacp_members = []
        for member_info in interface_info['member']:
            lacp_info = {}
            lacp_info['__Output'] = {}
            lacp_info['pod_node_name'] = interface_info['pod_node_name']
            lacp_info['id'] = interface_info['id']
            lacp_info['__Output']['id'] = interface_info['__Output']['id']
            lacp_info['isActiveMemberTick'] = member_info['isActiveMemberTick']
            lacp_info['__Output']['isActiveMemberTick'] = member_info['__Output']['isActiveMemberTick']

            lacp_info['adjacency'] = self.get_lacp_adjacency_endpoint(
                pod_id,
                node_id,
                member_info['tSKey'],
                allow_multiple=False
            )

            lacp_info['local'] = self.get_interface_lacp(
                pod_id,
                node_id,
                interface_filter=['id:%s' % (member_info['tSKey'])]
            )[0]
            lacp_info['local'] = self.my_output.merge_output(
                lacp_info['local']
            )

            lacp_info['stats'] = self.get_interface_lacp_stats(
                pod_id,
                node_id,
                member_info['tSKey']
            )
            lacp_info['stats'] = self.my_output.merge_output(
                lacp_info['stats']
            )

            lacp_members.append(
                lacp_info
            )

        return lacp_members
