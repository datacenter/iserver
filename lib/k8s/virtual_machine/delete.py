from menu.common import get_confirmation


class K8sVirtualMachineDelete():
    def __init__(self):
        pass
        
    def delete_virtual_machine(self, namespace, name, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Delete Virtual Machine', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        info = self.get_virtual_machine(namespace, name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.error('not found')
            return False

        if my_output is not None:
            my_output.default('- state: %s' % (info['status']))

        vmi = self.get_virtual_machine_instance(namespace, name, cache_enabled=False)
        if vmi is not None:
            if my_output is not None:
                my_output.default('- vmi found <=> vm currently running')
            return False

        if my_output is not None:
            my_output.default('- vmi not found <=> vm stopped')

        if confirmation:
            if not get_confirmation():
                return False
            
        success = self.delete_virtual_machine_mo(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False
        
        if my_output is not None:
            my_output.default('Virtual machine deleted', before_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for virtual machine gone')

        success = self.wait_no_virtual_machine(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return success
