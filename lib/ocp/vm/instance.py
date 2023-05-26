import time


class OcpVmInstance():
    def __init__(self):
        self.vmis = None

    def is_ocp_vm_running(self, namespace, vm_name, cache=True):
        vm_mo = self.get_ocp_vm(
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

    def is_ocp_vm_stopped(self, namespace, vm_name, cache=True):
        vm_mo = self.get_ocp_vm(
            namespace,
            vm_name,
            cache=cache
        )
        if vm_mo is None:
            return False

        if vm_mo['status']['printable_status'] == 'Stopped':
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

    def wait_ocp_vm_stopped(self, namespace, vm_name, timeout=300):
        start_time = int(time.time())
        while True:
            if self.is_ocp_vm_stopped(namespace, vm_name, cache=False):
                return True

            if int(time.time()) - start_time > timeout:
                return False

            time.sleep(5)

    def start_ocp_vm(self, namespace, vm_name):
        body = {}
        body['spec'] = {}
        body['spec']['running'] = True

        return self.kubevirt_handler.patch_namespaced_virtual_machine(namespace, vm_name, body)

    def stop_ocp_vm(self, namespace, vm_name):
        body = {}
        body['spec'] = {}
        body['spec']['running'] = False

        return self.kubevirt_handler.patch_namespaced_virtual_machine(namespace, vm_name, body)

    def restart_ocp_vm(self, namespace, vm_name):
        return self.kubevirt_handler.delete_namespaced_virtual_machine_instance(namespace, vm_name)

    def is_ocp_vmi(self, vmi_namespace, vmi_name):
        if self.get_ocp_vmi(vmi_namespace, vmi_name) is None:
            return False
        return True

    def get_ocp_vmi(self, vmi_namespace, vmi_name, cache=True):
        vmis = self.get_ocp_vmis(cache=cache)
        for vmi in vmis:
            if vmi['metadata']['name'] == vmi_name and vmi['metadata']['namespace'] == vmi_namespace:
                return vmi
        return None

    def get_ocp_vmis(self, cache=True):
        if cache and self.vmis is not None:
            return self.vmis
        self.vmis = self.kubevirt_handler.list_virtual_machine_instance_for_all_namespaces()
        return self.vmis
