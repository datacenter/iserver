from lib import filter_helper


class K8sVolumeSnapshotClassInfo():
    def __init__(self):
        self.volume_snapshot_class = None

    def get_volume_snapshot_class_info(self, managed_object):
        return self.get_base_info(managed_object)
        
    def get_volume_snapshot_classs(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'volume_snapshot_class', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_volume_snapshot_class(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'volume_snapshot_class', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_volume_snapshot_class(self, name, cache_enabled=True, optimized=True):
        if self.get_volume_snapshot_class(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_volume_snapshot_class(self, cache_enabled=True):
        infos = self.get_volume_snapshot_classs(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True