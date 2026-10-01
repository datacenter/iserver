class K8sAuthApi():
    def __init__(self):
        self.auth_mo = None

    def get_auth_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.auth_mo
        )
        if cache_hit:
            return response

        response, self.auth_mo = self.get_resources(
            'Auth', 
            'services.platform.opendatahub.io/v1alpha1', 
            self.auth_mo,
            name=name
        )

        return response

    def delete_auth_mo(self, name):
        success, _ = self.delete_resource('Auth', 'services.platform.opendatahub.io/v1alpha1', name)
        return success