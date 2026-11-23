class K8sLogicalVolumeApi():
    def __init__(self):
        self.logical_volume_mo = None

    def get_logical_volume_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.logical_volume_mo
        )
        if cache_hit:
            return response

        response, self.logical_volume_mo = self.get_resources(
            'LogicalVolume', 
            'topolvm.io/v1', 
            self.logical_volume_mo,
            name=name
        )

        return response