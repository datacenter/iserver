import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sNetworkInfo():
    def __init__(self):
        self.network = None

    def get_network_info(self, network_mo):
        if network_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            network_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(network_mo, 'spec')
        info['status'] = self.get(network_mo, 'status')
        info['network_type'] = self.get(network_mo, 'status:networkType')
        info['service_network'] = ','.join(self.get(network_mo, 'status:serviceNetwork', on_error=[], on_none=[]))

        cidr = []
        prefix = None
        cluster_networks = self.get(network_mo, 'status:clusterNetwork', on_error=[], on_none=[])
        for cluster_network in cluster_networks:
            cidr.append(
                cluster_network['cidr']
            )
            prefix = cluster_network['hostPrefix']
        
        info['cluster_network'] = ','.join(cidr)
        info['host_prefix'] = prefix
        return info

    def get_networks_info(self, cache_enabled=True):
        if cache_enabled:
            if self.network is not None:
                return self.network

        managed_objects = self.get_network_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.network = []
        for managed_object in managed_objects:
            network_info = {}
            network_info['info'] = self.get_network_info(
                managed_object
            )
            network_info['mo'] = managed_object
            self.network.append(
                network_info
            )

        return self.network

    def match_network(self, network_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, network_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_network',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_networks(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_networks = self.get_networks_info(cache_enabled=cache_enabled)
        if all_networks is None:
            return None

        networks = []

        for network_info in all_networks:
            if not self.match_network(network_info['info'], object_filter):
                continue

            if return_mo:
                networks.append(
                    network_info['mo']
                )
                continue

            networks.append(
                network_info['info']
            )

        return networks

    def is_network(self, name, cache_enabled=True):
        if self.get_network(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_network(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        networks = self.get_networks(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if networks is None:
            return None

        if len(networks) == 1:
            return networks[0]

        return None

    def get_cluster_network(self, return_mo=False, cache_enabled=True):
        info = self.get_network('cluster')
        if info is None:
            return None
        return info
    
    def get_cluster_network_type(self, cache_enabled=True):
        info = self.get_cluster_network(cache_enabled=cache_enabled)
        if info is None:
            return info
        return info['network_type']
    
    def is_cluster_network_ovn(self, cache_enabled=True):
        info = self.get_cluster_network_type(cache_enabled=cache_enabled)
        if info is not None and info == 'OVNKubernetes':
            return True
        return False
    
    def get_cluster_network_body(self, network_type, cidr, host_prefix):
        body = {}
        body['apiVersion'] = 'config.openshift.io/v1'
        body['kind'] = 'Network'
        body['metadata'] = dict(name='cluster')
        body['spec'] = {}
        body['spec']['networkType'] = network_type
        network_mo = {}
        network_mo['cidr'] = cidr
        network_mo['hostPrefix'] = host_prefix
        body['spec']['clusterNetwork'] = [network_mo]
        body['status'] = None
        return body

    def set_cluster_network_type(self, network_type, cidr, host_prefix, confirmation=False, my_output=None):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Set Cluster Network Type', before_newline=True, underline=True)
            my_output.default('- type: %s' % (network_type))
            my_output.default('- cidr: %s' % (cidr))
            my_output.default('- host prefix: %s' % (host_prefix))
            
        body = self.get_cluster_network_body(network_type, cidr, host_prefix)
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False     

        success = self.patch_network_mo(body)
        if not success:
            if my_output is not None:
                my_output.error('patch failed')
            return False
        
        if my_output is not None:
            my_output.default('Patch successful')

        return True
