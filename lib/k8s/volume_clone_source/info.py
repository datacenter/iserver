class K8sVolumeCloneSourceInfo():
    def __init__(self):
        self.volume_clone_source = None

    def get_volume_clone_source_info(self, managed_object):
        return self.get_base_info(managed_object)
        
    def get_volume_clone_sources(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'volume_clone_source', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_volume_clone_source(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'volume_clone_source', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_volume_clone_source(self, name, cache_enabled=True, optimized=True):
        if self.get_volume_clone_source(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_volume_clone_source(self, cache_enabled=True):
        infos = self.get_volume_clone_sources(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True