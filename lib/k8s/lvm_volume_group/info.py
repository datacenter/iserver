
class K8sLvmVolumeGroupInfo():
    def __init__(self):
        self.lvm_volume_group = None

    def get_lvm_volume_group_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        return info

    def get_lvm_volume_groups(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'lvm_volume_group', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos