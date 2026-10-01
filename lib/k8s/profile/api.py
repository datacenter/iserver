class K8sProfileApi():
    def __init__(self):
        self.profile_mo = None
        self.profile_namespace_mo = {}

    def get_profile_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.profile_mo,
            self.profile_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.profile_mo, self.profile_namespace_mo = self.get_namespaced_resources(
            'Profile', 
            'tuned.openshift.io/v1', 
            self.profile_mo,
            self.profile_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response