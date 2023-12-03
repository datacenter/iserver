from lib import filter_helper


class K8sVolumeSnapshotInfo():
    def __init__(self):
        self.volume_snapshot = None

    def get_volume_snapshot_info(self, volume_snapshot_mo):
        if volume_snapshot_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            volume_snapshot_mo
        )
        info.update(metadata_info)

        return info

    def get_volume_snapshots_info(self, cache_enabled=True):
        if cache_enabled:
            if self.volume_snapshot is not None:
                return self.volume_snapshot

        managed_objects = self.get_volume_snapshot_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.volume_snapshot = []
        for managed_object in managed_objects:
            volume_snapshot_info = {}
            volume_snapshot_info['info'] = self.get_volume_snapshot_info(
                managed_object
            )
            volume_snapshot_info['mo'] = managed_object
            self.volume_snapshot.append(
                volume_snapshot_info
            )

        return self.volume_snapshot

    def match_volume_snapshot(self, volume_snapshot_info, volume_snapshot_filter):
        if volume_snapshot_filter is None or len(volume_snapshot_filter) == 0:
            return True

        for ap_rule in volume_snapshot_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_volume_snapshot',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_volume_snapshots(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_volume_snapshots = self.get_volume_snapshots_info(cache_enabled=cache_enabled)
        if all_volume_snapshots is None:
            return None

        volume_snapshots = []

        for volume_snapshot_info in all_volume_snapshots:
            if not self.match_volume_snapshot(volume_snapshot_info['info'], object_filter):
                continue

            if return_mo:
                volume_snapshots.append(
                    volume_snapshot_info['mo']
                )
                continue

            volume_snapshots.append(
                volume_snapshot_info['info']
            )

        return volume_snapshots
