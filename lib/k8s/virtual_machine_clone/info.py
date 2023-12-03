from lib import filter_helper


class K8sVirtualMachineCloneInfo():
    def __init__(self):
        self.virtual_machine_clone = None

    def get_virtual_machine_clone_info(self, virtual_machine_clone_mo):
        if virtual_machine_clone_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            virtual_machine_clone_mo
        )
        info.update(metadata_info)

        return info

    def get_virtual_machine_clones_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_clone is not None:
                return self.virtual_machine_clone

        managed_objects = self.get_virtual_machine_clone_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.virtual_machine_clone = []
        for managed_object in managed_objects:
            virtual_machine_clone_info = {}
            virtual_machine_clone_info['info'] = self.get_virtual_machine_clone_info(
                managed_object
            )
            virtual_machine_clone_info['mo'] = managed_object
            self.virtual_machine_clone.append(
                virtual_machine_clone_info
            )

        return self.virtual_machine_clone

    def match_virtual_machine_clone(self, virtual_machine_clone_info, virtual_machine_clone_filter):
        if virtual_machine_clone_filter is None or len(virtual_machine_clone_filter) == 0:
            return True

        for ap_rule in virtual_machine_clone_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_virtual_machine_clone',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machine_clones(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_virtual_machine_clones = self.get_virtual_machine_clones_info(cache_enabled=cache_enabled)
        if all_virtual_machine_clones is None:
            return None

        virtual_machine_clones = []

        for virtual_machine_clone_info in all_virtual_machine_clones:
            if not self.match_virtual_machine_clone(virtual_machine_clone_info['info'], object_filter):
                continue

            if return_mo:
                virtual_machine_clones.append(
                    virtual_machine_clone_info['mo']
                )
                continue

            virtual_machine_clones.append(
                virtual_machine_clone_info['info']
            )

        return virtual_machine_clones
