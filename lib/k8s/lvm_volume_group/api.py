class K8sLvmVolumeGroupApi():
    def __init__(self):
        self.lvm_volume_group_mo = None
        self.lvm_volume_group_namespace_mo = {}

    def get_lvm_volume_group_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.lvm_volume_group_mo,
            self.lvm_volume_group_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.lvm_volume_group_mo, self.lvm_volume_group_namespace_mo = self.get_namespaced_resources(
            'LVMVolumeGroup', 
            'lvm.topolvm.io/v1alpha1', 
            self.lvm_volume_group_mo,
            self.lvm_volume_group_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
    
    def delete_lvm_volume_group_mo(self, namespace, name):
        success, _ = self.delete_resource('LVMVolumeGroup', 'lvm.topolvm.io/v1alpha1', name, namespace=namespace)
        return success