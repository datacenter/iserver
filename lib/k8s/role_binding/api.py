class K8sRoleBindingApi():
    def __init__(self):
        self.role_binding_mo = None
        self.role_binding_namespace_mo = {}

    def get_role_binding_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.role_binding_mo,
            self.role_binding_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.role_binding_mo, self.role_binding_namespace_mo = self.get_namespaced_resources(
            'RoleBinding', 
            'rbac.authorization.k8s.io/v1', 
            self.role_binding_mo,
            self.role_binding_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_role_binding_mo(self, namespace, name):
        success, _ = self.delete_resource('RoleBinding', 'rbac.authorization.k8s.io/v1', name, namespace=namespace)
        return success