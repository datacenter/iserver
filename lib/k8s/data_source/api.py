class K8sDataSourceApi():
    def __init__(self):
        self.data_source_mo = None
        self.data_source_namespace_mo = {}

    def get_data_source_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.data_source_mo,
            self.data_source_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.data_source_mo, self.data_source_namespace_mo = self.get_namespaced_resources(
            'DataSource', 
            'cdi.kubevirt.io/v1beta1', 
            self.data_source_mo,
            self.data_source_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response