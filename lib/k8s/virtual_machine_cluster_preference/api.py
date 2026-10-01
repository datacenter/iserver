class K8sVirtualMachineClusterPreferenceApi():
    def __init__(self):
        self.virtual_machine_cluster_preference_mo = None

    def get_virtual_machine_cluster_preference_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.virtual_machine_cluster_preference_mo
        )
        if cache_hit:
            return response

        response, self.virtual_machine_cluster_preference_mo = self.get_resources(
            'VirtualMachineClusterPreference', 
            'instancetype.kubevirt.io/v1alpha2', 
            self.virtual_machine_cluster_preference_mo,
            name=name
        )

        return response