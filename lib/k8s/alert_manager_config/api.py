class K8sAlertManagerConfigApi():
    def __init__(self):
        self.alert_manager_config_mo = None
        self.alert_manager_config_namespace_mo = {}

    def get_alert_manager_config_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.alert_manager_config_mo,
            self.alert_manager_config_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.alert_manager_config_mo, self.alert_manager_config_namespace_mo = self.get_namespaced_resources(
            'AlertmanagerConfig', 
            'monitoring.coreos.com/v1beta1', 
            self.alert_manager_config_mo,
            self.alert_manager_config_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response