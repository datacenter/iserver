class K8sBgpPeerInfo():
    def __init__(self):
        self.bgp_peer = None

    def get_bgp_peer_info(self, managed_object):
        return self.get_base_info(managed_object)

    def get_bgp_peers(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'bgp_peer', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_bgp_peer(self, namespace, name, cache_enabled=True):
        if self.get_bgp_peer(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_bgp_peer(self, namespace, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'bgp_peer', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
