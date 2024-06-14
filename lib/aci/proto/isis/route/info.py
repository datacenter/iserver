class ProtocolIsisRouteInfo():
    def __init__(self):
        self.isis_domain_routes = {}

    def get_protocol_isis_domain_route_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            if key == 'isisNexthop':
                info['isisNexthop'] = []
                for next_hop in managed_object['isisNexthop']:
                    # "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1/db-nh/nh-[eth1/107.7]-[<ip>]",
                    nh_info = {}
                    nh_info['interface'] = next_hop.split('nh-[')[1].split(']')[0]
                    nh_info['address'] = next_hop.split(']-[')[1].split(']')[0]
                    info['isisNexthop'].append(
                        nh_info
                    )
            else:
                info[key] = managed_object[key]

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )
        info['instance'] = info['dn'].split('/')[5].split('-')[1]
        info['domain'] = info['dn'].split('/')[6].split('-')[1]

        return info

    def get_protocol_isis_domain_routes_info(self, pod_id, node_id, instance_name, domain_name):
        key = '%s.%s.%s.%s' % (
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if key in self.isis_domain_routes:
            return self.isis_domain_routes[key]

        isis_domain_routes_mo = self.get_protocol_isis_domain_routes_mo(
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if isis_domain_routes_mo is not None:
            self.isis_domain_routes[key] = []
            for isis_domain_route_mo in isis_domain_routes_mo:
                self.isis_domain_routes[key].append(
                    self.get_protocol_isis_domain_route_info(
                        isis_domain_route_mo
                    )
                )

        return self.isis_domain_routes[key]

    def get_protocol_isis_domain_routes(self, pod_id, node_id, instance_name, domain_name):
        routes = self.get_protocol_isis_domain_routes_info(pod_id, node_id, instance_name, domain_name)
        if routes is None:
            return None

        routes = sorted(
            routes,
            key=lambda i: i['pfx'].lower()
        )

        return routes
