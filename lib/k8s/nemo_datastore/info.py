class K8sNemoDatastoreInfo():
    def __init__(self):
        self.nemo_datastore = None

    def get_nemo_datastore_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_nemo_datastores(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'nemo_datastore', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_nemo_datastore(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'nemo_datastore', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_nemo_datastore(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_nemo_datastore(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_nemo_datastore(self, cache_enabled=True):
        infos = self.get_nemo_datastores(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True