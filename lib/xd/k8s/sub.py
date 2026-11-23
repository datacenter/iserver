from lib.k8s import settings as k8s_settings
from lib.k8s import main as k8s


class K8sSub():
    def __init__(self):
        self.k8s_sub = None

    def get_k8s_sub(self, cluster_name):
        if self.k8s_sub is None:
            return None

        if cluster_name not in self.k8s_sub:
            return None

        return self.k8s_sub[cluster_name]

    def load_pre_k8s_sub(self):
        self.k8s_sub = self.get_pre_cache('k8s', 'sub')
        if self.k8s_sub is None:
            return False

        return True

    def set_post_k8s_sub(self):
        return self.set_post_cache('k8s-sub', self.k8s_sub)

    def load_post_k8s_sub(self):
        self.k8s_sub = self.get_post_cache('k8s-sub')
        if self.k8s_sub is None:
            return False

        return True

    def prepare_k8s_sub(self, cache_enabled=True):
        self.k8s_sub = {}

        success = True

        k8s_settings_handler = k8s_settings.K8sSettings(log_id=self.log_id)
        for k8s_cluster_name in self.k8s_clusters:
            self.my_output.debug('K8s cluster: %s' % (k8s_cluster_name))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if k8s_cluster_name in self.k8s_sub:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('k8s-%s-sub' % (k8s_cluster_name))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.k8s_sub[k8s_cluster_name] = cache
                    continue

            self.my_output.debug('Cache miss')

            cluster_settings = k8s_settings_handler.get_k8s_cluster(k8s_cluster_name, strict_match=True)
            if cluster_settings is None:
                self.my_output.error('Cluster settings not found: %s' % (k8s_cluster_name))
                success = False
                self.k8s_sub[k8s_cluster_name] = None
                continue

            k8s_handler = k8s.K8s(
                kubeconfig_filename=cluster_settings['kubeconfig'],
                cluster_type=cluster_settings['type'],
                log_id=self.log_id
            )

            self.k8s_sub[k8s_cluster_name] = k8s_handler.get_subscriptions(
                return_mo=False
            )
            if self.k8s_sub[k8s_cluster_name] is None:
                success = False
                self.k8s_sub[k8s_cluster_name] = None
                continue

        for k8s_cluster_name in self.k8s_clusters:
            self.set_cache(
                'k8s-%s-sub' % (k8s_cluster_name),
                self.k8s_sub[k8s_cluster_name]
            )

        return success

    def run_k8s_sub(self):
        if not self.set_post_k8s_sub():
            return False

        return True
