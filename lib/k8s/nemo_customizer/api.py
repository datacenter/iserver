class K8sNemoCustomizerApi():
    def __init__(self):
        self.nemo_customizer_mo = None
        self.nemo_customizer_namespace_mo = {}

    def get_nemo_customizer_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.nemo_customizer_mo,
            self.nemo_customizer_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.nemo_customizer_mo, self.nemo_customizer_namespace_mo = self.get_namespaced_resources(
            'NemoCustomizer', 
            'apps.nvidia.com/v1alpha1', 
            self.nemo_customizer_mo,
            self.nemo_customizer_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_nemo_customizer_mo(self, namespace, name):
        success, _ = self.delete_resource('NemoCustomizer', 'apps.nvidia.com/v1alpha1', name, namespace=namespace)
        return success