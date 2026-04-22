class K8sClusterwidePrivateNetworkApi():
    def __init__(self):
        self.clusterwide_private_network_mo = None

    def get_clusterwide_private_network_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.clusterwide_private_network_mo
        )
        if cache_hit:
            return response

        response, self.clusterwide_private_network_mo = self.get_resources(
            'ClusterwidePrivateNetwork', 
            'isovalent.com/v1alpha1', 
            self.clusterwide_private_network_mo,
            name=name
        )

        return response

    def delete_clusterwide_private_network_mo(self, name):
        return self.delete_resource('ClusterwidePrivateNetwork', 'isovalent.com/v1alpha1', name)