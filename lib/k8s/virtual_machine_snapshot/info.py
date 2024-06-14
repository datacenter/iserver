from lib import filter_helper


class K8sVirtualMachineSnapshotInfo():
    def __init__(self):
        self.virtual_machine_snapshot = None

    def get_virtual_machine_snapshot_info(self, virtual_machine_snapshot_mo):
        if virtual_machine_snapshot_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            virtual_machine_snapshot_mo
        )
        info.update(metadata_info)

        return info

    def get_virtual_machine_snapshots_info(self, cache_enabled=True):
        if cache_enabled:
            if self.virtual_machine_snapshot is not None:
                return self.virtual_machine_snapshot

        managed_objects = self.get_virtual_machine_snapshot_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.virtual_machine_snapshot = []
        for managed_object in managed_objects:
            virtual_machine_snapshot_info = {}
            virtual_machine_snapshot_info['info'] = self.get_virtual_machine_snapshot_info(
                managed_object
            )
            virtual_machine_snapshot_info['mo'] = managed_object
            self.virtual_machine_snapshot.append(
                virtual_machine_snapshot_info
            )

        return self.virtual_machine_snapshot

    def match_virtual_machine_snapshot(self, virtual_machine_snapshot_info, virtual_machine_snapshot_filter):
        if virtual_machine_snapshot_filter is None or len(virtual_machine_snapshot_filter) == 0:
            return True

        for ap_rule in virtual_machine_snapshot_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_virtual_machine_snapshot',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_virtual_machine_snapshots(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_virtual_machine_snapshots = self.get_virtual_machine_snapshots_info(cache_enabled=cache_enabled)
        if all_virtual_machine_snapshots is None:
            return None

        virtual_machine_snapshots = []

        for virtual_machine_snapshot_info in all_virtual_machine_snapshots:
            if not self.match_virtual_machine_snapshot(virtual_machine_snapshot_info['info'], object_filter):
                continue

            if return_mo:
                virtual_machine_snapshots.append(
                    virtual_machine_snapshot_info['mo']
                )
                continue

            virtual_machine_snapshots.append(
                virtual_machine_snapshot_info['info']
            )

        return virtual_machine_snapshots
