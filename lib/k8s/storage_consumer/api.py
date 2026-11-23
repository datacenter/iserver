class K8sStorageConsumerApi():
    def __init__(self):
        self.storage_consumer_mo = None
        self.storage_consumer_namespace_mo = {}

    def get_storage_consumer_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.storage_consumer_mo,
            self.storage_consumer_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.storage_consumer_mo, self.storage_consumer_namespace_mo = self.get_namespaced_resources(
            'StorageConsumer', 
            'ocs.openshift.io/v1alpha1', 
            self.storage_consumer_mo,
            self.storage_consumer_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response