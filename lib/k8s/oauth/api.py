class K8sOAuthApi():
    def __init__(self):
        self.oauth_mo = None

    def get_oauth_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.oauth_mo
        )
        if cache_hit:
            return response

        response, self.oauth_mo = self.get_resources(
            'OAuth', 
            'config.openshift.io/v1', 
            self.oauth_mo,
            name=name
        )

        return response
