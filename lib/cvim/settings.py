import os
import json
import shutil
import traceback

from lib import filter_helper
from lib import log_helper
from lib import output_helper
from lib.settings_helper import Settings


class CvimSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        self.cvim_settings_filename = os.path.join(
            self.settings_dir,
            'cvim'
        )

        self.cvim_clusters_directory = os.path.join(
            self.settings_dir,
            'cvim-clusters'
        )

        if not self.initialize_cvim_settings():
            raise ValueError('CVIM settings initialization failed')

    def get_cvim_default_settings(self):
        settings = {}
        settings['Enabled'] = True
        settings['Defaults'] = {}
        settings['Defaults']['Cluster'] = None
        settings['Clusters'] = []
        return settings

    def initialize_cvim_settings(self):
        if not os.path.isfile(self.cvim_settings_filename):
            settings = self.get_cvim_default_settings()
            if not self.set_cvim_settings(settings):
                return False

        if not os.path.isdir(self.cvim_clusters_directory):
            os.makedirs(
                self.cvim_clusters_directory,
                exist_ok=True
            )

        fixup = False

        settings = self.get_cvim_settings()
        for cluster in settings['Clusters']:
            for key in ['cli']:
                if key not in cluster:
                    fixup = True
                    cluster[key] = None

        if fixup:
            return self.set_cvim_settings(settings)

        return True

    def get_cvim_settings(self):
        if not os.path.isfile(self.cvim_settings_filename):
            return None

        try:
            with open(self.cvim_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_cvim_settings', traceback.format_exc())
            return None

        return settings

    def set_cvim_settings(self, settings):
        try:
            with open(self.cvim_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_cvim_settings', traceback.format_exc())
            return False

        return True

    def get_default_cluster(self):
        settings = self.get_cvim_settings()
        if settings is None:
            return None

        try:
            default_cluster_name = settings['Defaults']['Cluster']
        except BaseException:
            default_cluster_name = None

        return default_cluster_name

    def set_default_cluster(self, name):
        settings = self.get_cvim_settings()
        if settings is None:
            return False

        if 'Defaults' not in settings:
            settings['Defaults'] = {}

        settings['Defaults']['Cluster'] = name
        return self.set_cvim_settings(settings)

    def get_cvim_cluster_names(self):
        clusters = self.get_cvim_clusters()
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

    def get_cvim_clusters(self, cluster_filter=None):
        settings = self.get_cvim_settings()
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

    def get_cvim_cluster(self, cvim_name, strict_match=True):
        clusters = self.get_cvim_clusters()
        if clusters is None:
            return None

        candidates = []
        for cluster in clusters:
            if cluster['name'] == cvim_name:
                return cluster

            if not strict_match:
                if cvim_name.lower() in cluster['name'].lower():
                    candidates.append(cluster)

        if not strict_match and len(candidates) == 1:
            return candidates[0]

        return None

    def set_cvim_clusters(self, clusters):
        settings = self.get_cvim_settings()
        if settings is None:
            return False

        settings['Clusters'] = clusters
        return self.set_cvim_settings(settings)

    def get_cvim_cluster_directory(self, cvim_name):
        cluster_directory = os.path.join(
            self.cvim_clusters_directory,
            cvim_name
        )
        return cluster_directory

    def create_cvim_cluster(self, name, openrc):
        new_cluster = {}
        new_cluster['name'] = name
        new_cluster['openrc'] = self.get_cvim_cluster_openrc_filename(name)
        for key in ['cli']:
            new_cluster[key] = None

        clusters = self.get_cvim_clusters()
        if clusters is None:
            self.log.error(
                'create_cvim_cluster',
                'Failed to get clusters'
            )
            return False

        clusters.append(new_cluster)
        if not self.set_cvim_clusters(clusters):
            self.log.error(
                'create_cvim_cluster',
                'Failed to set clusters'
            )
            return False

        return self.set_cvim_cluster_openrc(name, openrc)

    def set_cvim_cluster(self, cluster_settings):
        clusters = self.get_cvim_clusters()
        if clusters is None:
            self.log.error(
                'set_cvim_cluster',
                'Failed to get clusters'
            )
            return False

        new_clusters = []
        for cluster in clusters:
            if cluster['name'] == cluster_settings['name']:
                new_clusters.append(
                    cluster_settings
                )
                continue

            new_clusters.append(
                cluster
            )

        return self.set_cvim_clusters(new_clusters)

    def get_cvim_cluster_openrc_filename(self, cvim_name):
        cluster_directory = self.get_cvim_cluster_directory(cvim_name)
        target_openrc_filename = os.path.join(
            cluster_directory,
            'openrc'
        )
        return target_openrc_filename

    def set_cvim_cluster_openrc(self, cvim_name, openrc_filename):
        if not os.path.isfile(openrc_filename):
            self.log.error(
                'set_cvim_cluster_openrc',
                'Kubeconfig file not found: %s' % (openrc_filename)
            )
            return False

        cluster = self.get_cvim_cluster(cvim_name)
        if cluster is None:
            self.log.error(
                'set_cvim_cluster_openrc',
                'Cluster not found: %s' % (cvim_name)
            )
            return False

        cluster_directory = self.get_cvim_cluster_directory(cvim_name)
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
                'set_cvim_cluster_openrc',
                'Kubeconfig file copy failed: %s => %s' % (openrc_filename, target_openrc_filename)
            )
            return False

        return self.set_cvim_cluster(cluster)

    def delete_cvim_cluster(self, cvim_name):
        clusters = self.get_cvim_clusters()
        if clusters is None:
            return False

        new_clusters = []
        for cluster in clusters:
            if cluster['name'] != cvim_name:
                new_clusters.append(cluster)

        cluster_directory = os.path.join(
            self.cvim_clusters_directory,
            cvim_name
        )
        if os.path.isdir(cluster_directory):
            shutil.rmtree(cluster_directory)

        return self.set_cvim_clusters(new_clusters)
