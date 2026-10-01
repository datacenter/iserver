class K8sProviderApi():
    def __init__(self):
        self.provider_mo = None
        self.provider_namespace_mo = {}

    def get_provider_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.provider_mo,
            self.provider_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.provider_mo, self.provider_namespace_mo = self.get_namespaced_resources(
            'Provider', 
            'forklift.konveyor.io/v1beta1', 
            self.provider_mo,
            self.provider_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_provider_mo(self, namespace, name):
        success, _ = self.delete_resource('Provider', 'forklift.konveyor.io/v1beta1', name, namespace=namespace)
        return success