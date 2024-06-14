from lib import filter_helper


class K8sVirtualMachineSnapshotContentInfo():
    def __init__(self):
        self.virtual_machine_snapshot_content = None

    def get_virtual_machine_snapshot_content_info(self, virtual_machine_snapshot_content_mo):
        if virtual_machine_snapshot_content_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            virtual_machine_snapshot_content_mo
        )
        info.update(metadata_info)

        return info

    def get_virtual_machine_snapshot_contents_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_snapshot_content is not None:
                return self.virtual_machine_snapshot_content

        managed_objects = self.get_virtual_machine_snapshot_content_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.virtual_machine_snapshot_content = []
        for managed_object in managed_objects:
            virtual_machine_snapshot_content_info = {}
            virtual_machine_snapshot_content_info['info'] = self.get_virtual_machine_snapshot_content_info(
                managed_object
            )
            virtual_machine_snapshot_content_info['mo'] = managed_object
            self.virtual_machine_snapshot_content.append(
                virtual_machine_snapshot_content_info
            )

        return self.virtual_machine_snapshot_content

    def match_virtual_machine_snapshot_content(self, virtual_machine_snapshot_content_info, virtual_machine_snapshot_content_filter):
        if virtual_machine_snapshot_content_filter is None or len(virtual_machine_snapshot_content_filter) == 0:
            return True

        for ap_rule in virtual_machine_snapshot_content_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_virtual_machine_snapshot_content',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machine_snapshot_contents(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_virtual_machine_snapshot_contents = self.get_virtual_machine_snapshot_contents_info(cache_enabled=cache_enabled)
        if all_virtual_machine_snapshot_contents is None:
            return None

        virtual_machine_snapshot_contents = []

        for virtual_machine_snapshot_content_info in all_virtual_machine_snapshot_contents:
            if not self.match_virtual_machine_snapshot_content(virtual_machine_snapshot_content_info['info'], object_filter):
                continue

            if return_mo:
                virtual_machine_snapshot_contents.append(
                    virtual_machine_snapshot_content_info['mo']
                )
                continue

            virtual_machine_snapshot_contents.append(
                virtual_machine_snapshot_content_info['info']
            )

        return virtual_machine_snapshot_contents
