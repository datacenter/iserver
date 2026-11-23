from menu.common import get_confirmation


class K8sVirtualMachineUnpause():
    def __init__(self):
        pass
    
    def unpause_virtual_machine(self, ssh_handler, namespace, name, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Unpause Virtual Machine', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        info = self.get_virtual_machine(namespace, name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.error('not found')
            return False

        if my_output is not None:
            my_output.default('- state: %s' % (info['status']))

        if info['status'] == 'Running':
            if my_output is not None:
                my_output.default('- already running')
            return True

        if info['status'] != 'Paused':
            if my_output is not None:
                my_output.error('paused state expected')
            return False

        if confirmation:
            if not get_confirmation('Unpause virtual machine'):
                return False
            
        success, output, error = ssh_handler.run_cmd('virtctl unpause vm %s' % (name))
        if not success:
            if my_output is not None:
                my_output.error('virtctl unpause failed')
                my_output.default(str(output))
                my_output.default(str(error))
            return False

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for virtual machine running')

        success = self.wait_virtual_machine_up(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True
