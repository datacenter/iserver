import os
import socket

from lib import ssh
from lib import output_helper


class OcpClusterConsole():
    def __init__(self, log_id=None):
        self.log_id = log_id
        self.my_output = output_helper.OutputHelper(
            log_id=log_id
        )

    def download_kubeadmin(self, installer_ip, installer_username, installer_password, silent=False):
        ssh_handler = ssh.Ssh(
            installer_ip,
            installer_username,
            password=installer_password,
            log_id=self.log_id
        )
        source = './install/auth/kubeadmin-password'
        destination = '/tmp/kubeadmin'
        success = ssh_handler.scp_file(
            source,
            destination,
            put=False
        )

        if not success:
            if not silent:
                self.my_output.error('Kubeadmin download failed')
            return None

        if not silent:
            self.my_output.default('Kubeadmin downloaded: %s => %s' % (source, destination))
        return destination

    def is_kubeadmin_file(self, kubeadmin_filename):
        return os.path.isfile(kubeadmin_filename)

    def get_kubeadmin_password(self, kubeadmin_filename):
        try:
            with open(kubeadmin_filename, 'r', encoding='utf-8') as file_handler:
                content = file_handler.read()

        except BaseException:
            self.log.error(
                'get_kubeadmin',
                'File read failed: %s' % (kubeadmin_filename)
            )
            return None

        return content

    def get_ocp_cluster_console_info(self):
        info = {}
        info['__Output'] = {}
        info['name'] = self.ocp_cluster_settings['name']
        info['installation'] = self.ocp_cluster_settings['parameters']['ocp']['installation']
        info['release'] = self.ocp_cluster_settings['parameters']['ocp']['release']
        info['cni'] = self.ocp_cluster_settings['parameters']['cni']['type']

        info['consoleFqdn'] = 'console-openshift-console.apps.%s.%s' % (
            self.ocp_cluster_settings['parameters']['ocp']['cluster']['name'],
            self.ocp_cluster_settings['parameters']['ocp']['cluster']['domain']
        )
        info['consoleUrl'] = 'https://%s' % (
            info['consoleFqdn']
        )

        info['authFqdn'] = 'oauth-openshift.apps.%s.%s' % (
            self.ocp_cluster_settings['parameters']['ocp']['cluster']['name'],
            self.ocp_cluster_settings['parameters']['ocp']['cluster']['domain']
        )

        info['consoleIp'] = self.ocp_cluster_settings['parameters']['ocp']['cluster']['ingress_vip']
        try:
            info['consoleDns'] = socket.gethostbyname(info['consoleFqdn'])
        except BaseException:
            info['consoleDns'] = 'not-resolved'

        if info['consoleIp'] == info['consoleDns']:
            info['__Output']['consoleIp'] = 'Green'
            info['__Output']['consoleDns'] = 'Green'
        else:
            info['__Output']['consoleIp'] = 'Red'
            info['__Output']['consoleDns'] = 'Red'

        info['authIp'] = self.ocp_cluster_settings['parameters']['ocp']['cluster']['ingress_vip']

        try:
            info['authDns'] = socket.gethostbyname(info['authFqdn'])
        except BaseException:
            info['authDns'] = 'not-resolved'

        if info['consoleIp'] == info['authDns']:
            info['__Output']['authIp'] = 'Green'
            info['__Output']['authDns'] = 'Green'
        else:
            info['__Output']['authIp'] = 'Red'
            info['__Output']['authDns'] = 'Red'

        info['consoleUsername'] = 'kubeadmin'
        info['consolePassword'] = None
        if 'kubeadmin' in self.ocp_cluster_settings:
            info['consolePassword'] = self.get_kubeadmin_password(
                self.ocp_cluster_settings['kubeadmin']
            )

        return info
