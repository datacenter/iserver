class InterfacePhyCapInfo():
    def __init__(self):
        pass

    def get_interface_phy_cap_info(self, managed_object):
        keys = [
            'mdix',
            'speed'
        ]

        info = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_interface_phy_cap_stats(self, pod_id, node_id, interface_id):
        managed_object = self.get_interface_phy_cap_mo(pod_id, node_id, interface_id)
        if managed_object is None:
            return None
        return self.get_interface_phy_cap_info(managed_object)
