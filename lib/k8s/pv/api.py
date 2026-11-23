class K8sPvApi():
    def __init__(self):
        self.pv_mo = None

    def get_pv_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.pv_mo
        )
        if cache_hit:
            return response

        response, self.pv_mo = self.get_resources(
            'PersistentVolume', 
            'v1', 
            self.pv_mo,
            name=name
        )

        return response
    
    def delete_pv_mo(self, name):
        success, _ = self.delete_resource('PersistentVolume', 'v1', name)
        return success