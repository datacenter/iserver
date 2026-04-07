class K8sRouteAdvertisementApi():
    def __init__(self):
        self.route_advertisement_mo = None

    def get_route_advertisement_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.route_advertisement_mo
        )
        if cache_hit:
            return response

        response, self.route_advertisement_mo = self.get_resources(
            'RouteAdvertisements', 
            'k8s.ovn.org/v1', 
            self.route_advertisement_mo,
            name=name
        )

        return response
    