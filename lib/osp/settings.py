import os
import json
import shutil
import traceback

from lib import filter_helper
from lib import file_helper
from lib import log_helper
from lib.settings_helper import Settings
from lib.cvim import settings as cvim_settings


class OspSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)

        self.openstack_settings_filename = os.path.join(
            self.settings_dir,
            'osp'
        )

        self.openstack_clusters_directory = os.path.join(
            self.settings_dir,
            'osp-clusters'
        )

        if not self.initialize_openstack_settings():
            raise ValueError('Openstack settings initialization failed')

    def get_openstack_default_settings(self):
        settings = {}
        settings['Enabled'] = True
        settings['Defaults'] = {}
        settings['Defaults']['Cluster'] = None
        settings['Clusters'] = []
        return settings

    def initialize_openstack_settings(self):
        if not os.path.isfile(self.openstack_settings_filename):
            settings = self.get_openstack_default_settings()
            if not self.set_openstack_settings(settings):
                return False

        if not os.path.isdir(self.openstack_clusters_directory):
            os.makedirs(
                self.openstack_clusters_directory,
                exist_ok=True
            )

        if not self.import_cvim_settings():
            return False

        return True

    def delete_cvim_clusters(self):
        clusters = self.get_openstack_clusters()
        if clusters is not None:
            for cluster in clusters:
                if cluster['source'] == 'import':
                    if not self.delete_openstack_cluster(cluster['name']):
                        self.log.error(
                            'delete_cvim_clusters',
                            'Cluster delete failed: %s' % (cluster['name'])
                        )
                        return False

        return True

    def import_cvim_settings(self):
        default_cluster_name = self.get_default_cluster()

        if not self.delete_cvim_clusters():
            return False

        cvim_settings_handler = cvim_settings.CvimSettings(
            log_id=self.log_id
        )
        cvim_clusters = cvim_settings_handler.get_cvim_clusters()
        for cvim_cluster in cvim_clusters:
            if not self.set_openstack_cluster('%s' % (cvim_cluster['name']), cvim_cluster['openrc'], cluster_source='import'):
                self.log.error(
                    'import_cvim_settings',
                    'Failed to add cvim cluster: %s' % (cvim_cluster['name'])
                )
                return False

        if self.get_openstack_cluster(default_cluster_name) is not None:
            self.set_default_cluster(default_cluster_name)

        return True

    def get_openstack_settings(self):
        if not os.path.isfile(self.openstack_settings_filename):
            return None

        try:
            with open(self.openstack_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_openstack_settings', traceback.format_exc())
            return None

        return settings

    def set_openstack_settings(self, settings):
        try:
            with open(self.openstack_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_openstack_settings', traceback.format_exc())
            return False

        return True

    def get_default_cluster(self):
        settings = self.get_openstack_settings()
        if settings is None:
            return None

        try:
            default_cluster_name = settings['Defaults']['Cluster']
        except BaseException:
            default_cluster_name = None

        return default_cluster_name

    def set_default_cluster(self, name):
        settings = self.get_openstack_settings()
        if settings is None:
            return False

        if 'Defaults' not in settings:
            settings['Defaults'] = {}

        settings['Defaults']['Cluster'] = name
        return self.set_openstack_settings(settings)

    def get_openstack_cluster_names(self):
        clusters = self.get_openstack_clusters()
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

    def get_openstack_clusters(self, cluster_filter=None):
        settings = self.get_openstack_settings()
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

    def get_openstack_cluster(self, openstack_name, strict_match=True):
        clusters = self.get_openstack_clusters()
        if clusters is None:
            return None

        candidates = []
        for cluster in clusters:
            if cluster['name'] == openstack_name:
                return cluster

            if not strict_match:
                if openstack_name.lower() in cluster['name'].lower():
                    candidates.append(cluster)

        if not strict_match and len(candidates) == 1:
            return candidates[0]

        return None

    def set_openstack_clusters(self, clusters):
        settings = self.get_openstack_settings()
        if settings is None:
            return False

        settings['Clusters'] = clusters
        return self.set_openstack_settings(settings)

    def get_openstack_cluster_directory(self, openstack_name):
        cluster_directory = os.path.join(
            self.openstack_clusters_directory,
            openstack_name
        )
        return cluster_directory

    def parse_openrc(self, openrc_filename):
        content = file_helper.get_file_text(openrc_filename)
        if content is None:
            self.log.error(
                'parse_openrc',
                'Openrc file read failed: %s' % (openrc_filename)
            )
            return None

        openrc_content = {}

        for line in content.split('\n'):
            if line.startswith('export '):
                (key, value) = line.split('export ')[1].split('=')
                openrc_content[key.upper()] = value

        return openrc_content

    def set_openstack_cluster(self, openstack_name, openrc_filename, cluster_type='standard', cert_filename=None, cluster_source='user'):
        if not os.path.isfile(openrc_filename):
            self.log.error(
                'set_openstack_cluster',
                'Openrc file not found: %s' % (openrc_filename)
            )
            return False

        openrc_content = self.parse_openrc(
            openrc_filename
        )
        if openrc_content is None:
            return False

        if cert_filename is not None:
            if not os.path.isfile(cert_filename):
                self.log.error(
                    'set_openstack_cluster',
                    'Cert file not found: %s' % (openrc_filename)
                )
                return False

        clusters = self.get_openstack_clusters()
        if clusters is None:
            return False

        new_clusters = []
        for cluster in clusters:
            if cluster['name'] != openstack_name:
                new_clusters.append(cluster)

        cluster_directory = self.get_openstack_cluster_directory(openstack_name)
        if not os.path.isdir(cluster_directory):
            os.makedirs(
                cluster_directory,
                exist_ok=True
            )

        target_openrc_filename = os.path.join(
            cluster_directory,
            'openrc'
        )

        shutil.copy(
            openrc_filename,
            target_openrc_filename
        )
        if not os.path.isfile(target_openrc_filename):
            self.log.error(
                'set_openstack_cluster',
                'Kubeconfig file copy failed: %s => %s' % (openrc_filename, target_openrc_filename)
            )
            return False

        target_cert_filename = None
        if cert_filename is not None:
            target_cert_filename = os.path.join(
                cluster_directory,
                'cert'
            )

            shutil.copy(
                cert_filename,
                target_cert_filename
            )
            if not os.path.isfile(target_cert_filename):
                self.log.error(
                    'set_openstack_cluster',
                    'Cert file copy failed: %s => %s' % (cert_filename, target_cert_filename)
                )
                return False

            openrc_content['OS_CACERT'] = target_cert_filename

        new_cluster = {}
        new_cluster['name'] = openstack_name
        new_cluster['export'] = openrc_content
        new_cluster['openrc'] = target_openrc_filename
        new_cluster['cert'] = target_cert_filename
        new_cluster['type'] = cluster_type
        new_cluster['source'] = cluster_source

        new_clusters.append(new_cluster)

        return self.set_openstack_clusters(new_clusters)

    def delete_openstack_cluster(self, openstack_name):
        clusters = self.get_openstack_clusters()
        if clusters is None:
            return False

        default_cluster = self.get_default_cluster()
        if default_cluster is not None and default_cluster == openstack_name:
            self.set_default_cluster(None)

        new_clusters = []
        for cluster in clusters:
            if cluster['name'] != openstack_name:
                new_clusters.append(cluster)

        cluster_directory = os.path.join(
            self.openstack_clusters_directory,
            openstack_name
        )
        if os.path.isdir(cluster_directory):
            shutil.rmtree(cluster_directory)

        return self.set_openstack_clusters(new_clusters)
