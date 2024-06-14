import os
import json
import socket
import shutil
import traceback

from lib import file_helper
from lib import filter_helper
from lib import log_helper
from lib.settings_helper import Settings
from lib.ocp import settings as ocp_settings


class K8sSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)

        self.k8s_settings_filename = os.path.join(
            self.settings_dir,
            'k8s'
        )

        self.k8s_clusters_directory = os.path.join(
            self.settings_dir,
            'k8s-clusters'
        )

        if not self.initialize_k8s_settings():
            raise ValueError('K8s settings initialization failed')

    def get_k8s_default_settings(self):
        settings = {}
        settings['Enabled'] = True
        settings['Defaults'] = {}
        settings['Defaults']['Cluster'] = None
        settings['Clusters'] = []
        return settings

    def initialize_k8s_settings(self):
        if not os.path.isfile(self.k8s_settings_filename):
            settings = self.get_k8s_default_settings()
            if not self.set_k8s_settings(settings):
                return False

        if not os.path.isdir(self.k8s_clusters_directory):
            os.makedirs(
                self.k8s_clusters_directory,
                exist_ok=True
            )

        if not self.import_ocp_settings():
            return False

        return True

    def delete_ocp_clusters(self):
        clusters = self.get_k8s_clusters()
        if clusters is not None:
            for cluster in clusters:
                if cluster['type'] == 'ocp' and cluster['source'] == 'import':
                    if not self.delete_k8s_cluster(cluster['name']):
                        self.log.error(
                            'delete_ocp_clusters',
                            'Cluster delete failed: %s' % (cluster['name'])
                        )
                        return False

        return True

    def import_ocp_settings(self):
        default_cluster_name = self.get_default_cluster()

        if not self.delete_ocp_clusters():
            return False

        ocp_settings_handler = ocp_settings.OcpSettings(
            log_id=self.log_id
        )
        ocp_clusters = ocp_settings_handler.get_ocp_clusters()
        for ocp_cluster in ocp_clusters:
            if not self.set_k8s_cluster('%s' % (ocp_cluster['name']), ocp_cluster['kubeconfig'], cluster_type='ocp', cluster_source='import'):
                self.log.error(
                    'import_ocp_settings',
                    'Failed to add ocp cluster: %s' % (ocp_cluster['name'])
                )
                return False

        if self.get_k8s_cluster(default_cluster_name) is not None:
            self.set_default_cluster(default_cluster_name)

        return True

    def get_k8s_settings(self):
        if not os.path.isfile(self.k8s_settings_filename):
            return None

        try:
            with open(self.k8s_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_k8s_settings', traceback.format_exc())
            return None

        return settings

    def set_k8s_settings(self, settings):
        try:
            with open(self.k8s_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_k8s_settings', traceback.format_exc())
            return False

        return True

    def get_default_cluster(self):
        settings = self.get_k8s_settings()
        if settings is None:
            return None

        try:
            default_cluster_name = settings['Defaults']['Cluster']
        except BaseException:
            default_cluster_name = None

        return default_cluster_name

    def set_default_cluster(self, name):
        settings = self.get_k8s_settings()
        if settings is None:
            return False

        if 'Defaults' not in settings:
            settings['Defaults'] = {}

        settings['Defaults']['Cluster'] = name
        return self.set_k8s_settings(settings)

    def get_k8s_cluster_names(self):
        clusters = self.get_k8s_clusters()
        if clusters is None:
            return None

        names = []
        for cluster in clusters:
            names.append(
                cluster['name']
            )

        return names

    def match_cluster(self, cluster_settings, cluster_filter):
        if cluster_filter is None or len(cluster_filter) == 0:
            return True

        for ap_rule in cluster_filter:
            (key, value) = ap_rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cluster_settings['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cluster',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_k8s_clusters(self, cluster_filter=None):
        settings = self.get_k8s_settings()
        if settings is None:
            return None

        all_clusters = settings['Clusters']
        clusters = []
        for cluster in all_clusters:
            if not self.match_cluster(cluster, cluster_filter):
                continue

            clusters.append(
                cluster
            )

        clusters = sorted(
            clusters,
            key=lambda i: i['name']
        )

        return clusters

    def get_k8s_cluster(self, k8s_name, strict_match=True):
        clusters = self.get_k8s_clusters()
        if clusters is None:
            return None

        candidates = []
        for cluster in clusters:
            if cluster['name'] == k8s_name:
                return cluster

            if not strict_match:
                if k8s_name.lower() in cluster['name'].lower():
                    candidates.append(cluster)

        if not strict_match and len(candidates) == 1:
            return candidates[0]

        return None

    def set_k8s_clusters(self, clusters):
        settings = self.get_k8s_settings()
        if settings is None:
            return False

        settings['Clusters'] = clusters
        return self.set_k8s_settings(settings)

    def get_k8s_cluster_directory(self, k8s_name):
        cluster_directory = os.path.join(
            self.k8s_clusters_directory,
            k8s_name
        )
        return cluster_directory

    def copy_k8s_cluster_file(self, k8s_name, source_filename, destination_filename):
        if not os.path.isfile(source_filename):
            self.log.error(
                'copy_k8s_cluster_file',
                'Source file not found: %s' % (source_filename)
            )
            return None

        cluster_directory = self.get_k8s_cluster_directory(k8s_name)
        if not os.path.isdir(cluster_directory):
            self.log.error(
                'copy_k8s_cluster_file',
                'OCP directory not found: %s' % (cluster_directory)
            )
            return None

        target_filename = os.path.join(
            cluster_directory,
            destination_filename
        )
        shutil.copy(
            source_filename,
            target_filename
        )
        if not os.path.isfile(target_filename):
            self.log.error(
                'copy_k8s_cluster_file',
                'File copy failed: %s => %s' % (source_filename, target_filename)
            )
            return None

        return target_filename

    def set_k8s_cluster(self, k8s_name, kubeconfig_filename, cluster_type='standard', cluster_source='user'):
        if not os.path.isfile(kubeconfig_filename):
            self.log.error(
                'set_k8s_cluster',
                'Kubeconfig file not found: %s' % (kubeconfig_filename)
            )
            return False

        clusters = self.get_k8s_clusters()
        if clusters is None:
            return False

        new_clusters = []
        for cluster in clusters:
            if cluster['name'] != k8s_name:
                new_clusters.append(cluster)

        cluster_directory = self.get_k8s_cluster_directory(k8s_name)
        if not os.path.isdir(cluster_directory):
            os.makedirs(
                cluster_directory,
                exist_ok=True
            )

        target_kubeconfig_filename = os.path.join(
            cluster_directory,
            'kubeconfig'
        )

        shutil.copy(
            kubeconfig_filename,
            target_kubeconfig_filename
        )
        if not os.path.isfile(target_kubeconfig_filename):
            self.log.error(
                'set_k8s_cluster',
                'Kubeconfig file copy failed: %s => %s' % (kubeconfig_filename, target_kubeconfig_filename)
            )
            return False

        new_cluster = {}
        new_cluster['name'] = k8s_name
        new_cluster['kubeconfig'] = target_kubeconfig_filename
        new_cluster['type'] = cluster_type
        new_cluster['source'] = cluster_source
        new_clusters.append(new_cluster)

        return self.set_k8s_clusters(new_clusters)

    def delete_k8s_cluster(self, k8s_name):
        clusters = self.get_k8s_clusters()
        if clusters is None:
            return False

        default_cluster = self.get_default_cluster()
        if default_cluster is not None and default_cluster == k8s_name:
            self.set_default_cluster(None)

        new_clusters = []
        for cluster in clusters:
            if cluster['name'] != k8s_name:
                new_clusters.append(cluster)

        cluster_directory = os.path.join(
            self.k8s_clusters_directory,
            k8s_name
        )
        if os.path.isdir(cluster_directory):
            shutil.rmtree(cluster_directory)

        return self.set_k8s_clusters(new_clusters)

    def get_cluster_kubeconfig_filename(self, cluster_name):
        cluster_settings = self.get_k8s_cluster(cluster_name)
        if cluster_settings is None:
            return None
        return cluster_settings['kubeconfig']

    def get_cluster_kubeconfig_server_name(self, content):
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

    def get_cluster_kubeconfig_info(self, cluster_name):
        info = {}
        info['__Output'] = {}

        info['name'] = cluster_name
        info['kubeconfigFilename'] = self.get_cluster_kubeconfig_filename(
            cluster_name
        )
        if info['kubeconfigFilename'] is None:
            return None

        info['isKubeconfigFile'] = os.path.isfile(
            info['kubeconfigFilename']
        )
        if info['isKubeconfigFile']:
            info['isKubeconfigFileTick'] = '\u2713'
            info['__Output']['isKubeconfigFileTick'] = 'Green'
        else:
            info['isKubeconfigFile'] = '\u2717'
            info['__Output']['isKubeconfigFileTick'] = 'Red'

        info['apiFqdn'] = ''
        info['apiVip'] = ''
        info['apiDns'] = ''

        if not info['isKubeconfigFile']:
            return info

        kubeconfig_content = file_helper.get_file_yaml(
            info['kubeconfigFilename']
        )
        if kubeconfig_content is None:
            self.log.error(
                'get_ocp_cluster_kubeconfig',
                'File read failed: %s' % (
                    info['kubeconfigFilename']
                )
            )
            return info

        info['apiFqdn'] = self.get_cluster_kubeconfig_server_name(kubeconfig_content)
        if info['apiFqdn'] is None:
            return info

        try:
            info['apiVip'] = socket.gethostbyname(info['apiFqdn'])
        except BaseException:
            info['apiVip'] = 'not-resolved'
            return info

        return info

    def get_clusters_kubeconfig_info(self):
        cluster_names = self.get_k8s_cluster_names()
        if cluster_names is None:
            return None

        clusters_info = []
        for cluster_name in cluster_names:
            cluster_info = self.get_cluster_kubeconfig_info(cluster_name)
            if cluster_info is None:
                continue

            clusters_info.append(
                cluster_info
            )

        return clusters_info
