class K8sOcsInitializationApi():
    def __init__(self):
        self.ocs_initialization_mo = None
        self.ocs_initialization_namespace_mo = {}

    def get_ocs_initialization_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.ocs_initialization_mo,
            self.ocs_initialization_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.ocs_initialization_mo, self.ocs_initialization_namespace_mo = self.get_namespaced_resources(
            'OCSInitialization', 
            'ocs.openshift.io/v1', 
            self.ocs_initialization_mo,
            self.ocs_initialization_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_ocs_initialization_mo(self, namespace, name):
        success, _ = self.delete_resource('OCSInitialization', 'ocs.openshift.io/v1', name, namespace=namespace)
        return success