class InterfacePortChannelMembers():
    def __init__(self):
        pass

    def get_interface_port_channel_lacp_members(self, pod_id, node_id, port_ids):
        lacp_members = []
        for port_id in port_ids:
            lacp_info = self.get_lacp_adjacency_endpoint(
                pod_id,
                node_id,
                port_id,
                allow_multiple=False
            )

            if lacp_info is None:
                continue

            lacp_info['local'] = self.get_interface_lacp(
                pod_id,
                node_id,
                interface_filter=['id:%s' % (port_id)]
            )
            lacp_info['local'] = self.my_output.merge_output(
                lacp_info['local']
            )

            lacp_info['stats'] = self.get_interface_lacp_stats(
                pod_id,
                node_id,
                port_id
            )
            lacp_info['stats'] = self.my_output.merge_output(
                lacp_info['stats']
            )

            lacp_members.append(
                lacp_info
            )

        return lacp_members
