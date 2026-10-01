class K8sAaqApi():
    def __init__(self):
        self.aaq_mo = None

    def get_aaq_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.aaq_mo
        )
        if cache_hit:
            return response

        response, self.aaq_mo = self.get_resources(
            'AAQ', 
            'aaq.kubevirt.io/v1alpha1', 
            self.aaq_mo,
            name=name
        )

        return response