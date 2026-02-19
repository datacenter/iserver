from lib import ip_helper

from lib.k8s import settings as k8s_settings
from lib.k8s import main as k8s


class K8sNns():
    def __init__(self):
        self.k8s_nns = None

    def get_k8s_nns(self, cluster_name):
        if self.k8s_nns is None:
            return None

        if cluster_name not in self.k8s_nns:
            return None

        return self.k8s_nns[cluster_name]

    def get_k8s_nns_node(self, cluster_name, node_name):
        cluster_nns = self.get_k8s_nns(cluster_name)
        if cluster_nns is None:
            return None

        for item in cluster_nns:
            if item['supported']:
                if item['owner_kind'] == 'Node' and item['owner_name'] == node_name:
                    return item

        return None

    def load_pre_k8s_nns(self, may_fail=True):
        self.k8s_nns = self.get_pre_cache('k8s', 'nns')
        if self.k8s_nns is None and not may_fail:
            return False

        return True

    def set_post_k8s_nns(self):
        return self.set_post_cache('k8s-nns', self.k8s_nns)

    def load_post_k8s_nns(self, may_fail=True):
        self.k8s_nns = self.get_post_cache('k8s-nns')
        if self.k8s_nns is None and not may_fail:
            return False

        return True

    def prepare_k8s_nns(self, cache_enabled=True):
        self.k8s_nns = {}

        success = True

        k8s_settings_handler = k8s_settings.K8sSettings(log_id=self.log_id)
        for k8s_cluster_name in self.k8s_clusters:
            self.my_output.debug('K8s cluster: %s' % (k8s_cluster_name))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if k8s_cluster_name in self.k8s_nns:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('k8s-%s-nns' % (k8s_cluster_name))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.k8s_nns[k8s_cluster_name] = cache
                    continue

            self.my_output.debug('Cache miss')

            cluster_settings = k8s_settings_handler.get_k8s_cluster(k8s_cluster_name, strict_match=True)
            if cluster_settings is None:
                self.my_output.error('Cluster settings not found: %s' % (k8s_cluster_name))
                success = False
                self.k8s_nns[k8s_cluster_name] = None
                continue

            k8s_handler = k8s.K8s(
                kubeconfig_filename=cluster_settings['kubeconfig'],
                cluster_type=cluster_settings['type'],
                log_id=self.log_id
            )

            self.k8s_nns[k8s_cluster_name] = k8s_handler.get_node_network_states(
                return_mo=False,
                cluster_name=k8s_cluster_name,
                fixup=True
            )
            if self.k8s_nns[k8s_cluster_name] is None:
                success = False
                self.k8s_nns[k8s_cluster_name] = [dict(supported=False)]
            else:
                for item in self.k8s_nns[k8s_cluster_name]:
                    item['supported'] = True

        for k8s_cluster_name in self.k8s_clusters:
            self.set_cache(
                'k8s-%s-nns' % (k8s_cluster_name),
                self.k8s_nns[k8s_cluster_name]
            )

        return success

    def run_k8s_nns(self):
        for cluster_name in self.k8s_nns:
            if self.k8s_nns[cluster_name] is None:
                continue

            for nns_info in self.k8s_nns[cluster_name]:
                default_interface_name = None
                default_inteface_type = None
                if 'route' in nns_info and nns_info['route'] is not None:
                    for route in nns_info['route']:
                        if route['destination'] == '0.0.0.0/0':
                            default_interface_name = route['next-hop-interface']

                if 'interface' not in nns_info:
                    continue

                if nns_info['interface'] is None:
                    continue

                nns_info['node_hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        cluster_name,
                        nns_info['owner_name']
                    )
                )

                for interface_info in nns_info['interface']:
                    interface_info['default'] = False
                    if default_interface_name is not None:
                        if interface_info['name'] == default_interface_name:
                            default_inteface_type = interface_info['type']
                            interface_info['default'] = True

                for interface_info in nns_info['interface']:
                    if default_interface_name is not None and default_inteface_type is not None:
                        if default_inteface_type == 'bond':
                            if interface_info['type'] == 'ethernet':
                                if interface_info['lacp_parent'] is not None:
                                    if interface_info['lacp_parent'] == default_interface_name:
                                        interface_info['default'] = True

                        if default_inteface_type == 'vlan':
                            if interface_info['type'] == 'bond':
                                if interface_info['name'] == default_interface_name.split('.')[0]:
                                    interface_info['default'] = True

                            if interface_info['type'] == 'ethernet':
                                if interface_info['lacp_parent'] == default_interface_name.split('.')[0]:
                                    interface_info['default'] = True

                    interface_info['hash'] = ip_helper.get_string_md5(
                        '%s %s %s' % (
                            cluster_name,
                            nns_info['owner_name'],
                            interface_info['name']
                        )
                    )

                    interface_info['Server'] = self.get_server_mac_info_by_mac(
                        interface_info['mac']
                    )
                    if interface_info['Server'] is not None:
                        self.update_k8s_node_server_ref(
                            cluster_name,
                            nns_info['owner_name'],
                            interface_info['Server']['ServerName'],
                            interface_info['Server']['ServerMoid']
                        )

                        self.update_server_ocp(
                            interface_info['Server']['ServerMoid'],
                            cluster_name,
                            nns_info['owner_name'],
                            nns_info['node_hash']
                        )

                self.update_k8s_node_ethernet_counts(cluster_name, nns_info['owner_name'], nns_info)

        if not self.set_post_k8s_node():
            return False

        if not self.set_post_k8s_nns():
            return False

        if not self.set_post_server():
            return False

        return True
