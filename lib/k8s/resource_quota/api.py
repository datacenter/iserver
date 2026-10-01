class K8sResourceQuotaApi():
    def __init__(self):
        self.resource_quota_mo = None
        self.resource_quota_namespace_mo = {}

    def get_resource_quota_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.resource_quota_mo,
            self.resource_quota_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.resource_quota_mo, self.resource_quota_namespace_mo = self.get_namespaced_resources(
            'ResourceQuota', 
            'v1', 
            self.resource_quota_mo,
            self.resource_quota_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response