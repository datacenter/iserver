class K8sFrrConfigurationApi():
    def __init__(self):
        self.frr_configuration_mo = None
        self.frr_configuration_namespace_mo = {}

    def get_frr_configuration_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.frr_configuration_mo,
            self.frr_configuration_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.frr_configuration_mo, self.frr_configuration_namespace_mo = self.get_namespaced_resources(
            'FRRConfiguration', 
            'frrk8s.metallb.io/v1beta1', 
            self.frr_configuration_mo,
            self.frr_configuration_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
