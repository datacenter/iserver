class K8sServiceMonitorApi():
    def __init__(self):
        self.service_monitor_mo = None
        self.service_monitor_namespace_mo = {}

    def get_service_monitor_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.service_monitor_mo,
            self.service_monitor_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.service_monitor_mo, self.service_monitor_namespace_mo = self.get_namespaced_resources(
            'ServiceMonitor', 
            'monitoring.coreos.com/v1', 
            self.service_monitor_mo,
            self.service_monitor_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_service_monitor_mo(self, namespace, name):
        success, _ = self.delete_resource('ServiceMonitor', 'monitoring.coreos.com/v1', name, namespace=namespace)
        return success