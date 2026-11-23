class K8sNmstateApi():
    def __init__(self):
        self.nmstate_mo = None

    def get_nmstate_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.nmstate_mo
        )
        if cache_hit:
            return response

        response, self.nmstate_mo = self.get_resources(
            'NMState', 
            'nmstate.io/v1', 
            self.nmstate_mo,
            name=name
        )

        return response
    
    def delete_nmstate_mo(self, name):
        success, _ = self.delete_resource('NMState', 'nmstate.io/v1', name)
        return success