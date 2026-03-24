class K8sVirtualMachineApi():
    def __init__(self):
        self.virtual_machine_mo = None
        self.virtual_machine_namespace_mo = {}

    def get_virtual_machine_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.virtual_machine_mo,
            self.virtual_machine_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.virtual_machine_mo, self.virtual_machine_namespace_mo = self.get_namespaced_resources(
            'VirtualMachine', 
            'kubevirt.io/v1', 
            self.virtual_machine_mo,
            self.virtual_machine_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
    
    def delete_virtual_machine_mo(self, namespace, name):
        return self.delete_resource('VirtualMachine', 'kubevirt.io/v1', name, namespace=namespace)
    