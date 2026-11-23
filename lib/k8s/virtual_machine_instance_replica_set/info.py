class K8sVirtualMachineInstanceReplicaSetInfo():
    def __init__(self):
        self.virtual_machine_instance_replica_set = None

    def get_virtual_machine_instance_replica_set_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_virtual_machine_instance_replica_sets(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'virtual_machine_instance_replica_set', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_virtual_machine_instance_replica_set(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'virtual_machine_instance_replica_set', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_virtual_machine_instance_replica_set(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_virtual_machine_instance_replica_set(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_virtual_machine_instance_replica_set(self, cache_enabled=True):
        infos = self.get_virtual_machine_instance_replica_sets(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True