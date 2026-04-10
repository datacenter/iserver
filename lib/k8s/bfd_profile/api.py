class K8sBfdProfileApi():
    def __init__(self):
        self.bfd_profile_mo = None
        self.bfd_profile_namespace_mo = {}

    def get_bfd_profile_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.bfd_profile_mo,
            self.bfd_profile_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.bfd_profile_mo, self.bfd_profile_namespace_mo = self.get_namespaced_resources(
            'BFDProfile', 
            'metallb.io/v1beta1', 
            self.bfd_profile_mo,
            self.bfd_profile_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_bfd_profile_mo(self, namespace, name):
        return self.delete_resource('BFDProfile', 'metallb.io/v1beta1', name, namespace=namespace)
