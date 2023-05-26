import os
import socket
import yaml

from lib import log_helper
from lib import output_helper
from lib import ssh

from lib.k8s import main as k8s
from lib.ocp import settings as ocp_settings


class OcpKubeconfig():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)
        self.log_id = log_id
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )
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

    def get_ocp_cluster_kubeconfig(self, cluster_name, validate=False):
        cluster = self.ocp_settings_handler.get_ocp_cluster(
            cluster_name
        )
        if cluster is None:
            return None

        cluster['__Output'] = {}

        cluster['kubeconfigFile'] = os.path.isfile(cluster['kubeconfig'])
        if cluster['kubeconfigFile']:
            cluster['kubeconfigFileTick'] = '\u2713'
            cluster['__Output']['kubeconfigFileTick'] = 'Green'
        else:
            cluster['kubeconfigFileTick'] = '\u2717'
            cluster['__Output']['kubeconfigFileTick'] = 'Red'

        cluster['apiFqdn'] = ''
        cluster['apiVip'] = ''
        cluster['apiDns'] = ''
        if validate:
            cluster['kubeApi'] = False
            cluster['kubeApiTick'] = '\u2717'
            cluster['__Output']['kubeApiTick'] = 'Red'

        if not cluster['kubeconfigFile']:
            return cluster

        kubeconfig_content = self.get_kubeconfig(cluster['kubeconfig'])
        if kubeconfig_content is None:
            return cluster

        cluster['apiFqdn'] = self.get_cluster_name(kubeconfig_content)
        if cluster['apiFqdn'] is None:
            return cluster

        cluster['apiVip'] = cluster['parameters']['ocp']['cluster']['api_vip']

        try:
            cluster['apiDns'] = socket.gethostbyname(cluster['apiFqdn'])
        except BaseException:
            cluster['apiDns'] = 'not-resolved'
            cluster['__Output']['apiDns'] = 'Red'
            return cluster

        if cluster['apiVip'] != cluster['apiDns']:
            cluster['__Output']['apiVip'] = 'Red'
            cluster['__Output']['apiDns'] = 'Red'
            return cluster

        cluster['__Output']['apiFqdn'] = 'Green'
        cluster['__Output']['apiVip'] = 'Green'
        cluster['__Output']['apiDns'] = 'Green'

        if validate:
            k8s_handler = k8s.K8s(
                cluster['kubeconfig'],
                log_id=self.log_id
            )
            if k8s_handler.connect():
                cluster['kubeApi'] = k8s_handler.is_connected()
                if cluster['kubeApi']:
                    cluster['kubeApiTick'] = '\u2713'
                    cluster['__Output']['kubeApiTick'] = 'Green'

        return cluster

    def get_ocp_clusters_kubeconfig(self, validate=False):
        cluster_names = self.ocp_settings_handler.get_ocp_cluster_names()
        if cluster_names is None:
            return None

        clusters = []
        for cluster_name in cluster_names:
            clusters.append(
                self.get_ocp_cluster_kubeconfig(cluster_name, validate=validate)
            )

        clusters = sorted(
            clusters,
            key=lambda i: i['name']
        )

        return clusters

    def print_ocp_cluster_kubeconfig(self, info, validated=False):
        order = [
            'name',
            'parameters.ocp.installation',
            'parameters.ocp.release',
            'parameters.cni.type',
            'kubeconfigFileTick',
            'apiFqdn',
            'apiVip',
            'apiDns'
        ]

        headers = [
            'Name',
            'Type',
            'Release',
            'CNI',
            'Kubeconfig',
            'API FQDN',
            'API VIP',
            'API DNS'
        ]

        if validated:
            order.append('kubeApiTick')
            headers.append('K8s API')

        self.my_output.dictionary(
            info,
            title='OCP Kubeconfig',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_ocp_clusters_kubeconfig(self, clusters, validated=False):
        order = [
            'name',
            'parameters.ocp.installation',
            'parameters.ocp.release',
            'parameters.cni.type',
            'kubeconfigFileTick',
            'apiFqdn',
            'apiVip',
            'apiDns'
        ]

        headers = [
            'Name',
            'Type',
            'Release',
            'CNI',
            'Kubeconfig',
            'API FQDN',
            'API VIP',
            'API DNS'
        ]

        if validated:
            order.append('kubeApiTick')
            headers.append('K8s API')

        self.my_output.my_table(
            clusters,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )
