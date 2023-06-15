import time


class OcpVmCreateVmi():
    def __init__(self):
        pass

    def is_ocp_vm_running(self, namespace, vm_name, cache=True):
        vm_mo = self.get_ocp_vm_mo(
            namespace,
            vm_name,
            cache=cache
        )
        if vm_mo is None:
            return False

        if 'status' not in vm_mo or vm_mo['status'] is None:
            return False

        if 'printable_status' not in vm_mo['status']:
            return False

        if vm_mo['status']['printable_status'] == 'Running':
            return True

        return False

    def wait_ocp_vm_running(self, namespace, vm_name, timeout=300):
        start_time = int(time.time())
        while True:
            if self.is_ocp_vm_running(namespace, vm_name, cache=False):
                return True

            if int(time.time()) - start_time > timeout:
                return False

            time.sleep(5)

    def start_ocp_vm(self, namespace, vm_name):
        body = {}
        body['spec'] = {}
        body['spec']['running'] = True

        return self.kubevirt_handler.patch_namespaced_virtual_machine(namespace, vm_name, body)

    def restart_ocp_vm(self, namespace, vm_name):
        return self.kubevirt_handler.delete_namespaced_virtual_machine_instance(namespace, vm_name)
