class K8sStorageClusterPeerApi():
    def __init__(self):
        self.storage_cluster_peer_mo = None
        self.storage_cluster_peer_namespace_mo = {}

    def get_storage_cluster_peer_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.storage_cluster_peer_mo,
            self.storage_cluster_peer_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.storage_cluster_peer_mo, self.storage_cluster_peer_namespace_mo = self.get_namespaced_resources(
            'StorageClusterPeer', 
            'ocs.openshift.io/v1', 
            self.storage_cluster_peer_mo,
            self.storage_cluster_peer_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response