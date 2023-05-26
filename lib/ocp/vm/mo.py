class OcpVmMo():
    def __init__(self):
        self.vms = None

    def create_ocp_vm(self, vm_definition):
        return self.kubevirt_handler.create_namespaced_virtual_machine(vm_definition)

    def delete_ocp_vm(self, namespace, vm_name):
        return self.kubevirt_handler.delete_namespaced_virtual_machine(namespace, vm_name)

    def get_ocp_vms_by_name(self, vm_name, brief=True):
        virtual_machine_mos = self.get_ocp_vms()
        if virtual_machine_mos is None:
            return None

        vms = []
        for virtual_machine_mo in virtual_machine_mos:
            if virtual_machine_mo['metadata']['name'] == vm_name:
                if brief:
                    info = {}
                    info['name'] = virtual_machine_mo['metadata']['name']
                    info['namespace'] = virtual_machine_mo['metadata']['namespace']
                    vms.append(
                        info
                    )
                    continue

                vms.append(
                    virtual_machine_mo
                )

        return vms

    def is_ocp_vm(self, vm_namespace, vm_name, cache=True):
        if self.get_ocp_vm(vm_namespace, vm_name, cache=cache) is None:
            return False
        return True

    def get_ocp_vm_label_special(self, vm_namespace, vm_name, cache=True):
        virtual_machine_mo = self.get_ocp_vm(
            vm_namespace,
            vm_name,
            cache=cache
        )
        if virtual_machine_mo is None:
            return None

        if 'special' not in virtual_machine_mo['spec']['template']['metadata']['labels']:
            return None

        return virtual_machine_mo['spec']['template']['metadata']['labels']['special']

    def get_ocp_vm(self, vm_namespace, vm_name, cache=True):
        vms = self.get_ocp_vms(cache=cache)
        if vms is not None:
            for virtual_machine in vms:
                if virtual_machine['metadata']['name'] == vm_name and virtual_machine['metadata']['namespace'] == vm_namespace:
                    return virtual_machine
        return None

    def get_ocp_vms(self, cache=True):
        if cache and self.vms is not None:
            return self.vms
        self.vms = self.kubevirt_handler.list_virtual_machine_for_all_namespaces()
        return self.vms
