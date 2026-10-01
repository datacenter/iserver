class K8sStorageProfileApi():
    def __init__(self):
        self.storage_profile_mo = None

    def get_storage_profile_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.storage_profile_mo
        )
        if cache_hit:
            return response

        response, self.storage_profile_mo = self.get_resources(
            'StorageProfile', 
            'cdi.kubevirt.io/v1beta1', 
            self.storage_profile_mo,
            name=name
        )

        return response