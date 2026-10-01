class K8sProbeApi():
    def __init__(self):
        self.probe_mo = None
        self.probe_namespace_mo = {}

    def get_probe_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.probe_mo,
            self.probe_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.probe_mo, self.probe_namespace_mo = self.get_namespaced_resources(
            'Probe', 
            'monitoring.coreos.com/v1', 
            self.probe_mo,
            self.probe_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response