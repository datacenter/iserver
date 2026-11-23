class K8sNetworkAttachmentDefinitionApi():
    def __init__(self):
        self.nad_mo = None
        self.nad_namespace_mo = {}

    def get_nad_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.nad_mo,
            self.nad_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.nad_mo, self.nad_namespace_mo = self.get_namespaced_resources(
            'NetworkAttachmentDefinition', 
            'k8s.cni.cncf.io/v1', 
            self.nad_mo,
            self.nad_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_nad_mo(self, namespace, name):
        success, _ = self.delete_resource('NetworkAttachmentDefinition', 'k8s.cni.cncf.io/v1', name, namespace=namespace)
        return success