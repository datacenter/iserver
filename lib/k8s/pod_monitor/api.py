class K8sPodMonitorApi():
    def __init__(self):
        self.pod_monitor_mo = None
        self.pod_monitor_namespace_mo = {}

    def get_pod_monitor_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.pod_monitor_mo,
            self.pod_monitor_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.pod_monitor_mo, self.pod_monitor_namespace_mo = self.get_namespaced_resources(
            'PodMonitor', 
            'monitoring.coreos.com/v1', 
            self.pod_monitor_mo,
            self.pod_monitor_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response