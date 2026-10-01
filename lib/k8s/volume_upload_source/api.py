class K8sVolumeUploadSourceApi():
    def __init__(self):
        self.volume_upload_source_mo = None
        self.volume_upload_source_namespace_mo = {}

    def get_volume_upload_source_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.volume_upload_source_mo,
            self.volume_upload_source_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.volume_upload_source_mo, self.volume_upload_source_namespace_mo = self.get_namespaced_resources(
            'VolumeUploadSource', 
            'cdi.kubevirt.io/v1beta1',
            self.volume_upload_source_mo,
            self.volume_upload_source_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response