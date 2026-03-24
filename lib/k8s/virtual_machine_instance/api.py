import time
import traceback


class K8sVirtualMachineInstanceApi():
    def __init__(self):
        self.virtual_machine_instance_mo = None
        self.virtual_machine_instance_namespace_mo = {}

    def get_virtual_machine_instance_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.virtual_machine_instance_mo,
            self.virtual_machine_instance_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.virtual_machine_instance_mo, self.virtual_machine_instance_namespace_mo = self.get_namespaced_resources(
            'VirtualMachineInstance', 
            'kubevirt.io/v1', 
            self.virtual_machine_instance_mo,
            self.virtual_machine_instance_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
    
    def delete_virtual_machine_instance_mo(self, namespace, name):
        return self.delete_resource('VirtualMachineInstance', 'kubevirt.io/v1', name, namespace=namespace)
