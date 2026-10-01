class K8sVolumeCloneSourceApi():
    def __init__(self):
        self.volume_clone_source_mo = None
        
    def get_volume_clone_source_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.volume_clone_source_mo
        )
        if cache_hit:
            return response

        response, self.volume_clone_source_mo = self.get_resources(
            'VolumeCloneSource', 
            'cdi.kubevirt.io/v1beta1', 
            self.volume_clone_source_mo,
            name=name
        )

        return response