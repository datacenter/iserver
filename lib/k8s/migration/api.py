class K8sMigrationApi():
    def __init__(self):
        self.migration_mo = None
        self.migration_namespace_mo = {}

    def get_migration_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.migration_mo,
            self.migration_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.migration_mo, self.migration_namespace_mo = self.get_namespaced_resources(
            'Migration', 
            'forklift.konveyor.io/v1beta1', 
            self.migration_mo,
            self.migration_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
    
    def delete_migration_mo(self, namespace, name):
        self.delete_resource('Migration', 'forklift.konveyor.io/v1beta1', name, namespace=namespace)