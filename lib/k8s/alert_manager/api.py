class K8sAlertManagerApi():
    def __init__(self):
        self.alert_manager_mo = None
        self.alert_manager_namespace_mo = {}

    def get_alert_manager_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.alert_manager_mo,
            self.alert_manager_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.alert_manager_mo, self.alert_manager_namespace_mo = self.get_namespaced_resources(
            'Alertmanager', 
            'monitoring.coreos.com/v1', 
            self.alert_manager_mo,
            self.alert_manager_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response