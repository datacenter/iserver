class K8sPolicyBindingApi():
    def __init__(self):
        self.policy_binding_mo = None
        self.policy_binding_namespace_mo = {}

    def get_policy_binding_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.policy_binding_mo,
            self.policy_binding_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.policy_binding_mo, self.policy_binding_namespace_mo = self.get_namespaced_resources(
            'PolicyBinding', 
            'sts.min.io/v1beta1', 
            self.policy_binding_mo,
            self.policy_binding_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
    
    def delete_policy_binding_mo(self, namespace, name):
        success, _ = self.delete_resource('PolicyBinding', 'sts.min.io/v1beta1', name, namespace=namespace)
        return success