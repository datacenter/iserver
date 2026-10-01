class K8sStorageRequestApi():
    def __init__(self):
        self.storage_request_mo = None
        self.storage_request_namespace_mo = {}

    def get_storage_request_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.storage_request_mo,
            self.storage_request_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.storage_request_mo, self.storage_request_namespace_mo = self.get_namespaced_resources(
            'StorageRequest', 
            'ocs.openshift.io/v1alpha1', 
            self.storage_request_mo,
            self.storage_request_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response