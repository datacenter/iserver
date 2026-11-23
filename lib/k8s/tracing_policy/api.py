class K8sTracingPolicyApi():
    def __init__(self):
        self.tracing_policy_mo = None

    def get_tracing_policy_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.tracing_policy_mo
        )
        if cache_hit:
            return response

        response, self.tracing_policy_mo = self.get_resources(
            'TracingPolicy', 
            'cilium.io/v1alpha1', 
            self.tracing_policy_mo,
            name=name
        )

        return response