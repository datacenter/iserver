class K8sBgpAdvertisementApi():
    def __init__(self):
        self.bgp_advertisement_mo = None
        self.bgp_advertisement_namespace_mo = {}

    def get_bgp_advertisement_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.bgp_advertisement_mo,
            self.bgp_advertisement_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.bgp_advertisement_mo, self.bgp_advertisement_namespace_mo = self.get_namespaced_resources(
            'BGPAdvertisement', 
            'metallb.io/v1beta1', 
            self.bgp_advertisement_mo,
            self.bgp_advertisement_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_bgp_advertisement_mo(self, namespace, name):
        return self.delete_resource('BGPAdvertisement', 'metallb.io/v1beta1', name, namespace=namespace)
