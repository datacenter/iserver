class K8sIsovalentBGPAdvertisementApi():
    def __init__(self):
        self.isovalent_bgp_advertisement_mo = None

    def get_isovalent_bgp_advertisement_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.isovalent_bgp_advertisement_mo
        )
        if cache_hit:
            return response

        response, self.isovalent_bgp_advertisement_mo = self.get_resources(
            'IsovalentBGPAdvertisement', 
            'isovalent.com/v1', 
            self.isovalent_bgp_advertisement_mo,
            name=name
        )

        return response
    
    def delete_isovalent_bgp_advertisement_mo(self, name):
        return self.delete_resource('IsovalentBGPAdvertisement', 'isovalent.com/v1', name)
