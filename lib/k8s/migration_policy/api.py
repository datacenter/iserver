class K8sMigrationPolicyApi():
    def __init__(self):
        self.migration_policy_mo = None

    def get_migration_policy_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.migration_policy_mo
        )
        if cache_hit:
            return response

        response, self.migration_policy_mo = self.get_resources(
            'MigrationPolicy', 
            'migrations.kubevirt.io/v1alpha1', 
            self.migration_policy_mo,
            name=name
        )

        return response