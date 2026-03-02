class K8sVastStorageApi():
    def __init__(self):
        self.vast_storage_mo = None
        self.vast_storage_namespace_mo = {}

    def get_vast_storage_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.vast_storage_mo,
            self.vast_storage_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.vast_storage_mo, self.vast_storage_namespace_mo = self.get_namespaced_resources(
            'VastStorage', 
            'storage.vastdata.com/v1', 
            self.vast_storage_mo,
            self.vast_storage_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_vast_storage_mo(self, namespace, name):
        return self.delete_resource('VastStorage', 'storage.vastdata.com/v1', name, namespace=namespace)