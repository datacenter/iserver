class K8sThanosRulerApi():
    def __init__(self):
        self.thanos_ruler_mo = None
        self.thanos_ruler_namespace_mo = {}

    def get_thanos_ruler_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.thanos_ruler_mo,
            self.thanos_ruler_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.thanos_ruler_mo, self.thanos_ruler_namespace_mo = self.get_namespaced_resources(
            'ThanosRuler', 
            'monitoring.coreos.com/v1', 
            self.thanos_ruler_mo,
            self.thanos_ruler_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response