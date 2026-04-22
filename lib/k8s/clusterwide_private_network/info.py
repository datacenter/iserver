from lib import ip_helper


class K8sClusterwidePrivateNetworkInfo():
    def __init__(self):
        self.clusterwide_private_network = None

    def get_clusterwide_private_network_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)

        info['cidrv4'] = []
        info['cidrv6'] = []

        subnets_mo = self.get(managed_object, 'spec:subnets', on_error=[], on_none=[])
        for subnet_mo in subnets_mo:
            cidr_mo = self.get(subnet_mo, 'cidr')
            if cidr_mo is not None:
                if ip_helper.is_valid_ipv4_cidr(subnet_mo['cidr']):
                    info['cidrv4'].append(subnet_mo['cidr'])
                if ip_helper.is_valid_ipv6_cidr(subnet_mo['cidr']):
                    info['cidrv6'].append(subnet_mo['cidr'])

        info['inb'] = []
        bridges_mo = self.get(managed_object, 'spec:networkBridges', on_error=[], on_none=[])
        for bridge_mo in bridges_mo:
            info['inb'].append(
                bridge_mo['cluster']
            )

        info['destT'] = []
        info['gatewayT'] = []
        routes_mo = self.get(managed_object, 'spec:routes', on_error=[], on_none=[])
        for route_mo in routes_mo:
            info['destT'].append(
                route_mo['destination']
            )
            info['gatewayT'].append(
                route_mo['gateway']
            )

        return info

    def add_clusterwide_private_networks_info(self, infos, pod_info=False, cache_enabled=True):
        if pod_info:
            pods = self.get_pods_cilium_private_networks(cache_enabled=cache_enabled)

            for info in infos:
                info['podT'] = []
                info['pod'] = []

                for pod in pods:
                    if pod['private_network']['name'] == info['name']:
                        info['pod'].append(pod)
                        info['podT'].append(pod['namespace_name'])

        return infos
    
    def get_clusterwide_private_networks(self, object_filter=None, pod_info=False, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'clusterwide_private_network', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        if return_mo:
            return infos

        if infos is not None:
            infos = self.add_clusterwide_private_networks_info(
                infos,
                pod_info=pod_info,
                cache_enabled=cache_enabled
            )

        return infos   
            
    def is_clusterwide_private_network(self, name, cache_enabled=True, optimized=True):
        if self.get_clusterwide_private_network(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_clusterwide_private_network(self, name, pod_info=False, return_mo=False, cache_enabled=True, optimized=True):
        info = self.get_info(
            'clusterwide_private_network', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
        if return_mo:
            return info
        
        infos = [info]
        infos = self.add_clusterwide_private_networks_info(
            infos,
            pod_info=pod_info,
            cache_enabled=cache_enabled
        )

        return infos[0]