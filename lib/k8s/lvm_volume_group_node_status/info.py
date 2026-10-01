
class K8sLvmVolumeGroupNodeStatusInfo():
    def __init__(self):
        self.lvm_volume_group_node_status = None

    def get_lvm_volume_group_node_status_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        return info

    def get_lvm_volume_group_node_statuss(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'lvm_volume_group_node_status', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos