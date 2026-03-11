class K8sGroupApi():
    def __init__(self):
        self.group_mo = None

    def get_group_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.group_mo
        )
        if cache_hit:
            return response

        response, self.group_mo = self.get_resources(
            'Group', 
            'user.openshift.io/v1', 
            self.group_mo,
            name=name
        )

        return response
    
    def delete_group_mo(self, name):
        return self.delete_resource('User', 'user.openshift.io/v1', name)
