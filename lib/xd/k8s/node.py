from lib import ip_helper

from lib.k8s import settings as k8s_settings
from lib.k8s import main as k8s


class K8sNode():
    def __init__(self):
        self.k8s_node = None
        self.k8s_node_counts = None

    def load_pre_k8s_node(self):
        self.k8s_node = self.get_pre_cache('k8s', 'node')
        if self.k8s_node is None:
            return False

        return True

    def set_post_k8s_node(self):
        return self.set_post_cache('k8s-node', self.k8s_node)

    def load_post_k8s_node(self):
        self.k8s_node = self.get_post_cache('k8s-node')
        if self.k8s_node is None:
            return False

        self.run_k8s_node_counts()
        return True

    def run_k8s_node_counts(self):
        self.k8s_node_counts = {}
        for k8s_cluster_name in self.k8s_clusters:
            self.k8s_node_counts[k8s_cluster_name] = 0
            if k8s_cluster_name in self.k8s_node:
                self.k8s_node_counts[k8s_cluster_name] = len(
                    self.k8s_node[k8s_cluster_name]
                )

    def prepare_k8s_node(self, cache_enabled=True):
        self.k8s_node = {}

        success = True

        k8s_settings_handler = k8s_settings.K8sSettings(log_id=self.log_id)
        for k8s_cluster_name in self.k8s_clusters:
            self.my_output.debug('K8s cluster: %s' % (k8s_cluster_name))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if k8s_cluster_name in self.k8s_node:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('k8s-%s-node' % (k8s_cluster_name))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.k8s_node[k8s_cluster_name] = cache
                    continue

            self.my_output.debug('Cache miss')

            cluster_settings = k8s_settings_handler.get_k8s_cluster(k8s_cluster_name, strict_match=True)
            if cluster_settings is None:
                self.my_output.error('Cluster settings not found: %s' % (k8s_cluster_name))
                success = False
                self.k8s_node[k8s_cluster_name] = None
                continue

            k8s_handler = k8s.K8s(
                kubeconfig_filename=cluster_settings['kubeconfig'],
                cluster_type=cluster_settings['type'],
                log_id=self.log_id
            )

            self.k8s_node[k8s_cluster_name] = k8s_handler.get_nodes(
                sriov_phy_info=False,
                sriov_policy_info=False,
                sriov_network_info=False,
                sriov_vf_info=False,
                return_mo=False
            )
            if self.k8s_node[k8s_cluster_name] is None:
                success = False
                self.k8s_node[k8s_cluster_name] = None
                continue

        for k8s_cluster_name in self.k8s_clusters:
            self.set_cache(
                'k8s-%s-node' % (k8s_cluster_name),
                self.k8s_node[k8s_cluster_name]
            )

        return success

    def update_k8s_node_server_ref(self, cluster_name, node_name, server_name, server_moid):
        for cname in self.k8s_clusters:
            if cname != cluster_name:
                continue

            if self.k8s_node[cluster_name] is None:
                continue

            for node in self.k8s_node[cluster_name]:
                if node['name'] != node_name:
                    continue

                node['ServerName'] = server_name
                node['ServerMoid'] = server_moid

    def update_k8s_node_ethernet_counts(self, cluster_name, node_name, nns_info):
        for cname in self.k8s_clusters:
            if cname != cluster_name:
                continue

            if self.k8s_node[cluster_name] is None:
                continue

            for node in self.k8s_node[cluster_name]:
                if node['name'] != node_name:
                    continue

                for nns_item in nns_info['interface']:
                    if nns_item['type'] == 'ethernet':
                        node['EthernetCount'] += 1
                        if nns_item['state'] == 'up':
                            node['EthernetUp'] += 1

                node['EthernetSummary'] = '%s/%s' % (
                    node['EthernetUp'],
                    node['EthernetCount']
                )

    def run_k8s_node(self):
        for cluster_name in self.k8s_clusters:
            if self.k8s_node[cluster_name] is None:
                continue

            for node in self.k8s_node[cluster_name]:
                node['ServerName'] = None
                node['ServerMoid'] = None
                node['EthernetCount'] = 0
                node['EthernetUp'] = 0
                node['EthernetSummary'] = None

                node['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        cluster_name,
                        node['name']
                    )
                )

        if not self.set_post_k8s_node():
            return False

        self.run_k8s_node_counts()
        return True
