import os
import socket

from lib import file_helper
from lib.k8s import main as k8s
from lib import ssh
from lib import output_helper


class OcpClusterKubeconfig():
    def __init__(self, log_id=None):
        self.log_id=log_id
        self.my_output = output_helper.OutputHelper(
            log_id=log_id
        )

    def download_kubeconfig(self, installer_ip, installer_username, installer_password, silent=False):
        ssh_handler = ssh.Ssh(
            installer_ip,
            installer_username,
            password=installer_password,
            log_id=self.log_id
        )
        source = './install/auth/kubeconfig'
        destination = '/tmp/kubeconfig'
        success = ssh_handler.scp_file(
            source,
            destination,
            put=False
        )

        if not success:
            if not silent:
                self.my_output.error('Kubeconfig download failed')
            return None

        if not silent:
            self.my_output.default('Kubeconfig downloaded: %s => %s' % (source, destination))
        return destination

    def is_kubeconfig_file(self, kubeconfig_filename):
        return os.path.isfile(kubeconfig_filename)

    def get_cluster_name(self, content):
        try:
            api_server = content['clusters'][0]['cluster']['server']
            api_server_name = api_server[8:].split(':')[0]

        except BaseException:
            self.log.error(
                'get_cluster_name',
                'Failed getting api server value'
            )
            return None

        return api_server_name

    def check_kubeconfig(self, kubeconfig_filename, api_vip, silent=False):
        if not self.is_kubeconfig_file(kubeconfig_filename):
            if not silent:
                self.my_output.error('Kubeconfig file not found: %s' % (kubeconfig_filename))
            return False

        content = file_helper.get_file_yaml(
            kubeconfig_filename
        )
        if content is None:
            return False

        api_server_name = self.get_cluster_name(content)
        if api_server_name is None:
            return False

        try:
            api_server_ip = socket.gethostbyname(api_server_name)

        except BaseException:
            if not silent:
                self.my_output.error('DNS resolution failed: %s' % (api_server_name))
                self.my_output.default(
                    'Expected DNS resolution (%s, %s)' % (
                        api_server_name,
                        api_vip
                    )
                )
            return False

        if api_server_ip != api_vip:
            if not silent:
                self.my_output.error(
                    'DNS resolution does not match OCP cluster API VIP: (%s, %s) vs. API VIP %s' % (
                        api_server_name,
                        api_server_ip,
                        api_vip
                    )
                )
            return False

        if not silent:
            self.my_output.default('Kubeconfig validated: %s => %s' % (api_server_name, api_vip))
        return True

    def get_ocp_cluster_kubeconfig_info(self, validate=False):
        info = {}
        info['__Output'] = {}

        info['name'] = self.ocp_cluster_settings['name']
        info['kubeconfigFilename'] = self.ocp_cluster_settings['kubeconfig']
        info['kubeconfigFile'] = os.path.isfile(
            self.ocp_cluster_settings['kubeconfig']
        )
        if info['kubeconfigFile']:
            info['kubeconfigFileTick'] = '\u2713'
            info['__Output']['kubeconfigFileTick'] = 'Green'
            info['__Output']['kubeconfigFilename'] = 'Green'
        else:
            info['kubeconfigFileTick'] = '\u2717'
            info['__Output']['kubeconfigFileTick'] = 'Red'
            info['__Output']['kubeconfigFilename'] = 'Red'

        info['apiFqdn'] = ''
        info['apiVip'] = ''
        info['apiDns'] = ''
        if validate:
            info['kubeApi'] = False
            info['kubeApiTick'] = '\u2717'
            info['__Output']['kubeApiTick'] = 'Red'

        if not info['kubeconfigFile']:
            return info

        kubeconfig_content = file_helper.get_file_yaml(
            self.ocp_cluster_settings['kubeconfig']
        )
        if kubeconfig_content is None:
            self.log.error(
                'get_ocp_cluster_kubeconfig',
                'File read failed: %s' % (
                    self.ocp_cluster_settings['kubeconfig']
                )
            )
            return info

        info['apiFqdn'] = self.get_cluster_name(kubeconfig_content)
        if info['apiFqdn'] is None:
            return info

        try:
            info['apiVip'] = socket.gethostbyname(info['apiFqdn'])
        except BaseException:
            info['apiVip'] = 'not-resolved'
            info['__Output']['apiDns'] = 'Red'
            return info

        info['__Output']['apiFqdn'] = 'Green'
        info['__Output']['apiVip'] = 'Green'

        if validate:
            k8s_handler = k8s.K8s(info['kubeconfigFilename'])
            if k8s_handler.get_api() is not None:
                info['kubeApi'] = True
                info['kubeApiTick'] = '\u2713'
                info['__Output']['kubeApiTick'] = 'Green'

        return info
