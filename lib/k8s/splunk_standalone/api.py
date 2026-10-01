class K8sSplunkStandaloneApi():
    def __init__(self):
        self.splunk_standalone_mo = None
        self.splunk_standalone_namespace_mo = {}

    def get_splunk_standalone_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.splunk_standalone_mo,
            self.splunk_standalone_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.splunk_standalone_mo, self.splunk_standalone_namespace_mo = self.get_namespaced_resources(
            'Standalone', 
            'enterprise.splunk.com/v4', 
            self.splunk_standalone_mo,
            self.splunk_standalone_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_splunk_standalone_mo(self, namespace, name):
        success, _ = self.delete_resource('Standalone', 'enterprise.splunk.com/v4', name, namespace=namespace)
        return success