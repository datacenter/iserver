class K8sVirtualMachineClusterInstanceTypeApi():
    def __init__(self):
        self.virtual_machine_cluster_instance_type_mo = None

    def get_virtual_machine_cluster_instance_type_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.virtual_machine_cluster_instance_type_mo
        )
        if cache_hit:
            return response

        response, self.virtual_machine_cluster_instance_type_mo = self.get_resources(
            'VirtualMachineClusterInstancetype', 
            'instancetype.kubevirt.io/v1beta1', 
            self.virtual_machine_cluster_instance_type_mo,
            name=name
        )

        return response