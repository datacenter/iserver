class K8sCniApi():
    def __init__(self):
        self.cni_mo = None

    def get_cni_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.cni_mo
        )
        if cache_hit:
            return response

        response, self.cni_mo = self.get_resources(
            'Network', 
            'config.openshift.io/v1', 
            self.cni_mo,
            name=name
        )

        return response