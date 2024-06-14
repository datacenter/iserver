from lib import filter_helper


class K8sVolumeAttachmentInfo():
    def __init__(self):
        self.volume_attachment = None

    def get_volume_attachment_info(self, volume_attachment_mo):
        if volume_attachment_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            volume_attachment_mo
        )
        info.update(metadata_info)

        return info

    def get_volume_attachments_info(self, cache_enabled=True):
        if cache_enabled:
            if self.volume_attachment is not None:
                return self.volume_attachment

        managed_objects = self.get_volume_attachment_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.volume_attachment = []
        for managed_object in managed_objects:
            volume_attachment_info = {}
            volume_attachment_info['info'] = self.get_volume_attachment_info(
                managed_object
            )
            volume_attachment_info['mo'] = managed_object
            self.volume_attachment.append(
                volume_attachment_info
            )

        return self.volume_attachment

    def match_volume_attachment(self, volume_attachment_info, volume_attachment_filter):
        if volume_attachment_filter is None or len(volume_attachment_filter) == 0:
            return True

        for ap_rule in volume_attachment_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_volume_attachment',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_volume_attachments(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_volume_attachments = self.get_volume_attachments_info(cache_enabled=cache_enabled)
        if all_volume_attachments is None:
            return None

        volume_attachments = []

        for volume_attachment_info in all_volume_attachments:
            if not self.match_volume_attachment(volume_attachment_info['info'], object_filter):
                continue

            if return_mo:
                volume_attachments.append(
                    volume_attachment_info['mo']
                )
                continue

            volume_attachments.append(
                volume_attachment_info['info']
            )

        return volume_attachments
