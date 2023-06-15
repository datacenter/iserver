import yaml


class OcpVmDeleteVm():
    def __init__(self):
        pass

    def delete_ocp_vm(self, namespace, vm_name):
        return self.kubevirt_handler.delete_namespaced_virtual_machine(namespace, vm_name)

    def delete_vm(self):
        vm_filename = self.user_input['deployment']['vm']
        yaml_content = self.user_input['files'][vm_filename]
        content = yaml.safe_load(yaml_content)

        namespace = content['metadata']['namespace']
        name = content['metadata']['name']

        is_running = self.is_ocp_vmi_mo(
            namespace,
            name
        )

        is_defined = self.is_ocp_vm_mo(
            namespace,
            name
        )

        if not is_running:
            self.my_output.default(
                'Virtual machine instance %s/%s does not exist' % (
                    namespace,
                    name
                )
            )

        if is_running:
            self.my_output.default(
                'Stopping virtual machine %s/%s...' % (
                    namespace,
                    name
                )
            )
            if not self.stop_ocp_vm(namespace, name):
                self.my_output.error('Virtual machine stop failed')
                return False

            self.my_output.default('Wait for virtual machine stopped...')
            if not self.wait_ocp_vm_stopped(namespace, name):
                self.my_output.error('Timed out')
                return False

        if not is_defined:
            self.my_output.default(
                'Virtual machine not defined %s/%s' % (
                    namespace,
                    name
                )
            )

        if is_defined:
            self.my_output.default(
                'Deleting virtual machine %s/%s...' % (
                    namespace,
                    name
                )
            )
            success = self.delete_ocp_vm(
                namespace,
                name
            )
            if not success:
                self.my_output.error('Virtual machine delete failed')
                return False

            self.my_output.default('Virtual machine deleted')

        return True
