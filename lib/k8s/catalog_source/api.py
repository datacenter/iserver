class K8sCatalogSourceApi():
    def __init__(self):
        self.catalog_source_mo = None
        self.catalog_source_namespace_mo = {}

    def get_catalog_source_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.catalog_source_mo,
            self.catalog_source_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.catalog_source_mo, self.catalog_source_namespace_mo = self.get_namespaced_resources(
            'CatalogSource', 
            'operators.coreos.com/v1alpha1', 
            self.catalog_source_mo,
            self.catalog_source_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response