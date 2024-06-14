from lib import filter_helper


class K8sVirtualMachineInstanceMigrationInfo():
    def __init__(self):
        self.virtual_machine_instance_migration = None

    def get_virtual_machine_instance_migration_info(self, virtual_machine_instance_migration_mo):
        if virtual_machine_instance_migration_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            virtual_machine_instance_migration_mo
        )
        info.update(metadata_info)

        return info

    def get_virtual_machine_instance_migrations_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_instance_migration is not None:
                return self.virtual_machine_instance_migration

        managed_objects = self.get_virtual_machine_instance_migration_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.virtual_machine_instance_migration = []
        for managed_object in managed_objects:
            virtual_machine_instance_migration_info = {}
            virtual_machine_instance_migration_info['info'] = self.get_virtual_machine_instance_migration_info(
                managed_object
            )
            virtual_machine_instance_migration_info['mo'] = managed_object
            self.virtual_machine_instance_migration.append(
                virtual_machine_instance_migration_info
            )

        return self.virtual_machine_instance_migration

    def match_virtual_machine_instance_migration(self, virtual_machine_instance_migration_info, virtual_machine_instance_migration_filter):
        if virtual_machine_instance_migration_filter is None or len(virtual_machine_instance_migration_filter) == 0:
            return True

        for ap_rule in virtual_machine_instance_migration_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_virtual_machine_instance_migration',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machine_instance_migrations(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_virtual_machine_instance_migrations = self.get_virtual_machine_instance_migrations_info(cache_enabled=cache_enabled)
        if all_virtual_machine_instance_migrations is None:
            return None

        virtual_machine_instance_migrations = []

        for virtual_machine_instance_migration_info in all_virtual_machine_instance_migrations:
            if not self.match_virtual_machine_instance_migration(virtual_machine_instance_migration_info['info'], object_filter):
                continue

            if return_mo:
                virtual_machine_instance_migrations.append(
                    virtual_machine_instance_migration_info['mo']
                )
                continue

            virtual_machine_instance_migrations.append(
                virtual_machine_instance_migration_info['info']
            )

        return virtual_machine_instance_migrations
