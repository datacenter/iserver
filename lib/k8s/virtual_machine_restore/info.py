from lib import filter_helper


class K8sVirtualMachineRestoreInfo():
    def __init__(self):
        self.virtual_machine_restore = None

    def get_virtual_machine_restore_info(self, virtual_machine_restore_mo):
        if virtual_machine_restore_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            virtual_machine_restore_mo
        )
        info.update(metadata_info)

        return info

    def get_virtual_machine_restores_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_restore is not None:
                return self.virtual_machine_restore

        managed_objects = self.get_virtual_machine_restore_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.virtual_machine_restore = []
        for managed_object in managed_objects:
            virtual_machine_restore_info = {}
            virtual_machine_restore_info['info'] = self.get_virtual_machine_restore_info(
                managed_object
            )
            virtual_machine_restore_info['mo'] = managed_object
            self.virtual_machine_restore.append(
                virtual_machine_restore_info
            )

        return self.virtual_machine_restore

    def match_virtual_machine_restore(self, virtual_machine_restore_info, virtual_machine_restore_filter):
        if virtual_machine_restore_filter is None or len(virtual_machine_restore_filter) == 0:
            return True

        for ap_rule in virtual_machine_restore_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_virtual_machine_restore',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machine_restores(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_virtual_machine_restores = self.get_virtual_machine_restores_info(cache_enabled=cache_enabled)
        if all_virtual_machine_restores is None:
            return None

        virtual_machine_restores = []

        for virtual_machine_restore_info in all_virtual_machine_restores:
            if not self.match_virtual_machine_restore(virtual_machine_restore_info['info'], object_filter):
                continue

            if return_mo:
                virtual_machine_restores.append(
                    virtual_machine_restore_info['mo']
                )
                continue

            virtual_machine_restores.append(
                virtual_machine_restore_info['info']
            )

        return virtual_machine_restores
