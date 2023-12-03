from lib import filter_helper


class K8sVirtualMachineInstanceReplicaSetInfo():
    def __init__(self):
        self.virtual_machine_instance_replica_set = None

    def get_virtual_machine_instance_replica_set_info(self, virtual_machine_instance_replica_set_mo):
        if virtual_machine_instance_replica_set_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            virtual_machine_instance_replica_set_mo
        )
        info.update(metadata_info)

        return info

    def get_virtual_machine_instance_replica_sets_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_instance_replica_set is not None:
                return self.virtual_machine_instance_replica_set

        managed_objects = self.get_virtual_machine_instance_replica_set_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.virtual_machine_instance_replica_set = []
        for managed_object in managed_objects:
            virtual_machine_instance_replica_set_info = {}
            virtual_machine_instance_replica_set_info['info'] = self.get_virtual_machine_instance_replica_set_info(
                managed_object
            )
            virtual_machine_instance_replica_set_info['mo'] = managed_object
            self.virtual_machine_instance_replica_set.append(
                virtual_machine_instance_replica_set_info
            )

        return self.virtual_machine_instance_replica_set

    def match_virtual_machine_instance_replica_set(self, virtual_machine_instance_replica_set_info, virtual_machine_instance_replica_set_filter):
        if virtual_machine_instance_replica_set_filter is None or len(virtual_machine_instance_replica_set_filter) == 0:
            return True

        for ap_rule in virtual_machine_instance_replica_set_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_virtual_machine_instance_replica_set',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machine_instance_replica_sets(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_virtual_machine_instance_replica_sets = self.get_virtual_machine_instance_replica_sets_info(cache_enabled=cache_enabled)
        if all_virtual_machine_instance_replica_sets is None:
            return None

        virtual_machine_instance_replica_sets = []

        for virtual_machine_instance_replica_set_info in all_virtual_machine_instance_replica_sets:
            if not self.match_virtual_machine_instance_replica_set(virtual_machine_instance_replica_set_info['info'], object_filter):
                continue

            if return_mo:
                virtual_machine_instance_replica_sets.append(
                    virtual_machine_instance_replica_set_info['mo']
                )
                continue

            virtual_machine_instance_replica_sets.append(
                virtual_machine_instance_replica_set_info['info']
            )

        return virtual_machine_instance_replica_sets
