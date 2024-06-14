from lib import filter_helper


class K8sVolumeSnapshotClassInfo():
    def __init__(self):
        self.volume_snapshot_class = None

    def get_volume_snapshot_class_info(self, volume_snapshot_class_mo):
        if volume_snapshot_class_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            volume_snapshot_class_mo
        )
        info.update(metadata_info)

        return info

    def get_volume_snapshot_classs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.volume_snapshot_class is not None:
                return self.volume_snapshot_class

        managed_objects = self.get_volume_snapshot_class_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.volume_snapshot_class = []
        for managed_object in managed_objects:
            volume_snapshot_class_info = {}
            volume_snapshot_class_info['info'] = self.get_volume_snapshot_class_info(
                managed_object
            )
            volume_snapshot_class_info['mo'] = managed_object
            self.volume_snapshot_class.append(
                volume_snapshot_class_info
            )

        return self.volume_snapshot_class

    def match_volume_snapshot_class(self, volume_snapshot_class_info, volume_snapshot_class_filter):
        if volume_snapshot_class_filter is None or len(volume_snapshot_class_filter) == 0:
            return True

        for ap_rule in volume_snapshot_class_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_volume_snapshot_class',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_volume_snapshot_classs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_volume_snapshot_classs = self.get_volume_snapshot_classs_info(cache_enabled=cache_enabled)
        if all_volume_snapshot_classs is None:
            return None

        volume_snapshot_classs = []

        for volume_snapshot_class_info in all_volume_snapshot_classs:
            if not self.match_volume_snapshot_class(volume_snapshot_class_info['info'], object_filter):
                continue

            if return_mo:
                volume_snapshot_classs.append(
                    volume_snapshot_class_info['mo']
                )
                continue

            volume_snapshot_classs.append(
                volume_snapshot_class_info['info']
            )

        return volume_snapshot_classs
