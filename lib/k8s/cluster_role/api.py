class K8sClusterRoleApi():
    def __init__(self):
        self.cluster_role_mo = None

    def get_cluster_role_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.cluster_role_mo
        )
        if cache_hit:
            return response

        response, self.cluster_role_mo = self.get_resources(
            'ClusterRole', 
            'rbac.authorization.k8s.io/v1', 
            self.cluster_role_mo,
            name=name
        )

        return response

    def delete_cluster_role_mo(self, name):
        return self.delete_resource('ClusterRole', 'rbac.authorization.k8s.io/v1', name)
    