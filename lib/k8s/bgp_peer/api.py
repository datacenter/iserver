class K8sBgpPeerApi():
    def __init__(self):
        self.bgp_peer_mo = None
        self.bgp_peer_namespace_mo = {}

    def get_bgp_peer_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.bgp_peer_mo,
            self.bgp_peer_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.bgp_peer_mo, self.bgp_peer_namespace_mo = self.get_namespaced_resources(
            'BGPPeer', 
            'metallb.io/v1beta2', 
            self.bgp_peer_mo,
            self.bgp_peer_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_bgp_peer_mo(self, namespace, name):
        return self.delete_resource('BGPPeer', 'metallb.io/v1beta2', name, namespace=namespace)
