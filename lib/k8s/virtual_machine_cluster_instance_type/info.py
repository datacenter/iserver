from lib import filter_helper


class K8sVirtualMachineClusterInstanceTypeInfo():
    def __init__(self):
        self.virtual_machine_cluster_instance_type = None

    def get_virtual_machine_cluster_instance_type_info(self, virtual_machine_cluster_instance_type_mo):
        if virtual_machine_cluster_instance_type_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            virtual_machine_cluster_instance_type_mo
        )
        info.update(metadata_info)

        return info

    def get_virtual_machine_cluster_instance_types_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_cluster_instance_type is not None:
                return self.virtual_machine_cluster_instance_type

        managed_objects = self.get_virtual_machine_cluster_instance_type_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.virtual_machine_cluster_instance_type = []
        for managed_object in managed_objects:
            virtual_machine_cluster_instance_type_info = {}
            virtual_machine_cluster_instance_type_info['info'] = self.get_virtual_machine_cluster_instance_type_info(
                managed_object
            )
            virtual_machine_cluster_instance_type_info['mo'] = managed_object
            self.virtual_machine_cluster_instance_type.append(
                virtual_machine_cluster_instance_type_info
            )

        return self.virtual_machine_cluster_instance_type

    def match_virtual_machine_cluster_instance_type(self, virtual_machine_cluster_instance_type_info, virtual_machine_cluster_instance_type_filter):
        if virtual_machine_cluster_instance_type_filter is None or len(virtual_machine_cluster_instance_type_filter) == 0:
            return True

        for ap_rule in virtual_machine_cluster_instance_type_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_virtual_machine_cluster_instance_type',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machine_cluster_instance_types(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_virtual_machine_cluster_instance_types = self.get_virtual_machine_cluster_instance_types_info(cache_enabled=cache_enabled)
        if all_virtual_machine_cluster_instance_types is None:
            return None

        virtual_machine_cluster_instance_types = []

        for virtual_machine_cluster_instance_type_info in all_virtual_machine_cluster_instance_types:
            if not self.match_virtual_machine_cluster_instance_type(virtual_machine_cluster_instance_type_info['info'], object_filter):
                continue

            if return_mo:
                virtual_machine_cluster_instance_types.append(
                    virtual_machine_cluster_instance_type_info['mo']
                )
                continue

            virtual_machine_cluster_instance_types.append(
                virtual_machine_cluster_instance_type_info['info']
            )

        return virtual_machine_cluster_instance_types
