class K8sDaemonSetApi():
    def __init__(self):
        self.daemon_set_mo = None
        self.daemon_set_namespace_mo = {}

    def get_daemon_set_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.daemon_set_mo,
            self.daemon_set_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.daemon_set_mo, self.daemon_set_namespace_mo = self.get_namespaced_resources(
            'DaemonSet', 
            'apps/v1', 
            self.daemon_set_mo,
            self.daemon_set_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response