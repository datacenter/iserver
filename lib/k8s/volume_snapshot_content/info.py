from lib import filter_helper


class K8sVolumeSnapshotContentInfo():
    def __init__(self):
        self.volume_snapshot_content = None

    def get_volume_snapshot_content_info(self, volume_snapshot_content_mo):
        if volume_snapshot_content_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            volume_snapshot_content_mo
        )
        info.update(metadata_info)

        return info

    def get_volume_snapshot_contents_info(self, cache_enabled=True):
        if cache_enabled:
            if self.volume_snapshot_content is not None:
                return self.volume_snapshot_content

        managed_objects = self.get_volume_snapshot_content_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.volume_snapshot_content = []
        for managed_object in managed_objects:
            volume_snapshot_content_info = {}
            volume_snapshot_content_info['info'] = self.get_volume_snapshot_content_info(
                managed_object
            )
            volume_snapshot_content_info['mo'] = managed_object
            self.volume_snapshot_content.append(
                volume_snapshot_content_info
            )

        return self.volume_snapshot_content

    def match_volume_snapshot_content(self, volume_snapshot_content_info, volume_snapshot_content_filter):
        if volume_snapshot_content_filter is None or len(volume_snapshot_content_filter) == 0:
            return True

        for ap_rule in volume_snapshot_content_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_volume_snapshot_content',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_volume_snapshot_contents(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_volume_snapshot_contents = self.get_volume_snapshot_contents_info(cache_enabled=cache_enabled)
        if all_volume_snapshot_contents is None:
            return None

        volume_snapshot_contents = []

        for volume_snapshot_content_info in all_volume_snapshot_contents:
            if not self.match_volume_snapshot_content(volume_snapshot_content_info['info'], object_filter):
                continue

            if return_mo:
                volume_snapshot_contents.append(
                    volume_snapshot_content_info['mo']
                )
                continue

            volume_snapshot_contents.append(
                volume_snapshot_content_info['info']
            )

        return volume_snapshot_contents
