class K8sNemoCustomizerInfo():
    def __init__(self):
        self.nemo_customizer = None

    def get_nemo_customizer_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_nemo_customizers(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'nemo_customizer', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_nemo_customizer(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'nemo_customizer', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_nemo_customizer(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_nemo_customizer(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_nemo_customizer(self, cache_enabled=True):
        infos = self.get_nemo_customizers(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True