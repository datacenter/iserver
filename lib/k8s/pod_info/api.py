class K8sPodInfoApi():
    def __init__(self):
        self.pod_info_mo = None
        self.pod_info_namespace_mo = {}

    def get_pod_info_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.pod_info_mo,
            self.pod_info_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.pod_info_mo, self.pod_info_namespace_mo = self.get_namespaced_resources(
            'PodInfo', 
            'cilium.io/v1alpha1', 
            self.pod_info_mo,
            self.pod_info_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response