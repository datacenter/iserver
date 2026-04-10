class K8sMetalLbApi():
    def __init__(self):
        self.metallb_mo = None
        self.metallb_namespace_mo = {}

    def get_metallb_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.metallb_mo,
            self.metallb_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.metallb_mo, self.metallb_namespace_mo = self.get_namespaced_resources(
            'MetalLB', 
            'metallb.io/v1beta1', 
            self.metallb_mo,
            self.metallb_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_metallb_mo(self, namespace, name):
        return self.delete_resource('MetalLB', 'metallb.io/v1beta1', name, namespace=namespace)
