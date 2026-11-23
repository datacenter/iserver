class K8sClusterQuotaApi():
    def __init__(self):
        self.cluster_quota_mo = None

    def get_cluster_quota_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.cluster_quota_mo
        )
        if cache_hit:
            return response

        response, self.cluster_quota_mo = self.get_resources(
            'ClusterResourceQuota', 
            'quota.openshift.io/v1', 
            self.cluster_quota_mo,
            name=name
        )

        return response