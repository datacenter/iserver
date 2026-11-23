class K8sStorageMapApi():
    def __init__(self):
        self.storage_map_mo = None
        self.storage_map_namespace_mo = {}

    def get_storage_map_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.storage_map_mo,
            self.storage_map_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.storage_map_mo, self.storage_map_namespace_mo = self.get_namespaced_resources(
            'StorageMap', 
            'forklift.konveyor.io/v1beta1', 
            self.storage_map_mo,
            self.storage_map_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_storage_map_mo(self, namespace, name):
        success, _ = self.delete_resource('StorageMap', 'forklift.konveyor.io/v1beta1', name, namespace=namespace)
        return success