class K8sKubevirtApi():
    def __init__(self):
        self.kubevirt_mo = None

    def get_kubevirt_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.kubevirt_mo
        )
        if cache_hit:
            return response

        response, self.kubevirt_mo = self.get_resources(
            'KubeVirt', 
            'kubevirt.io/v1', 
            self.kubevirt_mo,
            name=name
        )

        return response