class K8sSplunkMonitoringConsoleApi():
    def __init__(self):
        self.splunk_monitoring_console_mo = None
        self.splunk_monitoring_console_namespace_mo = {}

    def get_splunk_monitoring_console_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.splunk_monitoring_console_mo,
            self.splunk_monitoring_console_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.splunk_monitoring_console_mo, self.splunk_monitoring_console_namespace_mo = self.get_namespaced_resources(
            'MonitoringConsole', 
            'enterprise.splunk.com/v4', 
            self.splunk_monitoring_console_mo,
            self.splunk_monitoring_console_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response