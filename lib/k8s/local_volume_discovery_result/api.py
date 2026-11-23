class K8sLocalVolumeDiscoveryResultApi():
    def __init__(self):
        self.local_volume_discovery_result_mo = None
        self.local_volume_discovery_result_namespace_mo = {}

    def get_local_volume_discovery_result_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.local_volume_discovery_result_mo,
            self.local_volume_discovery_result_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.local_volume_discovery_result_mo, self.local_volume_discovery_result_namespace_mo = self.get_namespaced_resources(
            'LocalVolumeDiscoveryResult', 
            'local.storage.openshift.io/v1alpha1', 
            self.local_volume_discovery_result_mo,
            self.local_volume_discovery_result_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
