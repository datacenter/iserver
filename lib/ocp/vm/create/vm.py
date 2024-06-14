import yaml


class OcpVmCreateVm():
    def __init__(self):
        pass

    def create_vm(self):
        vm_filename = self.user_input['deployment']['vm']
        vm_yaml = yaml.safe_load(self.user_input['files'][vm_filename])

        namespace = vm_yaml['metadata']['namespace']
        name = vm_yaml['metadata']['name']

        if not self.kubevirt_handler.create_namespaced_virtual_machine(vm_yaml):
            self.my_output.error(
                'Create virtual machine request failed'
            )
            return False

        self.my_output.default(
            'Virtual machine %s/%s created' % (
                namespace,
                name
            )
        )

        if not self.user_input['running']['wait']:
            self.my_output.default('Wait for virtual machine running disabled')
            return True

        if vm_yaml['spec']['running']:
            self.my_output.default('Wait for virtual machine running...')
            if not self.kubevirt_handler.wait_virtual_machine_running(namespace, name, output_handler=self.my_output):
                self.my_output.error('Timed out')
                return False

        if not vm_yaml['spec']['running']:
            self.my_output.default('Wait for virtual machine stopped...')
            if not self.kubevirt_handler.wait_virtual_machine_stopped(namespace, name):
                self.my_output.error('Timed out')
                return False

        return True
