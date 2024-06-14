import yaml


class OcpVmDeleteVm():
    def __init__(self):
        pass

    def delete_vm(self):
        vm_filename = self.user_input['deployment']['vm']
        yaml_content = self.user_input['files'][vm_filename]
        content = yaml.safe_load(yaml_content)

        namespace = content['metadata']['namespace']
        name = content['metadata']['name']

        is_running = self.k8s_handler.is_virtual_machine_instance(
            namespace,
            name,
            cache_enabled=False
        )

        is_defined = self.k8s_handler.is_virtual_machine(
            namespace,
            name,
            cache_enabled=False
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
            if not self.kubevirt_handler.stop_virtual_machine(namespace, name):
                self.my_output.error('Virtual machine stop failed')
                return False

            self.my_output.default('Wait for virtual machine stopped...')
            if not self.kubevirt_handler.wait_virtual_machine_stopped(namespace, name):
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
            success = self.kubevirt_handler.delete_namespaced_virtual_machine(
                namespace,
                name
            )
            if not success:
                self.my_output.error('Virtual machine delete failed')
                return False

            self.my_output.default('Virtual machine deleted')

        return True
