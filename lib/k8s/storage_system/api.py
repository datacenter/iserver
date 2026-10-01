class K8sStorageSystemApi():
    def __init__(self):
        self.storage_system_mo = None
        self.storage_system_namespace_mo = {}

    def get_storage_system_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.storage_system_mo,
            self.storage_system_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.storage_system_mo, self.storage_system_namespace_mo = self.get_namespaced_resources(
            'StorageSystem', 
            'odf.openshift.io/v1alpha1', 
            self.storage_system_mo,
            self.storage_system_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_storage_system_mo(self, namespace, name):
        success, _ = self.delete_resource('StorageSystem', 'odf.openshift.io/v1alpha1', name, namespace=namespace)
        return success