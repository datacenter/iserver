class K8sClusterPolicyApi():
    def __init__(self):
        self.cluster_policy_mo = None

    def get_cluster_policy_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.cluster_policy_mo
        )
        if cache_hit:
            return response

        response, self.cluster_policy_mo = self.get_resources(
            'ClusterPolicy', 
            'nvidia.com/v1', 
            self.cluster_policy_mo,
            name=name
        )

        return response
    
    def delete_cluster_policy_mo(self, name):
        success, _ = self.delete_resource('ClusterPolicy', 'nvidia.com/v1', name)
        return success