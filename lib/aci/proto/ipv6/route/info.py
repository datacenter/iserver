from lib import ip_helper


class ProtocolIpv6RouteInfo():
    def __init__(self):
        self.ipv6_routes = {}

    def get_protocol_ipv6_route_next_hop_types(self, route):
        next_hop_types = []

        if 'next_hop' in route:
            for next_hop in route['next_hop']:
                if next_hop['routeType'] not in next_hop_types:
                    next_hop_types.append(
                        next_hop['routeType']
                    )

        if 'ebgp' in next_hop_types or 'ibgp' in next_hop_types:
            next_hop_types.append('bgp')

        return next_hop_types

    def get_protocol_ipv6_routes_summary(self, routes):
        summary = {}
        summary['count'] = 0
        summary['default'] = False
        summary['ebgp'] = 0
        summary['ibgp'] = 0
        summary['bgp'] = 0
        summary['local'] = 0
        summary['direct'] = 0

        for route in routes:
            summary['count'] = summary['count'] + 1
            if route['prefix'] == '0.0.0.0/0':
                summary['default'] = True

            next_hop_types = self.get_protocol_ipv6_route_next_hop_types(route)
            for next_hop_type in next_hop_types:
                if next_hop_type in summary:
                    summary[next_hop_type] = summary[next_hop_type] + 1

        return summary

    def check_protocol_ipv6_route_filter_match(self, ipv6_route_info, route_filter):
        if route_filter is None or len(route_filter) == 0:
            return True

        for rule in route_filter:
            if rule in ['ibgp', 'ebgp', 'static', 'local', 'direct']:
                match = False
                if 'next_hop' in ipv6_route_info:
                    for next_hop in ipv6_route_info['next_hop']:
                        if next_hop['routeType'] == rule:
                            match = True

                if not match:
                    return False

            if rule == 'bgp':
                match = False
                for match_rule in ['ibgp', 'ebgp']:
                    if 'next_hop' in ipv6_route_info:
                        for next_hop in ipv6_route_info['next_hop']:
                            if next_hop['routeType'] == match_rule:
                                match = True

                if not match:
                    return False

            if rule.startswith('nh:'):
                match = False
                if 'next_hop' in ipv6_route_info:
                    for next_hop in ipv6_route_info['next_hop']:
                        if next_hop['addr'].split('/')[0] == rule.split(':')[1]:
                            match = True

                if not match:
                    return False

            if rule.startswith('ip:'):
                ip_address_search = rule.split(':')[1]
                if ipv6_route_info['prefix'] != '0.0.0.0/0':
                    if not ip_helper.is_ipv6_in_cidr(ip_address_search, ipv6_route_info['prefix']):
                        return False

            if rule.startswith('subnet:'):
                ip_subnet_search = rule.split(':')[1]
                if ip_subnet_search != ipv6_route_info['prefix']:
                    return False

            if rule.startswith('subnet-longer:'):
                ip_subnet_search = rule.split(':')[1]
                if not ip_helper.is_subnet_in_subnet(ipv6_route_info['prefix'], ip_subnet_search):
                    return False

        return True

    def get_protocol_ipv6_route_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        info['vrf'] = info['dn'].split('/')[5][4:]
        if 'next_hop' in managed_object:
            for nh_info in managed_object['next_hop']:
                if nh_info['if'] == 'unspecified':
                    nh_info['if'] = ''

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_protocol_ipv6_routes_info(self, pod_id, node_id, ipv6_domain_name):
        key = '%s.%s.%s' % (pod_id, node_id, '.'.join(ipv6_domain_name.split(':')))
        if key in self.ipv6_routes:
            return self.ipv6_routes[key]

        ipv6_routes_mo = self.get_protocol_ipv6_routes_mo(pod_id, node_id, ipv6_domain_name)
        if ipv6_routes_mo is not None:
            self.ipv6_routes[key] = []
            for hsrp_interface_mo in ipv6_routes_mo:
                self.ipv6_routes[key].append(
                    self.get_protocol_ipv6_route_info(
                        hsrp_interface_mo
                    )
                )

        self.log.apic_mo(
            'uribv6Route.info.%s' % (key),
            self.ipv6_routes[key]
        )

        return self.ipv6_routes[key]

    def get_protocol_ipv6_routes(self, pod_id, node_id, ipv6_domain_name, route_filter=None):
        all_routes = self.get_protocol_ipv6_routes_info(
            pod_id,
            node_id,
            ipv6_domain_name
        )

        info = []
        default_routes = []

        for ipv6_route_info in all_routes:
            if ipv6_route_info['prefix'] == '0.0.0.0/0':
                default_routes.append(
                    ipv6_route_info
                )

            if route_filter is not None:
                if not self.check_protocol_ipv6_route_filter_match(ipv6_route_info, route_filter):
                    continue

            info.append(
                ipv6_route_info
            )

        info = sorted(
            info,
            key=lambda i: i['prefix']
        )

        return info
