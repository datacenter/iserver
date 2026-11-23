class K8sNetworkMapApi():
    def __init__(self):
        self.network_map_mo = None
        self.network_map_namespace_mo = {}

    def get_network_map_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.network_map_mo,
            self.network_map_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.network_map_mo, self.network_map_namespace_mo = self.get_namespaced_resources(
            'NetworkMap', 
            'forklift.konveyor.io/v1beta1', 
            self.network_map_mo,
            self.network_map_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
    
    def delete_network_map_mo(self, namespace, name):
        success, _ = self.delete_resource('NetworkMap', 'forklift.konveyor.io/v1beta1', name, namespace=namespace)
        return success