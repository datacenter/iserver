import os
import socket

from lib import file_helper
from lib.k8s import main as k8s
from lib.ocp.cluster.console import main as ocp_cluster_console
from lib.ocp.cluster.kubeconfig import main as ocp_cluster_kubeconfig


class OcpCreate():
    def __init__(self):
        pass

    def validate_dns_resolution(self, name, ip_address):
        try:
            api_resolved_ip = socket.gethostbyname(name)

        except BaseException:
            self.my_output.error('DNS resolution failed: %s' % (name))
            self.my_output.default(
                'Expected DNS resolution (%s, %s)' % (
                    name,
                    ip_address
                )
            )
            return False

        if api_resolved_ip != ip_address:
            self.my_output.default(
                'Expected DNS resolution (%s, %s)' % (
                    name,
                    ip_address
                )
            )
            return False

        self.my_output.default('DNS resolved: (%s, %s)' % (name, ip_address))
        return True

    def validate_dns(self, ocp_parameters):
        name = 'api.%s.%s' % (
            ocp_parameters['ocp']['cluster']['name'],
            ocp_parameters['ocp']['cluster']['domain']
        )
        ip_address = ocp_parameters['ocp']['cluster']['api_vip']

        if not self.validate_dns_resolution(name, ip_address):
            return False

        name = 'oauth-openshift.apps.%s.%s' % (
            ocp_parameters['ocp']['cluster']['name'],
            ocp_parameters['ocp']['cluster']['domain']
        )
        ip_address = ocp_parameters['ocp']['cluster']['ingress_vip']

        if not self.validate_dns_resolution(name, ip_address):
            return False

        name = 'console-openshift-console.apps.%s.%s' % (
            ocp_parameters['ocp']['cluster']['name'],
            ocp_parameters['ocp']['cluster']['domain']
        )
        ip_address = ocp_parameters['ocp']['cluster']['ingress_vip']

        if not self.validate_dns_resolution(name, ip_address):
            return False

        return True

    def validate_create(self, input_location):
        self.my_output.default('Input parameters verification...')
        ocp_parameters = None

        if self.ocp_type == 'vsphere-ipi':
            ocp_parameters = self.validate_vsphere_ipi_create_user_input()

        if ocp_parameters is None:
            return None

        if not self.validate_dns(ocp_parameters):
            return None

        if ocp_parameters['cni']['type'] == 'Cilium':
            cilium_config_filename = os.path.join(
                input_location,
                'cilium_config.yaml'
            )

            if not os.path.isfile(cilium_config_filename):
                self.my_output.error('Cilium configuration expected: %s' % (cilium_config_filename))
                return None

            cilium_config_content = file_helper.get_file_yaml(cilium_config_filename)
            if cilium_config_content is None:
                self.my_output.error('Cilium configuration yaml expected: %s' % (cilium_config_filename))
                return None

            self.my_output.default('Cilium configuration valid: %s' % (cilium_config_filename))

        return ocp_parameters

    def create(self):
        ocp_parameters = self.validate_create(self.ocp_user_input_location)
        if ocp_parameters is None:
            return False

        if self.ocp_type == 'vsphere-ipi':
            success = self.vsphere_ipi_ocp_create(ocp_parameters, self.ocp_user_input_location)
            if not success:
                return False

        ocp_kubeconfig_handler = ocp_cluster_kubeconfig.OcpClusterKubeconfig(log_id=self.log_id)
        kubeconfig_filename = ocp_kubeconfig_handler.download_kubeconfig(
            ocp_parameters['installer']['vm']['ip'],
            ocp_parameters['installer']['vm']['username'],
            ocp_parameters['installer']['vm']['password'],
            silent=True
        )
        if kubeconfig_filename is None:
            return False
        self.my_output.default('Kubeconfig downloaded')

        if self.ocp_settings_handler.is_ocp_cluster(ocp_parameters['ocp']['name']):
            success = self.ocp_settings_handler.set_ocp_cluster_kubeconfig(
                ocp_parameters['ocp']['name'],
                kubeconfig_filename
            )
            if not success:
                self.my_output.error('Failed to set ocp cluster kubeconfig locally')
                return False
            self.my_output.default('OCP instance configured: %s' % (ocp_parameters['ocp']['name']))
        else:
            success = self.ocp_settings_handler.create_ocp_cluster(
                ocp_parameters['ocp']['name'],
                kubeconfig_filename
            )
            if not success:
                self.my_output.error('Failed to create ocp cluster locally')
                return False

            self.my_output.default('OCP instance created: %s' % (ocp_parameters['ocp']['name']))

        success = ocp_kubeconfig_handler.check_kubeconfig(
            kubeconfig_filename,
            ocp_parameters['ocp']['cluster']['api_vip'],
            silent=False
        )
        if not success:
            return False

        ocp_console_handler = ocp_cluster_console.OcpClusterConsole(
            log_id=self.log_id
        )
        kubeadmin_filename = ocp_console_handler.download_kubeadmin(
            ocp_parameters['installer']['vm']['ip'],
            ocp_parameters['installer']['vm']['username'],
            ocp_parameters['installer']['vm']['password'],
            silent=True
        )
        if kubeadmin_filename is None:
            self.my_output.default('Kubeadmin download failed')
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
        if not k8s_handler.get_namespaces():
            self.my_output.error('Kubernetes authentication failed')
            return False
        self.my_output.default('Kubernetes authentication successful with local kubeconfig')

        return True
