class K8sVersionApi():
    def __init__(self):
        self.version_mo = None

    def get_version_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.version_mo
        )
        if cache_hit:
            return response

        response, self.version_mo = self.get_resources(
            'ClusterVersion', 
            'config.openshift.io/v1', 
            self.version_mo,
            name=name
        )

        return response