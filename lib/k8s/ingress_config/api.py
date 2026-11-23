class K8sIngressConfigApi():
    def __init__(self):
        self.ingress_config_mo = None

    def get_ingress_config_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.ingress_config_mo
        )
        if cache_hit:
            return response

        response, self.ingress_config_mo = self.get_resources(
            'Ingress', 
            'config.openshift.io/v1', 
            self.ingress_config_mo,
            name=name
        )

        return response