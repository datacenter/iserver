class OcpDelete():
    def __init__(self):
        pass

    def validate_delete(self):
        self.my_output.default('Input parameters verification...')
        ocp_parameters = None

        if self.ocp_type == 'vsphere-ipi':
            ocp_parameters = self.validate_vsphere_ipi_delete_user_input()

        if ocp_parameters is None:
            return None

        return ocp_parameters

    def delete(self):
        ocp_parameters = self.validate_delete()
        if ocp_parameters is None:
            return False

        if self.ocp_type == 'vsphere-ipi':
            success = self.vsphere_ipi_ocp_delete(ocp_parameters)
            if not success:
                return False

        success = self.ocp_settings_handler.delete_ocp_cluster(
            ocp_parameters['ocp']['name']
        )
        if not success:
            return False

        self.my_output.default('OCP instance deleted: %s' % (ocp_parameters['ocp']['name']))

        return True
