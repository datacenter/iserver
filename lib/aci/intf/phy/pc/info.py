class InterfacePhyPcInfo():
    def __init__(self):
        pass

    def get_interface_phy_pc_info(self, managed_object):
        keys = [
            'channelingSt'
        ]

        info = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_interface_phy_pc_stats(self, pod_id, node_id, interface_id):
        managed_object = self.get_interface_phy_pc_mo(pod_id, node_id, interface_id)
        if managed_object is None:
            return None
        return self.get_interface_phy_pc_info(managed_object)
