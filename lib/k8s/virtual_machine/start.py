import yaml
from menu.common import get_confirmation


class K8sVirtualMachineStart():
    def __init__(self):
        pass
    
    def get_start_body_running(self, namespace, name):
        body = {}
        body['apiVersion'] = 'kubevirt.io/v1'
        body['kind'] = 'VirtualMachine'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['running'] = True
        return body

    def get_start_body_run_strategy(self, namespace, name):
        body = {}
        body['apiVersion'] = 'kubevirt.io/v1'
        body['kind'] = 'VirtualMachine'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['runStrategy'] = 'Always'
        return body
    
    def start_virtual_machine(self, namespace, name, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Start Virtual Machine', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        info = self.get_virtual_machine(namespace, name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.error('not found')
            return False

        if my_output is not None:
            my_output.default('- state: %s' % (info['status']))
            if info['run_strategy'] is not None:
                my_output.default('- runStrategy: %s' % info['run_strategy'])
            if info['running'] is not None:
                my_output.default('- running: %s' % info['running'])

        vmi = self.get_virtual_machine_instance(namespace, name, cache_enabled=False)
        if vmi is not None:
            if my_output is not None:
                my_output.default('- vmi found <=> vm already started')
            return True
        
        if my_output is not None:
            my_output.default('- vmi not found <=> vm currently not running')

        if info['running'] is not None:
            body = self.get_start_body_running(namespace, name)
            if my_output is not None:
                my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

            if confirmation:
                if not get_confirmation():
                    return False
            
            success, reason = self.patch_virtual_machine_mo(body)
            if not success:
                if my_output is not None:
                    my_output.error('rest api failed: %s' % (reason))
                return False
            
            if my_output is not None:
                my_output.default('Virtual machine patched', before_newline=True)

        if info['run_strategy'] is not None:
            body = self.get_start_body_run_strategy(namespace, name)
            if my_output is not None:
                my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

            if confirmation:
                if not get_confirmation():
                    return False
            
            success, reason = self.patch_virtual_machine_mo(body)
            if not success:
                if my_output is not None:
                    my_output.error('rest api failed: %s' % (reason))
                return False
            
            if my_output is not None:
                my_output.default('Virtual machine patched', before_newline=True)
                        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for virtual machine up')

        success = self.wait_virtual_machine_up(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True
