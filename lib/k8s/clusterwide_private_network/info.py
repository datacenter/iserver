from lib import filter_helper
from lib import ip_helper


class K8sClusterwidePrivateNetworkInfo():
    def __init__(self):
        self.clusterwide_private_network = None

    def get_clusterwide_private_network_info(self, clusterwide_private_network_mo):
        if clusterwide_private_network_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            clusterwide_private_network_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(clusterwide_private_network_mo, 'spec')
        info['status'] = self.get(clusterwide_private_network_mo, 'status')
        info['cidrv4'] = []
        info['cidrv6'] = []

        subnets_mo = self.get(clusterwide_private_network_mo, 'spec:subnets', on_error=[], on_none=[])
        for subnet_mo in subnets_mo:
            if ip_helper.is_valid_ipv4_cidr(subnet_mo['cidr']):
                info['cidrv4'].append(subnet_mo['cidr'])
            if ip_helper.is_valid_ipv6_cidr(subnet_mo['cidr']):
                info['cidrv6'].append(subnet_mo['cidr'])

        info['inb'] = []
        bridges_mo = self.get(clusterwide_private_network_mo, 'spec:networkBridges', on_error=[], on_none=[])
        for bridge_mo in bridges_mo:
            info['inb'].append(
                bridge_mo['cluster']
            )

        info['destT'] = []
        info['gatewayT'] = []
        routes_mo = self.get(clusterwide_private_network_mo, 'spec:routes', on_error=[], on_none=[])
        for route_mo in routes_mo:
            info['destT'].append(
                route_mo['destination']
            )
            info['gatewayT'].append(
                route_mo['gateway']
            )

        return info

    def get_clusterwide_private_networks_info(self, cache_enabled=True):
        if cache_enabled:
            if self.clusterwide_private_network is not None:
                return self.clusterwide_private_network

        managed_objects = self.get_clusterwide_private_network_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.clusterwide_private_network = []
        for managed_object in managed_objects:
            clusterwide_private_network_info = {}
            clusterwide_private_network_info['info'] = self.get_clusterwide_private_network_info(
                managed_object
            )
            clusterwide_private_network_info['mo'] = managed_object
            self.clusterwide_private_network.append(
                clusterwide_private_network_info
            )

        return self.clusterwide_private_network

    def match_clusterwide_private_network(self, clusterwide_private_network_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, clusterwide_private_network_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_clusterwide_private_network',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_clusterwide_private_networks(self, object_filter=None, pod_info=False, return_mo=False, cache_enabled=True):
        all_clusterwide_private_networks = self.get_clusterwide_private_networks_info(cache_enabled=cache_enabled)
        if all_clusterwide_private_networks is None:
            return None

        clusterwide_private_networks = []

        if pod_info:
            pods = self.get_pods_cilium_private_networks(cache_enabled=cache_enabled)

        for clusterwide_private_network_info in all_clusterwide_private_networks:
            if not self.match_clusterwide_private_network(clusterwide_private_network_info['info'], object_filter):
                continue

            if return_mo:
                clusterwide_private_networks.append(
                    clusterwide_private_network_info['mo']
                )
                continue

            if pod_info:
                clusterwide_private_network_info['info']['podT'] = []
                clusterwide_private_network_info['info']['pod'] = []

                for pod in pods:
                    if pod['private_network']['name'] == clusterwide_private_network_info['info']['name']:
                        clusterwide_private_network_info['info']['pod'].append(pod)
                        clusterwide_private_network_info['info']['podT'].append(pod['namespace_name'])

            clusterwide_private_networks.append(
                clusterwide_private_network_info['info']
            )

        return clusterwide_private_networks

    def is_clusterwide_private_network(self, name, cache_enabled=True):
        if self.get_clusterwide_private_network(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_clusterwide_private_network(self, name, pod_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        clusterwide_private_networks = self.get_clusterwide_private_networks(
            object_filter=object_filter,
            pod_info=pod_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if clusterwide_private_networks is None:
            return None

        if len(clusterwide_private_networks) == 1:
            return clusterwide_private_networks[0]

        return None
