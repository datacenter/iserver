class InterfacePhyRmonStatsInfo():
    def __init__(self):
        pass

    def get_interface_phy_rmon_stats_info(self, managed_object):
        info = {}
        for key in managed_object:
            info[key] = managed_object[key]
        return info

    def get_interface_phy_rmon_stats(self, pod_id, node_id, interface_id):
        managed_object = self.get_interface_phy_rmon_stats_mo(pod_id, node_id, interface_id)
        if managed_object is None:
            return None
        return self.get_interface_phy_rmon_stats_info(managed_object)
