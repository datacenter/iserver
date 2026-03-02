class K8sLocalVolumeSetApi():
    def __init__(self):
        self.local_volume_set_mo = None
        self.local_volume_set_namespace_mo = {}

    def get_local_volume_set_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.local_volume_set_mo,
            self.local_volume_set_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.local_volume_set_mo, self.local_volume_set_namespace_mo = self.get_namespaced_resources(
            'LocalVolumeSet', 
            'local.storage.openshift.io/v1alpha1', 
            self.local_volume_set_mo,
            self.local_volume_set_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_local_volume_set_mo(self, namespace, name):
        return self.delete_resource('LocalVolumeSet', 'local.storage.openshift.io/v1alpha1', name, namespace=namespace)
