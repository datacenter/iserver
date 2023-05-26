import os
import socket
import yaml

from lib import log_helper
from lib import output_helper
from lib import ssh

from lib.k8s import main as k8s
from lib.ocp import settings as ocp_settings


class OcpConsole():
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

    def download_kubeadmin(self, cluster_name, installer_ip, installer_username, installer_password):
        ssh_handler = ssh.Ssh(
            installer_ip,
            installer_username,
            password=installer_password
        )
        source = './install/auth/kubeadmin-password'
        destination = os.path.join(
            self.ocp_settings_handler.get_ocp_cluster_directory(cluster_name),
            'kubeadmin'
        )
        success = ssh_handler.scp_file(
            source,
            destination,
            put=False
        )

        if not success:
            self.my_output.error('Kubeadmin password download failed')
            return None

        self.my_output.default('Kubeadmin password downloaded: %s => %s' % (source, destination))
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

    def get_ocp_cluster_console(self, cluster_name, validate=False):
        cluster = self.ocp_settings_handler.get_ocp_cluster(
            cluster_name
        )
        if cluster is None:
            return None

        cluster['__Output'] = {}

        cluster['consoleFqdn'] = 'console-openshift-console.apps.%s.%s' % (
            cluster['parameters']['ocp']['cluster']['name'],
            cluster['parameters']['ocp']['cluster']['domain']
        )
        cluster['consoleUrl'] = 'https://%s' % (
            cluster['consoleFqdn']
        )

        cluster['authFqdn'] = 'oauth-openshift.apps.%s.%s' % (
            cluster['parameters']['ocp']['cluster']['name'],
            cluster['parameters']['ocp']['cluster']['domain']
        )

        cluster['consoleIp'] = cluster['parameters']['ocp']['cluster']['ingress_vip']
        try:
            cluster['consoleDns'] = socket.gethostbyname(cluster['consoleFqdn'])
        except BaseException:
            cluster['consoleDns'] = 'not-resolved'

        if cluster['consoleIp'] == cluster['consoleDns']:
            cluster['__Output']['consoleIp'] = 'Green'
            cluster['__Output']['consoleDns'] = 'Green'
        else:
            cluster['__Output']['consoleIp'] = 'Red'
            cluster['__Output']['consoleDns'] = 'Red'

        cluster['authIp'] = cluster['parameters']['ocp']['cluster']['ingress_vip']

        try:
            cluster['authDns'] = socket.gethostbyname(cluster['authFqdn'])
        except BaseException:
            cluster['authDns'] = 'not-resolved'

        if cluster['consoleIp'] == cluster['authDns']:
            cluster['__Output']['authIp'] = 'Green'
            cluster['__Output']['authDns'] = 'Green'
        else:
            cluster['__Output']['authIp'] = 'Red'
            cluster['__Output']['authDns'] = 'Red'

        cluster['consoleUsername'] = 'kubeadmin'
        cluster['consolePassword'] = None
        if 'kubeadmin' in cluster:
            cluster['consolePassword'] = self.get_kubeadmin_password(
                cluster['kubeadmin']
            )
        else:
            filename = self.download_kubeadmin(
                cluster_name,
                cluster['parameters']['installer']['vm']['ip'],
                cluster['parameters']['installer']['vm']['username'],
                cluster['parameters']['installer']['vm']['password']
            )
            if filename is not None:
                self.ocp_settings_handler.set_ocp_cluster_parameter(
                    cluster_name,
                    'kubeadmin',
                    filename
                )
                cluster['consolePassword'] = self.get_kubeadmin_password(
                    filename
                )

        if validate:
            pass

        return cluster

    def get_ocp_clusters_console(self, validate=False):
        cluster_names = self.ocp_settings_handler.get_ocp_cluster_names()
        if cluster_names is None:
            return None

        clusters = []
        for cluster_name in cluster_names:
            clusters.append(
                self.get_ocp_cluster_console(cluster_name, validate=validate)
            )

        clusters = sorted(
            clusters,
            key=lambda i: i['name']
        )

        return clusters

    def print_ocp_cluster_console(self, info, validated=False):
        order = [
            'name',
            'parameters.ocp.installation',
            'parameters.ocp.release',
            'parameters.cni.type',
            'consoleUrl',
            'consoleIp',
            'consoleDns',
            'authFqdn',
            'authIp',
            'authDns',
            'consoleUsername',
            'consolePassword'
        ]

        headers = [
            'Name',
            'Type',
            'Release',
            'CNI',
            'Console URL',
            'Expected Resolved IP',
            'DNS Resolved IP',
            'Authentication FQDN',
            'Expected Resolved IP',
            'DNS Resolved IP',
            'Username',
            'Password'
        ]

        if validated:
            pass

        self.my_output.dictionary(
            info,
            title='OCP Console',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_ocp_clusters_console(self, clusters, validated=False):
        order = [
            'name',
            'parameters.ocp.installation',
            'parameters.ocp.release',
            'parameters.cni.type'
        ]

        headers = [
            'Name',
            'Type',
            'Release',
            'CNI'
        ]

        if validated:
            pass

        self.my_output.my_table(
            clusters,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True
        )
