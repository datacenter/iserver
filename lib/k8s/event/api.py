class K8sEventApi():
    def __init__(self):
        self.event_mo = None
        self.event_namespace_mo = {}

    def get_event_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.event_mo,
            self.event_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.event_mo, self.event_namespace_mo = self.get_namespaced_resources(
            'Event', 
            'v1', 
            self.event_mo,
            self.event_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response