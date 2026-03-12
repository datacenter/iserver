class K8sAuthenticationApi():
    def __init__(self):
        self.authentication_mo = None

    def get_authentication_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.authentication_mo
        )
        if cache_hit:
            return response

        response, self.authentication_mo = self.get_resources(
            'Authentication', 
            'operator.openshift.io/v1', 
            self.authentication_mo,
            name=name
        )

        return response
