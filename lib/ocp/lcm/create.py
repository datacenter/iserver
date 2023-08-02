from lib.k8s import main as k8s
from lib.ocp.cluster.console import main as ocp_cluster_console
from lib.ocp.cluster.kubeconfig import main as ocp_cluster_kubeconfig


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

        ocp_kubeconfig_handler = ocp_cluster_kubeconfig.OcpClusterKubeconfig()
        kubeconfig_filename = ocp_kubeconfig_handler.download_kubeconfig(
            ocp_parameters['installer']['vm']['ip'],
            ocp_parameters['installer']['vm']['username'],
            ocp_parameters['installer']['vm']['password'],
            silent=True
        )
        if kubeconfig_filename is None:
            return False
        self.my_output.default('Kubeconfig downloaded')

        success = self.ocp_settings_handler.set_ocp_cluster(
            ocp_parameters['ocp']['name'],
            kubeconfig_filename,
            ocp_parameters
        )
        if not success:
            return False

        self.my_output.default('OCP instance configured: %s' % (ocp_parameters['ocp']['name']))

        success = ocp_kubeconfig_handler.check_kubeconfig(
            kubeconfig_filename,
            ocp_parameters['ocp']['cluster']['api_vip'],
            silent=True
        )
        if not success:
            return False

        ocp_console_handler = ocp_cluster_console.OcpClusterConsole()
        kubeadmin_filename = ocp_console_handler.download_kubeadmin(
            ocp_parameters['installer']['vm']['ip'],
            ocp_parameters['installer']['vm']['username'],
            ocp_parameters['installer']['vm']['password'],
            silent=True
        )
        if kubeadmin_filename is None:
            return False
        self.my_output.default('Kubeadmin downloaded')

        target_filename = self.ocp_settings_handler.copy_ocp_cluster_file(
            ocp_parameters['ocp']['name'],
            kubeadmin_filename,
            'kubeadmin'
        )
        if target_filename is None:
            self.my_output.error('Kubeadmin local copy failed')
            return False
        self.my_output.default('Kubeadmin copied to ocp cluster location')

        success = self.ocp_settings_handler.set_ocp_cluster_parameter(
            ocp_parameters['ocp']['name'],
            'kubeadmin',
            target_filename
        )
        if not success:
            self.my_output.error('Cluster settings failed')
            return False

        self.my_output.default('OCP instance configured: %s' % (ocp_parameters['ocp']['name']))

        k8s_handler = k8s.K8s(
            kubeconfig_filename,
            log_id=self.log_id
        )
        if not k8s_handler.connect():
            self.my_output.error('Kubernetes authentication failed')
            return False
        self.my_output.default('Kubernetes authentication successful with local kubeconfig')

        return True
