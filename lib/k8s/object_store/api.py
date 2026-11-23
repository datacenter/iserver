class K8sObjectStoreApi():
    def __init__(self):
        self.object_store_mo = None
        self.object_store_namespace_mo = {}

    def get_object_store_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.object_store_mo,
            self.object_store_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.object_store_mo, self.object_store_namespace_mo = self.get_namespaced_resources(
            'ObjectStore', 
            'aistor.min.io/v1', 
            self.object_store_mo,
            self.object_store_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
        
    def delete_object_store_mo(self, namespace, name):
        success, _ = self.delete_resource('ObjectStore', 'aistor.min.io/v1', name, namespace=namespace)
        return success