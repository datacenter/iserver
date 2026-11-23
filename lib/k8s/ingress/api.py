class K8sIngressApi():
    def __init__(self):
        self.ingress_mo = None
        self.intress_namespace_mo = {}

    def get_intress_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.intress_mo,
            self.intress_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.intress_mo, self.intress_namespace_mo = self.get_namespaced_resources(
            'Ingress', 
            'networking.k8s.io/v1', 
            self.intress_mo,
            self.intress_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response