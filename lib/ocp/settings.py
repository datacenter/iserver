import os
import json
import shutil
import traceback

from lib import file_helper
from lib import filter_helper
from lib import ip_helper
from lib import log_helper
from lib import output_helper
from lib.settings_helper import Settings


class OcpSettings(Settings):
    def __init__(self, log_id=None):
        Settings.__init__(self, log_id=log_id)

        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=False,
            debug=False
        )

        self.ocp_settings_filename = os.path.join(
            self.settings_dir,
            'ocp'
        )

        self.ocp_clusters_directory = os.path.join(
            self.settings_dir,
            'ocp-clusters'
        )

        if not self.initialize_ocp_settings():
            raise ValueError('OCP settings initialization failed')

    def get_ocp_default_settings(self):
        settings = {}
        settings['Enabled'] = True
        settings['Defaults'] = {}
        settings['Defaults']['Cluster'] = None
        settings['Clusters'] = []
        return settings

    def initialize_ocp_settings(self):
        if not os.path.isfile(self.ocp_settings_filename):
            settings = self.get_ocp_default_settings()
            if not self.set_ocp_settings(settings):
                return False

        if not os.path.isdir(self.ocp_clusters_directory):
            os.makedirs(
                self.ocp_clusters_directory,
                exist_ok=True
            )

        fixup = False

        settings = self.get_ocp_settings()
        for cluster in settings['Clusters']:
            for key in ['kubeconfig', 'helm', 'virtcl', 'tools', 'ssh', 'kubeadmin']:
                if key in cluster:
                    fixup = True
                    del cluster[key]

            if 'domain' not in cluster:
                fixup = True
                cluster['domain'] = None

        if fixup:
            return self.set_ocp_settings(settings)

        return True

    def get_ocp_settings(self):
        if not os.path.isfile(self.ocp_settings_filename):
            return None

        try:
            with open(self.ocp_settings_filename, 'r', encoding='utf-8') as file_handler:
                settings = json.loads(file_handler.read())

        except BaseException:
            self.log.error('get_ocp_settings', traceback.format_exc())
            return None

        return settings

    def set_ocp_settings(self, settings):
        try:
            with open(self.ocp_settings_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(settings, indent=4))

        except BaseException:
            self.log.error('set_ocp_settings', traceback.format_exc())
            return False

        return True

    def get_default_cluster(self):
        settings = self.get_ocp_settings()
        if settings is None:
            return None

        try:
            default_cluster_name = settings['Defaults']['Cluster']
        except BaseException:
            default_cluster_name = None

        return default_cluster_name

    def set_default_cluster(self, name):
        settings = self.get_ocp_settings()
        if settings is None:
            return False

        if 'Defaults' not in settings:
            settings['Defaults'] = {}

        settings['Defaults']['Cluster'] = name
        return self.set_ocp_settings(settings)

    def get_ocp_cluster_names(self):
        clusters = self.get_ocp_clusters()
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

            if key == 'domain':
                key_found = True
                if not filter_helper.match_string(value, cluster_settings['domain']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cluster',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ocp_clusters(self, cluster_filter=None, files_info=False):
        settings = self.get_ocp_settings()
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

        for cluster in clusters:
            cluster['__Output'] = {}
            cluster['kubeconfig'] = os.path.join(
                self.get_ocp_cluster_directory(cluster['name']), 
                'kubeconfig'
            )

            if files_info:
                cluster['isKube'] = os.path.isfile(cluster['kubeconfig'])
                if cluster['isKube']:
                    cluster['isKubeTick'] = '\u2713'
                    cluster['__Output']['isKubeTick'] = 'Green'
                else:
                    cluster['isKubeTick'] = '\u2717'
                    cluster['__Output']['isKubeTick'] = 'Red'

                cluster['isKube'] = os.path.isfile(cluster['kubeconfig'])
                if cluster['isKube']:
                    cluster['isKubeTick'] = '\u2713'
                    cluster['__Output']['isKubeTick'] = 'Green'
                else:
                    cluster['isKubeTick'] = '\u2717'
                    cluster['__Output']['isKubeTick'] = 'Red'

                if self.is_management_ssh_pub(cluster['name']):
                    cluster['isSshTick'] = '\u2713'
                    cluster['__Output']['isSshTick'] = 'Green'
                else:
                    cluster['isSshTick'] = '\u2717'
                    cluster['__Output']['isSshTick'] = 'Red'
                
                cluster['management_ip'] = self.get_management_ip(cluster['name'])
                if self.is_management_ip(cluster['name']):
                    cluster['isMgmtTick'] = '\u2713'
                    cluster['__Output']['isMgmtTick'] = 'Green'
                else:
                    cluster['isMgmtTick'] = '\u2717'
                    cluster['__Output']['isMgmtTick'] = 'Red'
                
        return clusters

    def get_ocp_cluster(self, ocp_name, strict_match=True):
        clusters = self.get_ocp_clusters()
        if clusters is None:
            return None

        candidates = []
        for cluster in clusters:
            if cluster['name'] == ocp_name:
                return cluster

            if not strict_match:
                if ocp_name.lower() in cluster['name'].lower():
                    candidates.append(cluster)

        if not strict_match and len(candidates) == 1:
            return candidates[0]

        return None

    def is_ocp_cluster(self, ocp_name):
        if self.get_ocp_cluster(ocp_name) is None:
            return False
        return True

    # LCM
    def get_ocp_cluster_parameters(self, ocp_name):
        return self.get_ocp_cluster_parameter(ocp_name, 'parameters')

    # LCM
    def get_ocp_cluster_parameter(self, ocp_name, parameter_name):
        clusters = self.get_ocp_clusters()
        if clusters is None:
            return None

        for cluster in clusters:
            if cluster['name'] == ocp_name:
                if parameter_name in cluster:
                    return cluster[parameter_name]

        return None

    # LCM, kubeadmin, cluster_id
    def set_ocp_cluster_parameter(self, ocp_name, parameter_name, parameter_value):
        clusters = self.get_ocp_clusters()
        if clusters is None:
            return None

        for cluster in clusters:
            if cluster['name'] == ocp_name:
                cluster[parameter_name] = parameter_value

        return self.set_ocp_clusters(clusters)

    def set_ocp_clusters(self, clusters):
        settings = self.get_ocp_settings()
        if settings is None:
            return False

        settings['Clusters'] = clusters
        return self.set_ocp_settings(settings)

    def get_ocp_cluster_directory(self, ocp_name):
        cluster_directory = os.path.join(
            self.ocp_clusters_directory,
            ocp_name
        )
        return cluster_directory

    def copy_ocp_cluster_file(self, ocp_name, source_filename, destination_filename):
        if not os.path.isfile(source_filename):
            self.log.error(
                'copy_ocp_cluster_file',
                'Source file not found: %s' % (source_filename)
            )
            return None

        cluster_directory = self.get_ocp_cluster_directory(ocp_name)
        if not os.path.isdir(cluster_directory):
            self.log.error(
                'copy_ocp_cluster_file',
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
                'copy_ocp_cluster_file',
                'File copy failed: %s => %s' % (source_filename, target_filename)
            )
            return None

        return target_filename

    def create_ocp_cluster(self, name, kubeconfig, domain=None):
        new_cluster = {}
        new_cluster['name'] = name
        new_cluster['domain'] = domain
        clusters = self.get_ocp_clusters()
        if clusters is None:
            self.log.error(
                'create_ocp_cluster',
                'Failed to get clusters'
            )
            return False

        clusters.append(new_cluster)
        if not self.set_ocp_clusters(clusters):
            self.log.error(
                'create_ocp_cluster',
                'Failed to set clusters'
            )
            return False

        return self.set_ocp_cluster_kubeconfig(name, kubeconfig)

    def set_ocp_cluster(self, cluster_settings):
        clusters = self.get_ocp_clusters()
        if clusters is None:
            self.log.error(
                'set_ocp_cluster',
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

        return self.set_ocp_clusters(new_clusters)

    def get_ocp_cluster_kubeconfig_filename(self, ocp_name):
        cluster_directory = self.get_ocp_cluster_directory(ocp_name)
        target_kubeconfig_filename = os.path.join(
            cluster_directory,
            'kubeconfig'
        )
        return target_kubeconfig_filename

    def set_ocp_cluster_kubeconfig(self, ocp_name, kubeconfig_filename):
        if not os.path.isfile(kubeconfig_filename):
            self.log.error(
                'set_ocp_cluster_kubeconfig',
                'Kubeconfig file not found: %s' % (kubeconfig_filename)
            )
            return False

        cluster = self.get_ocp_cluster(ocp_name)
        if cluster is None:
            self.log.error(
                'set_ocp_cluster_kubeconfig',
                'Cluster not found: %s' % (ocp_name)
            )
            return False

        cluster_directory = self.get_ocp_cluster_directory(ocp_name)
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
                'set_ocp_cluster_kubeconfig',
                'Kubeconfig file copy failed: %s => %s' % (kubeconfig_filename, target_kubeconfig_filename)
            )
            return False

        return self.set_ocp_cluster(cluster)

    def set_ocp_cluster_kubeadmin(self, ocp_name, kubeadmin):
        cluster = self.get_ocp_cluster(ocp_name)
        if cluster is None:
            self.log.error(
                'set_ocp_cluster_kubeadmin',
                'Cluster not found: %s' % (ocp_name)
            )
            return False

        cluster_directory = self.get_ocp_cluster_directory(ocp_name)
        if not os.path.isdir(cluster_directory):
            os.makedirs(
                cluster_directory,
                exist_ok=True
            )

        target_kubeadmin_filename = os.path.join(
            cluster_directory,
            'kubeadmin'
        )

        success = file_helper.set_file(
            target_kubeadmin_filename,
            kubeadmin
        )

        return success

    def get_ocp_cluster_filename(self, ocp_name, filename):
        cluster = self.get_ocp_cluster(ocp_name)
        if cluster is None:
            self.log.error(
                'set_ocp_cluster_kubeadmin',
                'Cluster not found: %s' % (ocp_name)
            )
            return None

        cluster_directory = self.get_ocp_cluster_directory(ocp_name)
        if not os.path.isdir(cluster_directory):
            os.makedirs(
                cluster_directory,
                exist_ok=True
            )

        target_filename = os.path.join(
            cluster_directory,
            filename
        )

        return target_filename

    def get_ocp_cluster_file(self, ocp_name, filename):
        target_filename = self.get_ocp_cluster_filename(ocp_name, filename)
        if target_filename is None:
            return None

        content = file_helper.get_file_text(
            target_filename
        )

        return content

    def set_ocp_cluster_file(self, ocp_name, filename, content):
        cluster = self.get_ocp_cluster(ocp_name)
        if cluster is None:
            self.log.error(
                'set_ocp_cluster_kubeadmin',
                'Cluster not found: %s' % (ocp_name)
            )
            return False

        cluster_directory = self.get_ocp_cluster_directory(ocp_name)
        if not os.path.isdir(cluster_directory):
            os.makedirs(
                cluster_directory,
                exist_ok=True
            )

        target_filename = os.path.join(
            cluster_directory,
            filename
        )

        success = file_helper.set_file(
            target_filename,
            content
        )

        return success

    def delete_ocp_cluster(self, ocp_name):
        clusters = self.get_ocp_clusters()
        if clusters is None:
            return False

        new_clusters = []
        for cluster in clusters:
            if cluster['name'] != ocp_name:
                new_clusters.append(cluster)

        cluster_directory = os.path.join(
            self.ocp_clusters_directory,
            ocp_name
        )
        if os.path.isdir(cluster_directory):
            shutil.rmtree(cluster_directory)

        return self.set_ocp_clusters(new_clusters)

    def get_domain(self, cluster_name):
        settings = self.get_ocp_cluster(cluster_name)
        if settings is None:
            return None
        
        return settings['domain']

    def is_domain(self, cluster_name):
        domain = self.get_domain(cluster_name)
        if domain is None:
            return False
        return True

    def set_domain(self, cluster_name, domain_name):
        return self.set_ocp_cluster_parameter(cluster_name, 'domain', domain_name)
    
    def is_kubeconfig(self, cluster_name):
        content = self.get_ocp_cluster_file(cluster_name, 'kubeconfig')
        if content is None:
            return False
        return True

    def is_management_ssh_pub(self, cluster_name):
        content = self.get_ocp_cluster_file(cluster_name, 'ssh.pub')
        if content is None:
            return False
        return True

    def get_management_ssh_pub(self, cluster_name):
        return self.get_ocp_cluster_file(cluster_name, 'ssh.pub')
    
    def get_management_ssh_pub_filename(self, cluster_name):
        return self.get_ocp_cluster_filename(cluster_name, 'ssh.pub')
    
    def set_management_ssh_pub(self, cluster_name, filename):
        content = file_helper.get_file_text(filename)
        if content is None:
            return False

        success = self.set_ocp_cluster_file(
            cluster_name,
            'ssh.pub',
            content
        )
        return success

    def is_management_ip(self, cluster_name):
        content = self.get_ocp_cluster_file(cluster_name, 'management_ip')
        if content is None:
            return False
        return True

    def get_management_ip(self, cluster_name):
        return self.get_ocp_cluster_file(cluster_name, 'management_ip')

    def set_management_ip(self, cluster_name, ip_address):
        success = self.set_ocp_cluster_file(
            cluster_name,
            'management_ip',
            ip_address
        )
        return success

    def is_etc_hosts(self, cluster_name):
        content = self.get_ocp_cluster_file(cluster_name, 'etc_hosts')
        if content is None:
            return False
        return True

    def set_etc_hosts(self, cluster_name, content):
        success = self.set_ocp_cluster_file(
            cluster_name,
            'etc_hosts',
            content
        )
        return success

    def check_etc_hosts(self, cluster_name):
        content = self.get_ocp_cluster_file(cluster_name, 'etc_hosts')
        if content is None:
            return False, None

        success = True
        etc_hosts = []
        for line in content.split('\n'):
            etc_host = {}
            (etc_host['address'], etc_host['fqdn']) = line.split('\t')
            etc_host['resolved'] = True

            address = ip_helper.get_ip(etc_host['fqdn'])
            if address is None or address != etc_host['address']:
                etc_host['resolved'] = False
                success = False

            etc_hosts.append(
                etc_host
            )

        return success, etc_hosts
