class K8sVolumeSnapshotContentInfo():
    def __init__(self):
        self.volume_snapshot_content = None

    def get_volume_snapshot_content_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_volume_snapshot_contents(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'volume_snapshot_content', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_volume_snapshot_content(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'volume_snapshot_content', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_volume_snapshot_content(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_volume_snapshot_content(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_volume_snapshot_content(self, cache_enabled=True):
        infos = self.get_volume_snapshot_contents(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True