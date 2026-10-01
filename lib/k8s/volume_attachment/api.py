class K8sVolumeAttachmentApi():
    def __init__(self):
        self.volume_attachment_mo = None
        
    def get_volume_attachment_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.volume_attachment_mo
        )
        if cache_hit:
            return response

        response, self.volume_attachment_mo = self.get_resources(
            'VolumeAttachment', 
            'storage.k8s.io/v1', 
            self.volume_attachment_mo,
            name=name
        )

        return response