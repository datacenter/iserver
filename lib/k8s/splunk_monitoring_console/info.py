class K8sSplunkMonitoringConsoleInfo():
    def __init__(self):
        self.splunk_monitoring_console = None

    def get_splunk_monitoring_console_info(self, managed_object):
        return self.get_base_info(managed_object)

    def get_splunk_monitoring_consoles(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'splunk_monitoring_console', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_splunk_monitoring_console(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_splunk_monitoring_console(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_splunk_monitoring_console(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'splunk_monitoring_console', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )