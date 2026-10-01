class K8sDnsApi():
    def __init__(self):
        self.dns_mo = None

    def get_dns_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.dns_mo
        )
        if cache_hit:
            return response

        response, self.dns_mo = self.get_resources(
            'DNS', 
            'config.openshift.io/v1', 
            self.dns_mo,
            name=name
        )

        return response