class K8sVolumeImportSourceInfo():
    def __init__(self):
        self.volume_import_source = None

    def get_volume_import_source_info(self, managed_object):
        return self.get_base_info(managed_object)
        
    def get_volume_import_sources(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'volume_import_source', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_volume_import_source(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'volume_import_source', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_volume_import_source(self, name, cache_enabled=True, optimized=True):
        if self.get_volume_import_source(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_volume_import_source(self, cache_enabled=True):
        infos = self.get_volume_import_sources(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True