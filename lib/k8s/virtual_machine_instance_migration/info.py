class K8sVirtualMachineInstanceMigrationInfo():
    def __init__(self):
        self.virtual_machine_instance_migration = None

    def get_virtual_machine_instance_migration_info(self, managed_object):
        return self.get_base_info(managed_object)
        
    def get_virtual_machine_instance_migrations(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'virtual_machine_instance_migration', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_virtual_machine_instance_migration(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'virtual_machine_instance_migration', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_virtual_machine_instance_migration(self, name, cache_enabled=True, optimized=True):
        if self.get_virtual_machine_instance_migration(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_virtual_machine_instance_migration(self, cache_enabled=True):
        infos = self.get_virtual_machine_instance_migrations(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True