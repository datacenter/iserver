from lib import filter_helper


class K8sVirtualMachineExportInfo():
    def __init__(self):
        self.virtual_machine_export = None

    def get_virtual_machine_export_info(self, virtual_machine_export_mo):
        if virtual_machine_export_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            virtual_machine_export_mo
        )
        info.update(metadata_info)

        return info

    def get_virtual_machine_exports_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_export is not None:
                return self.virtual_machine_export

        managed_objects = self.get_virtual_machine_export_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.virtual_machine_export = []
        for managed_object in managed_objects:
            virtual_machine_export_info = {}
            virtual_machine_export_info['info'] = self.get_virtual_machine_export_info(
                managed_object
            )
            virtual_machine_export_info['mo'] = managed_object
            self.virtual_machine_export.append(
                virtual_machine_export_info
            )

        return self.virtual_machine_export

    def match_virtual_machine_export(self, virtual_machine_export_info, virtual_machine_export_filter):
        if virtual_machine_export_filter is None or len(virtual_machine_export_filter) == 0:
            return True

        for ap_rule in virtual_machine_export_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_virtual_machine_export',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machine_exports(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_virtual_machine_exports = self.get_virtual_machine_exports_info(cache_enabled=cache_enabled)
        if all_virtual_machine_exports is None:
            return None

        virtual_machine_exports = []

        for virtual_machine_export_info in all_virtual_machine_exports:
            if not self.match_virtual_machine_export(virtual_machine_export_info['info'], object_filter):
                continue

            if return_mo:
                virtual_machine_exports.append(
                    virtual_machine_export_info['mo']
                )
                continue

            virtual_machine_exports.append(
                virtual_machine_export_info['info']
            )

        return virtual_machine_exports
