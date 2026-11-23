class K8sStorageClaimApi():
    def __init__(self):
        self.storage_claim_mo = None

    def get_storage_claim_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.storage_claim_mo
        )
        if cache_hit:
            return response

        response, self.storage_claim_mo = self.get_resources(
            'StorageClaim', 
            'ocs.openshift.io/v1alpha1', 
            self.storage_claim_mo,
            name=name
        )

        return response