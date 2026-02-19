import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sNetworkOperatorInfo():
    def __init__(self):
        self.network_operator = None

    def get_network_operator_info(self, network_operator_mo):
        if network_operator_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            network_operator_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(network_operator_mo, 'spec')
        info['status'] = self.get(network_operator_mo, 'status')
        return info

    def get_network_operators_info(self, cache_enabled=True):
        if cache_enabled:
            if self.network_operator is not None:
                return self.network_operator

        managed_objects = self.get_network_operator_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.network_operator = []
        for managed_object in managed_objects:
            network_operator_info = {}
            network_operator_info['info'] = self.get_network_operator_info(
                managed_object
            )
            network_operator_info['mo'] = managed_object
            self.network_operator.append(
                network_operator_info
            )

        return self.network_operator

    def match_network_operator(self, network_operator_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, network_operator_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_network_operator',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_network_operators(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_network_operators = self.get_network_operators_info(cache_enabled=cache_enabled)
        if all_network_operators is None:
            return None

        network_operators = []

        for network_operator_info in all_network_operators:
            if not self.match_network_operator(network_operator_info['info'], object_filter):
                continue

            if return_mo:
                network_operators.append(
                    network_operator_info['mo']
                )
                continue

            network_operators.append(
                network_operator_info['info']
            )

        return network_operators

    def is_network_operator(self, name, cache_enabled=True):
        if self.get_network_operator(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_network_operator(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        network_operators = self.get_network_operators(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if network_operators is None:
            return None

        if len(network_operators) == 1:
            return network_operators[0]

        return None

    def get_cluster_network_operator(self, return_mo=False, cache_enabled=True):
        info = self.get_network_operator('cluster', return_mo=return_mo, cache_enabled=cache_enabled)
        if info is None:
            return None
        return info
    
    def get_cluster_network_operator_type(self, cache_enabled=True):
        info = self.get_cluster_network_operator(cache_enabled=cache_enabled)
        if info is None:
            return info
        return info['network_operator_type']
    
    def is_cluster_network_operator_ovn(self, cache_enabled=True):
        info = self.get_cluster_network_operator_type(cache_enabled=cache_enabled)
        if info is not None and info == 'OVNKubernetes':
            return True
        return False
    
    def get_cluster_network_operator_body(self, network_operator_type, cidr, host_prefix, kube_proxy_replacement=False):
        body = {}
        body['apiVersion'] = 'operator.openshift.io/v1'
        body['kind'] = 'Network'
        body['metadata'] = dict(name='cluster')
        body['spec'] = {}
        body['spec']['defaultNetowkr'] = dict(type=network_operator_type)
        network_mo = {}
        network_mo['cidr'] = cidr
        network_mo['hostPrefix'] = host_prefix
        body['spec']['clusterNetwork'] = [network_mo]
        body['spec']['deployKubeProxy'] = kube_proxy_replacement
        body['status'] = None
        return body

    def set_cluster_network_operator_type(self, network_operator_type, cidr, host_prefix, kube_proxy_replacement=False, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Set Cluster Network Operator Type', before_newline=True, underline=True)
            my_output.default('- type: %s' % (network_operator_type))
            my_output.default('- cidr: %s' % (cidr))
            my_output.default('- host prefix: %s' % (host_prefix))
            my_output.default('- kube proxy replaceement: %s' % (kube_proxy_replacement))
            
        body = self.get_cluster_network_operator_body(network_operator_type, cidr, host_prefix, kube_proxy_replacement=kube_proxy_replacement)
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False     

        success = self.patch_network_operator_mo(body)
        if not success:
            if my_output is not None:
                my_output.error('patch failed')
            return False
        
        if my_output is not None:
            my_output.default('Patch successful')

        return True
