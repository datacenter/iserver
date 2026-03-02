class K8sLocalVolumeApi():
    def __init__(self):
        self.local_volume_mo = None
        self.local_volume_namespace_mo = {}

    def get_local_volume_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.local_volume_mo,
            self.local_volume_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.local_volume_mo, self.local_volume_namespace_mo = self.get_namespaced_resources(
            'LocalVolume', 
            'local.storage.openshift.io/v1', 
            self.local_volume_mo,
            self.local_volume_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_local_volume_mo(self, namespace, name):
        return self.delete_resource('LocalVolume', 'local.storage.openshift.io/v1', name, namespace=namespace)
