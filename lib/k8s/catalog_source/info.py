class K8sCatalogSourceInfo():
    def __init__(self):
        self.catalog_source = None

    def get_catalog_source_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(managed_object)
        info['display_name'] = self.get(managed_object, 'spec:displayName')
        return info

    def get_catalog_sources(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'catalog_source', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_catalog_source(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'catalog_source', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_catalog_source(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_catalog_source(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_catalog_source(self, cache_enabled=True):
        infos = self.get_catalog_sources(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True