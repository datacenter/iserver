class K8sIsovalentBGPPeerConfigApi():
    def __init__(self):
        self.isovalent_bgp_peer_config_mo = None

    def get_isovalent_bgp_peer_config_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.isovalent_bgp_peer_config_mo
        )
        if cache_hit:
            return response

        response, self.isovalent_bgp_peer_config_mo = self.get_resources(
            'IsovalentBGPPeerConfig', 
            'isovalent.com/v1', 
            self.isovalent_bgp_peer_config_mo,
            name=name
        )

        return response

    def delete_isovalent_bgp_peer_config_mo(self, name):
        return self.delete_resource('IsovalentBGPPeerConfig', 'isovalent.com/v1', name)
