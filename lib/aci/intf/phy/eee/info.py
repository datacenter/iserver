class InterfacePhyEeeInfo():
    def __init__(self):
        pass

    def get_interface_phy_eee_info(self, managed_object):
        keys = [
            'eeeLat',
            'eeeLpi',
            'eeeState'
        ]

        info = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_interface_phy_eee_stats(self, pod_id, node_id, interface_id):
        managed_object = self.get_interface_phy_eee_mo(pod_id, node_id, interface_id)
        if managed_object is None:
            return None
        return self.get_interface_phy_eee_info(managed_object)
