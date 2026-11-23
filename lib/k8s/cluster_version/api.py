class K8sClusterVersionApi():
    def __init__(self):
        self.cluster_version_mo = None
        
    def get_cluster_version_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.cluster_version_mo
        )
        if cache_hit:
            return response

        response, self.cluster_version_mo = self.get_resources(
            'ClusterVersion', 
            'config.openshift.io/v1', 
            self.cluster_version_mo,
            name=name
        )

        return response