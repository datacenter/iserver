class K8sStorageClientApi():
    def __init__(self):
        self.storage_client_mo = None

    def get_storage_client_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.storage_client_mo
        )
        if cache_hit:
            return response

        response, self.storage_client_mo = self.get_resources(
            'StorageClient', 
            'ocs.openshift.io/v1alpha1', 
            self.storage_client_mo,
            name=name
        )

        return response