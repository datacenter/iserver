class K8sBuildConfigInfo():
    def __init__(self):
        self.build_config = None

    def get_build_config_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(managed_object)
        info['type'] = self.get(managed_object, 'spec:source:type')
        info['ref'] = self.get(managed_object, 'spec:source:git:ref')
        info['uri'] = self.get(managed_object, 'spec:source:git:uri')
        return info

    def get_build_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'build_config', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_build_config(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'build_config', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_build_config(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_build_config(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_build_config(self, cache_enabled=True):
        infos = self.get_build_configs(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True