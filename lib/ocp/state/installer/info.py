from lib import filter_helper
from lib import ssh

from lib.ocp import settings as ocp_settings


class OcpInstallerInfo():
    def __init__(self, log_id=None):
        self.ocp_settings_handler = ocp_settings.OcpSettings(
            log_id=log_id
        )

    def get_ocp_cluster_installer_info(self, cluster_name):
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
        try:
            info['ssh'] = {}
            info['ssh']['ip'] = cluster['parameters']['installer']['vm']['ip']
            info['ssh']['username'] = cluster['parameters']['installer']['vm']['username']
            info['ssh']['password'] = cluster['parameters']['installer']['vm']['password']
        except BaseException:
            info['ssh'] = None

        return info

    def get_ocp_clusters_installer_info(self):
        cluster_names = self.ocp_settings_handler.get_ocp_cluster_names()
        if cluster_names is None:
            return None

        clusters = []
        for cluster_name in cluster_names:
            cluster_info = self.get_ocp_cluster_installer_info(
                cluster_name
            )
            if cluster_info is not None:
                clusters.append(
                    cluster_info
                )

        return clusters

    def get_ocp_cluster_installer_validation(self, cluster_info):
        if cluster_info['ssh'] is not None:
            ssh_handler = ssh.Ssh(
                cluster_info['ssh']['ip'],
                cluster_info['ssh']['username'],
                password=cluster_info['ssh']['password']
            )
            cluster_info['ssh']['validated'] = ssh_handler.is_ssh()
            if cluster_info['ssh']['validated']:
                cluster_info['ssh']['tick'] = '\u2713'
                cluster_info['__Output']['ssh.tick'] = 'Green'

        return cluster_info

    def match_ocp_cluster_installer(self, cluster_info, cluster_filter):
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

    def get_ocp_clusters_installer(self, cluster_filter=None, validate_info=False):
        all_clusters = self.get_ocp_clusters_installer_info()
        if all_clusters is None:
            return None

        clusters = []

        for cluster_info in all_clusters:
            if not self.match_ocp_cluster_installer(cluster_info, cluster_filter):
                continue

            if validate_info:
                cluster_info = self.get_ocp_cluster_installer_validation(
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
