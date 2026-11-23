class K8sDataVolumeApi():
    def __init__(self):
        self.data_volume_mo = None
        self.data_volume_namespace_mo = {}

    def get_data_volume_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.data_volume_mo,
            self.data_volume_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.data_volume_mo, self.data_volume_namespace_mo = self.get_namespaced_resources(
            'DataVolume', 
            'cdi.kubevirt.io/v1beta1', 
            self.data_volume_mo,
            self.data_volume_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_data_volume_mo(self, namespace, name):
        success, _ = self.delete_resource('DataVolume', 'cdi.kubevirt.io/v1beta1', name, namespace=namespace)
        return success