class K8sNemoEntitystoreInfo():
    def __init__(self):
        self.nemo_entitystore = None

    def get_nemo_entitystore_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_nemo_entitystores(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'nemo_entitystore', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_nemo_entitystore(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'nemo_entitystore', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_nemo_entitystore(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_nemo_entitystore(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_nemo_entitystore(self, cache_enabled=True):
        infos = self.get_nemo_entitystores(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True