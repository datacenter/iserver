class K8sVolumeAttachmentInfo():
    def __init__(self):
        self.volume_attachment = None

    def get_volume_attachment_info(self, managed_object):
        return self.get_base_info(managed_object)
        
    def get_volume_attachments(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'volume_attachment', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_volume_attachment(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'volume_attachment', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_volume_attachment(self, name, cache_enabled=True, optimized=True):
        if self.get_volume_attachment(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_volume_attachment(self, cache_enabled=True):
        infos = self.get_volume_attachments(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True