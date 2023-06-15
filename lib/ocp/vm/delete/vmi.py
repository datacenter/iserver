import time


class OcpVmDeleteVmi():
    def __init__(self):
        pass

    def is_ocp_vm_stopped(self, namespace, vm_name, cache=True):
        vm_mo = self.get_ocp_vm_mo(
            namespace,
            vm_name,
            cache=cache
        )
        if vm_mo is None:
            return False

        if vm_mo['status']['printable_status'] == 'Stopped':
            return True

        return False

    def wait_ocp_vm_stopped(self, namespace, vm_name, timeout=300):
        start_time = int(time.time())
        while True:
            if self.is_ocp_vm_stopped(namespace, vm_name, cache=False):
                return True

            if int(time.time()) - start_time > timeout:
                return False

            time.sleep(5)

    def stop_ocp_vm(self, namespace, vm_name):
        body = {}
        body['spec'] = {}
        body['spec']['running'] = False

        return self.kubevirt_handler.patch_namespaced_virtual_machine(namespace, vm_name, body)
