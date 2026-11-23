class K8sSandboxPolicyNamespacedApi():
    def __init__(self):
        self.sandbox_policy_namespaced_mo = None
        self.sandbox_policy_namespaced_namespace_mo = {}

    def get_sandbox_policy_namespaced_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.sandbox_policy_namespaced_mo,
            self.sandbox_policy_namespaced_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.sandbox_policy_namespaced_mo, self.sandbox_policy_namespaced_namespace_mo = self.get_namespaced_resources(
            'SandboxPolicyNamespaced', 
            'cilium.io/v1alpha1', 
            self.sandbox_policy_namespaced_mo,
            self.sandbox_policy_namespaced_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response