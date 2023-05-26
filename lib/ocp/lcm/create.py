from lib.k8s import main as k8s


class OcpCreate():
    def __init__(self):
        pass

    def validate_create(self):
        self.my_output.default('Input parameters verification...')
        ocp_parameters = None

        if self.ocp_type == 'vsphere-ipi':
            ocp_parameters = self.validate_vsphere_ipi_create_user_input()

        if ocp_parameters is None:
            return None

        return ocp_parameters

    def create(self):
        ocp_parameters = self.validate_create()
        if ocp_parameters is None:
            return False

        if self.ocp_type == 'vsphere-ipi':
            success = self.vsphere_ipi_ocp_create(ocp_parameters, self.ocp_user_input_location)
            if not success:
                return False

        kubeconfig_filename = self.ocp_kubeconfig_handler.download_kubeconfig(
            ocp_parameters['installer']['vm']['ip'],
            ocp_parameters['installer']['vm']['username'],
            ocp_parameters['installer']['vm']['password']
        )
        if kubeconfig_filename is None:
            return False

        success = self.ocp_settings_handler.set_ocp_cluster(
            ocp_parameters['ocp']['name'],
            kubeconfig_filename,
            ocp_parameters
        )
        if not success:
            return False

        self.my_output.default('OCP instance configured: %s' % (ocp_parameters['ocp']['name']))

        success = self.ocp_kubeconfig_handler.check_kubeconfig(
            kubeconfig_filename,
            ocp_parameters['ocp']['cluster']['api_vip']
        )
        if not success:
            return False

        k8s_handler = k8s.K8s(
            kubeconfig_filename,
            log_id=self.log_id
        )
        if not k8s_handler.connect():
            self.my_output.error('Kubernetes authentication failed')
            return False
        self.my_output.default('Kubernetes authentication successful with local kubeconfig')

        return True
