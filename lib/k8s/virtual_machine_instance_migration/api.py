class K8sVirtualMachineInstanceMigrationApi():
    def __init__(self):
        self.virtual_machine_instance_migration_mo = None

    def get_virtual_machine_instance_migration_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.virtual_machine_instance_migration_mo
        )
        if cache_hit:
            return response

        response, self.virtual_machine_instance_migration_mo = self.get_resources(
            'VirtualMachineInstanceMigration', 
            'kubevirt.io/v1', 
            self.virtual_machine_instance_migration_mo,
            name=name
        )

        return response