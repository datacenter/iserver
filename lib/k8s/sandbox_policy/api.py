class K8sSandboxPolicyApi():
    def __init__(self):
        self.sandbox_policy_mo = None

    def get_sandbox_policy_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.sandbox_policy_mo
        )
        if cache_hit:
            return response

        response, self.sandbox_policy_mo = self.get_resources(
            'SandboxPolicy', 
            'cilium.io/v1alpha1', 
            self.sandbox_policy_mo,
            name=name
        )

        return response