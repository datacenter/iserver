class K8sInfrastructureConfigApi():
    def __init__(self):
        self.infrastructure_config_mo = None

    def get_infrastructure_config_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.infrastructure_config_mo
        )
        if cache_hit:
            return response

        response, self.infrastructure_config_mo = self.get_resources(
            'Infrastructure', 
            'config.openshift.io/v1', 
            self.infrastructure_config_mo,
            name=name
        )

        return response