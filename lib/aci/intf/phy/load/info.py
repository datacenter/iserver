class InterfacePhyLoadInfo():
    def __init__(self):
        pass

    def get_interface_phy_load_info(self, managed_object):
        keys = [
            'loadIntvl1',
            'loadIntvl2',
            'loadIntvl3'
        ]

        info = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_interface_phy_load_stats(self, pod_id, node_id, interface_id):
        managed_object = self.get_interface_phy_load_mo(pod_id, node_id, interface_id)
        if managed_object is None:
            return None
        return self.get_interface_phy_load_info(managed_object)
