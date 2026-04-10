class K8sCommunityApi():
    def __init__(self):
        self.community_mo = None
        self.community_namespace_mo = {}

    def get_community_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.community_mo,
            self.community_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.community_mo, self.community_namespace_mo = self.get_namespaced_resources(
            'Community', 
            'metallb.io/v1beta1', 
            self.community_mo,
            self.community_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_community_mo(self, namespace, name):
        return self.delete_resource('Community', 'metallb.io/v1beta1', name, namespace=namespace)
