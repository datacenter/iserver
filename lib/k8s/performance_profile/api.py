class K8sPerformanceProfileApi():
    def __init__(self):
        self.performance_profile_mo = None

    def get_performance_profile_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.performance_profile_mo
        )
        if cache_hit:
            return response

        response, self.performance_profile_mo = self.get_resources(
            'PerformanceProfile', 
            'performance.openshift.io/v2', 
            self.performance_profile_mo,
            name=name
        )

        return response