class K8sUserDefinedNetworkApi():
    def __init__(self):
        self.user_defined_network_mo = None
        self.user_defined_network_namespace_mo = {}

    def get_user_defined_network_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.user_defined_network_mo,
            self.user_defined_network_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.user_defined_network_mo, self.user_defined_network_namespace_mo = self.get_namespaced_resources(
            'UserDefinedNetwork', 
            'k8s.ovn.org/v1', 
            self.user_defined_network_mo,
            self.user_defined_network_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_user_defined_network_mo(self, namespace, name):
        return self.delete_resource('UserDefinedNetwork', 'k8s.ovn.org/v1', name, namespace=namespace)