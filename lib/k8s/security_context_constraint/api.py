class K8sSecurityContextConstraintApi():
    def __init__(self):
        self.security_context_constraint_mo = None

    def get_security_context_constraint_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.security_context_constraint_mo
        )
        if cache_hit:
            return response

        response, self.security_context_constraint_mo = self.get_resources(
            'SecurityContextConstraints', 
            'security.openshift.io/v1', 
            self.security_context_constraint_mo,
            name=name
        )

        return response