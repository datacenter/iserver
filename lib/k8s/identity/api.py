class K8sIdentityApi():
    def __init__(self):
        self.identity_mo = None

    def get_identity_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.identity_mo
        )
        if cache_hit:
            return response

        response, self.identity_mo = self.get_resources(
            'Identity', 
            'user.openshift.io/v1', 
            self.identity_mo,
            name=name
        )

        return response
    
    def delete_identity_mo(self, name):
        return self.delete_resource('Identity', 'user.openshift.io/v1', name)
