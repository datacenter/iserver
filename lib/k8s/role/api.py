class K8sRoleApi():
    def __init__(self):
        self.role_mo = None
        self.role_namespace_mo = {}

    def get_role_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.role_mo,
            self.role_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.role_mo, self.role_namespace_mo = self.get_namespaced_resources(
            'Role', 
            'rbac.authorization.k8s.io/v1', 
            self.role_mo,
            self.role_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response