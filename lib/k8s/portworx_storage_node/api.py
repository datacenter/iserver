class K8sPortworxStorageNodeApi():
    def __init__(self):
        self.portworx_storage_node_mo = None
        self.portworx_storage_node_namespace_mo = {}

    def get_portworx_storage_node_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.portworx_storage_node_mo,
            self.portworx_storage_node_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.portworx_storage_node_mo, self.portworx_storage_node_namespace_mo = self.get_namespaced_resources(
            'StorageNode', 
            'core.libopenstorage.org/v1', 
            self.portworx_storage_node_mo,
            self.portworx_storage_node_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_portworx_storage_node_mo(self, namespace, name):
        return self.delete_resource('StorageNode', 'core.libopenstorage.org/v1', name, namespace=namespace)
