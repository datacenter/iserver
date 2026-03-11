class K8sUserApi():
    def __init__(self):
        self.user_mo = None

    def get_user_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.user_mo
        )
        if cache_hit:
            return response

        response, self.user_mo = self.get_resources(
            'User', 
            'user.openshift.io/v1', 
            self.user_mo,
            name=name
        )

        return response
    
    def delete_user_mo(self, name):
        return self.delete_resource('User', 'user.openshift.io/v1', name)
