class K8sTracingPolicyNamespacedApi():
    def __init__(self):
        self.tracing_policy_namespaced_mo = None
        self.tracing_policy_namespaced_namespace_mo = {}

    def get_tracing_policy_namespaced_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.tracing_policy_namespaced_mo,
            self.tracing_policy_namespaced_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.tracing_policy_namespaced_mo, self.tracing_policy_namespaced_namespace_mo = self.get_namespaced_resources(
            'TracingPolicyNamespaced', 
            'cilium.io/v1alpha1', 
            self.tracing_policy_namespaced_mo,
            self.tracing_policy_namespaced_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_tracing_policy_namespaced(self, namespace, name):
        success, _ = self.delete_resource('TracingPolicyNamespaced', 'cilium.io/v1alpha1', name, namespace=namespace)
        return success