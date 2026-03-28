class K8sClusterUserDefinedNetworkApi():
    def __init__(self):
        self.cluster_user_defined_network_mo = None

    def get_cluster_user_defined_network_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.cluster_user_defined_network_mo
        )
        if cache_hit:
            return response

        response, self.cluster_user_defined_network_mo = self.get_resources(
            'ClusterUserDefinedNetwork', 
            'k8s.ovn.org/v1', 
            self.cluster_user_defined_network_mo,
            name=name
        )

        return response

    def delete_cluster_user_defined_network_mo(self, name):
        return self.delete_resource('ClusterUserDefinedNetwork', 'k8s.ovn.org/v1', name)