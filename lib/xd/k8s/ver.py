from lib.k8s import settings as k8s_settings
from lib.k8s import main as k8s


class K8sVer():
    def __init__(self):
        self.k8s_ver = None

    def get_k8s_version(self, cluster_name):
        if self.k8s_ver is None:
            return None

        if cluster_name not in self.k8s_ver:
            return None

        if len(self.k8s_ver[cluster_name]) != 1:
            return None

        return self.k8s_ver[cluster_name][0]

    def get_k8s_version_ocp(self, cluster_name):
        version_info = self.get_k8s_version(cluster_name)
        if version_info is None:
            return None
        return version_info['ocp']

    def get_k8s_version_kube(self, cluster_name):
        version_info = self.get_k8s_version(cluster_name)
        if version_info is None:
            return None
        return version_info['version']

    def load_pre_k8s_ver(self):
        self.k8s_ver = self.get_pre_cache('k8s', 'ver')
        if self.k8s_ver is None:
            return False

        return True

    def set_post_k8s_ver(self):
        return self.set_post_cache('k8s-ver', self.k8s_ver)

    def load_post_k8s_ver(self):
        self.k8s_ver = self.get_post_cache('k8s-ver')
        if self.k8s_ver is None:
            return False

        return True

    def prepare_k8s_ver(self, cache_enabled=True):
        self.k8s_ver = {}

        success = True

        k8s_settings_handler = k8s_settings.K8sSettings(log_id=self.log_id)
        for k8s_cluster_name in self.k8s_clusters:
            self.my_output.debug('K8s cluster: %s' % (k8s_cluster_name))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if k8s_cluster_name in self.k8s_ver:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('k8s-%s-ver' % (k8s_cluster_name))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.k8s_ver[k8s_cluster_name] = cache
                    continue

            self.my_output.debug('Cache miss')

            cluster_settings = k8s_settings_handler.get_k8s_cluster(k8s_cluster_name, strict_match=True)
            if cluster_settings is None:
                self.my_output.error('Cluster settings not found: %s' % (k8s_cluster_name))
                success = False
                self.k8s_ver[k8s_cluster_name] = None
                continue

            k8s_handler = k8s.K8s(
                kubeconfig_filename=cluster_settings['kubeconfig'],
                cluster_type=cluster_settings['type'],
                log_id=self.log_id
            )

            self.k8s_ver[k8s_cluster_name] = k8s_handler.get_versions(
                return_mo=False
            )
            if self.k8s_ver[k8s_cluster_name] is None:
                success = False
                self.k8s_ver[k8s_cluster_name] = None
                continue

        for k8s_cluster_name in self.k8s_clusters:
            self.set_cache(
                'k8s-%s-ver' % (k8s_cluster_name),
                self.k8s_ver[k8s_cluster_name]
            )

        return success

    def run_k8s_ver(self):
        if not self.set_post_k8s_ver():
            return False

        return True
