import yaml
import time
from menu.common import get_confirmation


class K8sVirtualMachineCpu():
    def __init__(self):
        pass
    
    def get_virtual_machine_cpu_change_body(self, namespace, name, sockets, cores, threads):
        body = {}
        body['apiVersion'] = 'kubevirt.io/v1'
        body['kind'] = 'VirtualMachine'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['template'] = {}
        body['spec']['template']['spec'] = {}
        body['spec']['template']['spec']['domain'] = {}
        body['spec']['template']['spec']['domain']['cpu'] = {}
        body['spec']['template']['spec']['domain']['cpu']['cores'] = cores
        body['spec']['template']['spec']['domain']['cpu']['sockets'] = sockets
        body['spec']['template']['spec']['domain']['cpu']['threads'] = threads
        return body
    
    def change_virtual_machine_cpu(self, namespace, name, sockets, cores, threads, confirmation=False, my_output=None, wait=True, restart=False):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Virtual Machine CPU Change', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        info = self.get_virtual_machine(namespace, name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.error('not found')
            return False

        if my_output is not None:
            my_output.default(
                '- current sockets/cores/threads: %s/%s/%s' % (
                    info['sockets'],
                    info['cores'],
                    info['threads']
                )
            )
            my_output.default('- requested CPU topology: %s/%s/%s' % (sockets, cores, threads))

        if info['sockets'] == sockets and info['cores'] == cores and info['threads'] == threads:
            if my_output is not None:
                my_output.default('- nothing to do')
            return True

        vmi = self.get_virtual_machine_instance(namespace, name, cache_enabled=False)
        if vmi is None:
            if my_output is not None:
                my_output.default('- vm currently not running')
        else:
            if my_output is not None:
                my_output.default('- vm currenty running')
        
        body = self.get_virtual_machine_cpu_change_body(namespace, name, sockets, cores, threads)
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

        if not wait or vmi is None:
            return True

        if my_output is not None:
            my_output.default('Wait for virtual machine restart required condition check...')

        time.sleep(5)

        info = self.get_virtual_machine(namespace, name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.error('virtual machine not found')
            return False

        if not info['restartRequired']:
            if my_output is not None:
                my_output.default('Restart not required')
            return True

        if my_output is not None:
            my_output.default('Restart required')

        if not restart:
            if confirmation:
                if not get_confirmation():
                    return True
            else:
                return True

        if my_output is not None:
            my_output.default('Restart virtual machine...')

        success = self.delete_virtual_machine_instance_mo(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False

        if my_output is not None:
            my_output.default('Wait for virtual machine up')

        success = self.wait_virtual_machine_up(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True
