class InterfacePortChannelRelationsInfo():
    def __init__(self):
        pass

    def get_interface_port_channel_relations_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_interface_port_channel_relations(self, pod_id, node_id, port_channel_id):
        managed_object = self.get_interface_port_channel_relations_mo(
            pod_id,
            node_id,
            port_channel_id
        )
        if managed_object is None:
            return None

        return self.get_interface_port_channel_relations_info(managed_object)
