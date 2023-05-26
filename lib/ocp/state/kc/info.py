import os
import socket
import yaml

from lib import filter_helper
from lib import ssh

from lib.k8s import main as k8s
from lib.ocp import settings as ocp_settings


class OcpKubeconfigInfo():
    def __init__(self, log_id=None):
        self.ocp_settings_handler = ocp_settings.OcpSettings(
            log_id=log_id
        )

    def download_kubeconfig(self, installer_ip, installer_username, installer_password):
        ssh_handler = ssh.Ssh(
            installer_ip,
            installer_username,
            password=installer_password
        )
        source = './install/auth/kubeconfig'
        destination = '/tmp/kubeconfig'
        success = ssh_handler.scp_file(
            source,
            destination,
            put=False
        )

        if not success:
            self.my_output.error('Kubeconfig download failed')
            return None

        self.my_output.default('Kubeconfig downloaded: %s => %s' % (source, destination))
        return destination

    def is_kubeconfig_file(self, kubeconfig_filename):
        return os.path.isfile(kubeconfig_filename)

    def get_kubeconfig(self, kubeconfig_filename):
        try:
            with open(kubeconfig_filename, 'rb') as file_handler:
                content = yaml.safe_load(file_handler)

        except BaseException:
            self.log.error(
                'get_kubeconfig',
                'YAML format required: %s' % (kubeconfig_filename)
            )
            return None

        return content

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

    def check_kubeconfig(self, kubeconfig_filename, api_vip):
        if not self.is_kubeconfig_file(kubeconfig_filename):
            self.my_output.error('Kubeconfig file not found: %s' % (kubeconfig_filename))
            return False

        content = self.get_kubeconfig(kubeconfig_filename)
        if content is None:
            return False

        api_server_name = self.get_cluster_name(content)
        if api_server_name is None:
            return False

        try:
            api_server_ip = socket.gethostbyname(api_server_name)

        except BaseException:
            self.my_output.error('DNS resolution failed: %s' % (api_server_name))
            self.my_output.default(
                'Expected DNS resolution (%s, %s)' % (
                    api_server_name,
                    api_vip
                )
            )
            return False

        if api_server_ip != api_vip:
            self.my_output.error(
                'DNS resolution does not match OCP cluster API VIP: (%s, %s) vs. API VIP %s' % (
                    api_server_name,
                    api_server_ip,
                    api_vip
                )
            )
            return False

        self.my_output.default('Kubeconfig validated: %s => %s' % (api_server_name, api_vip))
        return True

    def get_ocp_cluster_kubeconfig_validation(self, cluster_info):
        cluster_info['kubeApi'] = False
        cluster_info['kubeApiTick'] = '\u2717'
        cluster_info['__Output']['kubeApiTick'] = 'Red'

        kubeconfig_content = self.get_kubeconfig(cluster_info['kubeconfigFilename'])
        if kubeconfig_content is None:
            return cluster_info

        k8s_handler = k8s.K8s(
            cluster_info['kubeconfigFilename'],
            log_id=self.log_id
        )
        if k8s_handler.connect():
            cluster_info['kubeApi'] = k8s_handler.is_connected()
            if cluster_info['kubeApi']:
                cluster_info['kubeApiTick'] = '\u2713'
                cluster_info['__Output']['kubeApiTick'] = 'Green'

        return cluster_info

    def get_ocp_cluster_kubeconfig_info(self, cluster_name):
        cluster = self.ocp_settings_handler.get_ocp_cluster(
            cluster_name
        )
        if cluster is None:
            return None

        info = {}
        info['__Output'] = {}
        info['name'] = cluster_name
        info['installation'] = cluster['parameters']['ocp']['installation']
        info['release'] = cluster['parameters']['ocp']['release']
        info['cni'] = cluster['parameters']['cni']['type']

        info['kubeconfigFilename'] = cluster['kubeconfig']
        info['isKubeconfigFile'] = os.path.isfile(cluster['kubeconfig'])
        if info['isKubeconfigFile']:
            info['kubeconfigFileTick'] = '\u2713'
            info['__Output']['kubeconfigFileTick'] = 'Green'
        else:
            info['kubeconfigFileTick'] = '\u2717'
            info['__Output']['kubeconfigFileTick'] = 'Red'

        info['apiFqdn'] = ''
        info['apiVip'] = ''
        info['apiDns'] = ''

        if not info['isKubeconfigFile']:
            return info

        kubeconfig_content = self.get_kubeconfig(info['kubeconfigFilename'])
        if kubeconfig_content is None:
            return info

        info['apiFqdn'] = self.get_cluster_name(kubeconfig_content)
        if info['apiFqdn'] is None:
            return info

        info['apiVip'] = cluster['parameters']['ocp']['cluster']['api_vip']

        try:
            info['apiDns'] = socket.gethostbyname(info['apiFqdn'])
        except BaseException:
            info['apiDns'] = 'not-resolved'
            info['__Output']['apiDns'] = 'Red'
            return info

        if info['apiVip'] != info['apiDns']:
            info['__Output']['apiVip'] = 'Red'
            info['__Output']['apiDns'] = 'Red'
            return info

        info['__Output']['apiFqdn'] = 'Green'
        info['__Output']['apiVip'] = 'Green'
        info['__Output']['apiDns'] = 'Green'

        return info

    def get_ocp_clusters_kubeconfig_info(self):
        cluster_names = self.ocp_settings_handler.get_ocp_cluster_names()
        if cluster_names is None:
            return None

        clusters = []
        for cluster_name in cluster_names:
            cluster_info = self.get_ocp_cluster_kubeconfig_info(
                cluster_name
            )
            if cluster_info is not None:
                clusters.append(
                    cluster_info
                )

        return clusters

    def match_ocp_cluster_kubeconfig(self, cluster_info, cluster_filter):
        if cluster_filter is None or len(cluster_filter) == 0:
            return True

        for ap_rule in cluster_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'name':
                if not filter_helper.match_string(value, cluster_info['name']):
                    return False

            if key == 'vc':
                if not filter_helper.match_string(value, cluster_info['vcenter']['name']):
                    return False

        return True

    def get_ocp_clusters_kubeconfig(self, cluster_filter=None, validate_info=False):
        all_clusters = self.get_ocp_clusters_kubeconfig_info()
        if all_clusters is None:
            return None

        clusters = []

        for cluster_info in all_clusters:
            if not self.match_ocp_cluster_kubeconfig(cluster_info, cluster_filter):
                continue

            if validate_info:
                cluster_info = self.get_ocp_cluster_kubeconfig_validation(
                    cluster_info
                )

            clusters.append(
                cluster_info
            )

        clusters = sorted(
            clusters,
            key=lambda i: i['name']
        )

        return clusters

    def get_ocp_cluster_kubeconfig(self, cluster_name):
        clusters = self.get_ocp_clusters_kubeconfig(
            cluster_filter=['name:%s' % (cluster_name)]
        )

        if clusters is None:
            return None

        if len(clusters) == 1:
            return clusters[0]

        return None
