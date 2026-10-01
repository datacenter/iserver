class K8sPrivateNetworkEndpointSliceApi():
    def __init__(self):
        self.private_network_endpoint_slice_mo = None
        self.private_network_endpoint_slice_namespace_mo = {}

    def get_private_network_endpoint_slice_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.private_network_endpoint_slice_mo,
            self.private_network_endpoint_slice_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.private_network_endpoint_slice_mo, self.private_network_endpoint_slice_namespace_mo = self.get_namespaced_resources(
            'PrivateNetworkEndpointSlice', 
            'isovalent.com/v1alpha1', 
            self.private_network_endpoint_slice_mo,
            self.private_network_endpoint_slice_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_private_network_endpoint_slice_mo(self, namespace, name):
        success, _ = self.delete_resource('PrivateNetworkEndpointSlice', 'isovalent.com/v1alpha1', name, namespace=namespace)
        return success