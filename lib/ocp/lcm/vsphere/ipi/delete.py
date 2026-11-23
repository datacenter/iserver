import json


class OcpVsphereIpiDelete():
    def __init__(self):
        self.ocp_parameters = None
        self.installer_parameters = None

    def vsphere_ipi_ocp_uninstall(self):
        self.my_output.default('Check ocp installation state...')
        if not self.is_vsphere_ipi_ocp_ready():
            self.my_output.default('OCP not installed')
            return True

        self.my_output.default('Destroy OCP cluster...')
        self.vcenter_handler.set_vm_parameters(
            self.installer_parameters
        )
        filename = self.get_template_filename('uninstall.sh')
        if not self.vcenter_handler.run_task_script(filename, live_output=True):
            return False

        return True

    def vsphere_ipi_ocp_delete(self, ocp_parameters):
        self.my_output.default('vsphere-ipi ocp delete workflow...')

        self.ocp_parameters = ocp_parameters
        self.installer_parameters = self.get_vsphere_ipi_installer_parameters()
        if self.installer_parameters is None:
            return False

        self.my_output.info(
            json.dumps(
                self.installer_parameters,
                indent=4
            )
        )

        self.my_output.default('Check installer virtual machine...')

        vm_name = self.installer_parameters['vm']['name']
        if not self.vcenter_handler.is_vm(vm_name):
            self.my_output.default('Installer VM already deleted: %s' % (vm_name))
            return True

        if not self.vsphere_ipi_ocp_uninstall():
            return False

        if not self.vcenter_handler.delete_vm(name=vm_name):
            return False

        self.my_output.default('Completed')
        return True
