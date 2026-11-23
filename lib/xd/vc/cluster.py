import copy
from lib import ip_helper
from lib.vc import vcenter


class VcCluster():
    def __init__(self):
        self.vc_cluster = None
        self.vc_host_to_cluster = None

    def load_pre_vc_cluster(self):
        self.vc_cluster = self.get_pre_cache('vcenter', 'cluster')
        if self.vc_cluster is None:
            return False

        self.prepare_vc_cluster_mappings()
        return True

    def set_post_vc_cluster(self):
        return self.set_post_cache('vcenter-cluster', self.vc_cluster)

    def load_post_vc_cluster(self):
        self.vc_cluster = self.get_post_cache('vcenter-cluster')
        if self.vc_cluster is None:
            return False

        self.prepare_vc_cluster_mappings()
        return True

    def get_vc_cluster(self, vc):
        if vc in self.vc_cluster:
            info = copy.deepcopy(self.vc_cluster[vc])
            return info

        return None

    def get_vc_host_to_cluster(self, host):
        if host in self.vc_host_to_cluster:
            return self.vc_host_to_cluster[host]
        return None

    def prepare_vc_cluster_mappings(self):
        self.vc_host_to_cluster = {}
        for vc_instance in self.vc_cluster:
            for cluster in self.vc_cluster[vc_instance]:
                for host in cluster['hosts']:
                    self.vc_host_to_cluster[host] = cluster['name']

    def prepare_vc_clusters(self, cache_enabled=True):
        vc_instances = self.get_vc_handlers()
        if vc_instances is None or len(vc_instances) == 0:
            return False

        self.vc_cluster = {}

        for vc_instance in vc_instances:
            self.my_output.debug('Vcenter clusters: %s' % (vc_instance['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if vc_instance['name'] in self.vc_cluster:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('vcenter-%s-cluster' % (vc_instance['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.vc_cluster[vc_instance['name']] = cache
                    continue

            self.my_output.debug('Cache miss')

            vc_handler = vcenter.Vcenter(
                vc_instance['ip'],
                vc_instance['username'],
                vc_instance['password'],
                port=vc_instance['port'],
                log_id=self.log_id
            )

            self.vc_cluster[vc_instance['name']] = vc_handler.get_vm_clusters()
            if self.vc_cluster[vc_instance['name']] is None:
                return False

            for vc_cluster in self.vc_cluster[vc_instance['name']]:
                self.my_output.debug('- cluster %s' % (vc_cluster['name']))
                vc_cluster['hosts'] = vc_handler.get_vm_cluster_hosts(
                    vc_cluster['name']
                )

            self.set_cache(
                'vcenter-%s-cluster' % (vc_instance['name']),
                self.vc_cluster[vc_instance['name']]
            )

        self.prepare_vc_cluster_mappings()
        return True

    def run_vc_cluster(self):
        for vc in self.vc_instance:
            if vc not in self.vc_cluster:
                self.vc_network[vc] = []

            for cluster in self.vc_cluster[vc]:
                cluster['_name'] = cluster['name']
                cluster['vcenter'] = vc
                cluster['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        vc,
                        cluster['name']
                    )
                )

        if not self.set_post_vc_cluster():
            return False

        return True
