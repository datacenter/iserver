class K8sIntersightInfo():
    def __init__(self):
        self.intersight = None

    def get_intersight_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(managed_object)
        info['ucsTool'] = self.get(managed_object, 'spec:OsDiscoveryToolInstall', on_error=False, on_none=False)
        info = self.add_tick(
            info, 
            'status:phase', 
            'Ready', 
            'readyTick',
            bool_attribute='ready'
        )
        return info

    def get_intersights(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'intersight', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_any_intersight(self, cache_enabled=True):
        instances = self.get_intersights(cache_enabled=cache_enabled)
        if instances is None or len(instances) == 0:
            return False
        return True

    def is_intersight(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_intersight(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_intersight(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'intersight', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
