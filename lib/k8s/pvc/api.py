class K8sPvcApi():
    def __init__(self):
        self.pvc_mo = None
        self.pvc_namespace_mo = {}

    def get_pvc_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.pvc_mo,
            self.pvc_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.pvc_mo, self.pvc_namespace_mo = self.get_namespaced_resources(
            'PersistentVolumeClaim', 
            'v1', 
            self.pvc_mo,
            self.pvc_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_pvc_mo(self, namespace, name):
        success, _ = self.delete_resource('PersistentVolumeClaim', 'v1', name, namespace=namespace)
        return success