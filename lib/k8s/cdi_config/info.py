class K8sCdiConfigInfo():
    def __init__(self):
        self.cdi_config = None

    def get_cdi_config_info(self, managed_object):
        return self.get_base_info(managed_object)

    def get_cdi_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'cdi_config', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_cdi_config(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'cdi_config', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_cdi_config(self, name, cache_enabled=True, optimized=True):
        if self.get_cdi_config(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_cdi_config(self, cache_enabled=True):
        infos = self.get_cdi_configs(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True