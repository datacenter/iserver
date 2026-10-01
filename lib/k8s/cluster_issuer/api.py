class K8sClusterIssuerApi():
    def __init__(self):
        self.cluster_issuer_mo = None

    def get_cluster_issuer_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.cluster_issuer_mo
        )
        if cache_hit:
            return response

        response, self.cluster_issuer_mo = self.get_resources(
            'ClusterIssuer', 
            'cert-manager.io/v1', 
            self.cluster_issuer_mo,
            name=name
        )

        return response
    
    def delete_cluster_issuer_mo(self, name):
        success, _ = self.delete_resource('ClusterIssuer', 'cert-manager.io/v1', name)
        return success