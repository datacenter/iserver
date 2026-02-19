from lib import filter_helper
from lib import ip_helper


class K8sClusterwidePrivateNetworkDb():
    def __init__(self):
        pass

    def get_clusterwide_private_network_db_info(self, managed_object, endpoints_info):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        info['name'] = filter_helper.get(managed_object, 'Name')
        info['cidrv4'] = []
        info['cidrv6'] = []

        subnets_mo = self.get(managed_object, 'Subnets', on_error=[], on_none=[])
        for subnet_mo in subnets_mo:
            if ip_helper.is_valid_ipv4_cidr(subnet_mo['CIDR']):
                info['cidrv4'].append(subnet_mo['CIDR'])
            if ip_helper.is_valid_ipv6_cidr(subnet_mo['CIDR']):
                info['cidrv6'].append(subnet_mo['CIDR'])

        info['inb'] = []
        selector_mo = self.get(managed_object, 'INBs:Selectors')
        if selector_mo is not None:
            for key in selector_mo:
                 info['inb'].append(key)

        info['podT'] = []
        if endpoints_info is not None:
            for endpoint_info in endpoints_info:
                if endpoint_info['network'] == info['name']:
                    info['podT'].append(
                        '%s/%s/%s/%s' % (
                            endpoint_info['cluster'],
                            endpoint_info['node_name'],
                            endpoint_info['namespace'],
                            endpoint_info['name']
                        )
                    )

        info['destT'] = []
        info['gatewayT'] = []
        routes_mo = self.get(managed_object, 'Routes', on_error=[], on_none=[])
        for route_mo in routes_mo:
            info['destT'].append(
                route_mo['Destination']
            )
            info['gatewayT'].append(
                route_mo['Gateway']
            )

        return info

    def get_clusterwide_private_networks_db_info(self, db_entries, endpoints_info):
        info = []

        if db_entries is not None:
            for db_entry in db_entries:
                info.append(
                    self.get_clusterwide_private_network_db_info(
                        db_entry,
                        endpoints_info
                    )
                )

        return info

    def get_clusterwide_private_network_endpoint_db_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        info['pod_ip'] = filter_helper.get(managed_object, 'ip')
        info['name'] = filter_helper.get(managed_object, 'name')
        info['network'] = filter_helper.get(managed_object, 'network:name')
        info['private_ip'] = filter_helper.get(managed_object, 'network:ip')
        info['private_mac'] = filter_helper.get(managed_object, 'network:mac')
        info['cluster'] = filter_helper.get(managed_object, 'source:cluster')
        info['node_name'] = filter_helper.get(managed_object, 'source:name')
        info['namespace'] = filter_helper.get(managed_object, 'source:namespace')
        info['since'] = filter_helper.get(managed_object, 'activatedAt')
        return info

    def get_clusterwide_private_network_endpoints_db_info(self, db_entries):
        info = []

        if db_entries is not None:
            for db_entry in db_entries:
                info.append(
                    self.get_clusterwide_private_network_endpoint_db_info(
                        db_entry
                    )
                )

        return info
