class K8sVirtualMachineInstanceReplicaSetApi():
    def __init__(self):
        self.virtual_machine_instance_replica_set_mo = None
        self.virtual_machine_instance_replica_set_namespace_mo = {}

    def get_virtual_machine_instance_replica_set_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.virtual_machine_instance_replica_set_mo,
            self.virtual_machine_instance_replica_set_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.virtual_machine_instance_replica_set_mo, self.virtual_machine_instance_replica_set_namespace_mo = self.get_namespaced_resources(
            'VirtualMachineInstanceReplicaSet', 
            'kubevirt.io/v1', 
            self.virtual_machine_instance_replica_set_mo,
            self.virtual_machine_instance_replica_set_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response