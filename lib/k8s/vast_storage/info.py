import yaml


class K8sVastStorageInfo():
    def __init__(self):
        self.vast_storage = None

    def get_vast_storage_info(self, managed_object):
        return self.get_vast_managed_object_info(managed_object)

    def get_vast_storages(self, object_filter=None, return_mo=False, cache_enabled=True):
        return self.get_infos(
            'vast_storage', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

    def is_vast_storage(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_vast_storage(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_vast_storage(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'vast_storage', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
    