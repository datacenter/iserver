class ProtocolIpv4RouteApi():
    def __init__(self):
        self.ipv4_routes_mo = {}

    def get_protocol_ipv4_routes_mo(self, pod_id, node_id, ipv4_domain_name):
        key = '%s.%s.%s' % (pod_id, node_id, ipv4_domain_name)
        if key in self.ipv4_routes_mo:
            return self.ipv4_routes_mo[key]

        cache = self.get_object_cache(
            'uribv4Route',
            object_selector=key
        )
        if cache is not None:
            self.ipv4_routes_mo[key] = cache
            self.log.apic_mo(
                'uribv4Route.%s' % (key),
                self.ipv4_routes_mo[key]
            )
            return self.ipv4_routes_mo[key]

        # url: https://apic11o-eu-spdc.cisco.com/api/node/mo/topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1-N6_VRF.json?query-target=subtree&target-subtree-class=uribv4Route&page=0&page-size=15
        distinguished_name = 'topology/pod-%s/node-%s/sys/uribv4/dom-%s' % (
            pod_id,
            node_id,
            ipv4_domain_name
        )
        query = 'query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_ipv4_routes_mo',
                'API failed'
            )
            return None

        self.ipv4_routes_mo[key] = []
        for managed_object in managed_objects['imdata']:
            if 'uribv4Route' in managed_object:
                self.ipv4_routes_mo[key].append(
                    managed_object['uribv4Route']['attributes']
                )

        for managed_object in managed_objects['imdata']:
            if 'uribv4Nexthop' in managed_object:
                next_hop_rt = managed_object['uribv4Nexthop']['attributes']['dn'].split('/')[7]
                for entry in self.ipv4_routes_mo[key]:
                    if next_hop_rt in entry['dn']:
                        if 'next_hop' not in entry:
                            entry['next_hop'] = []

                        entry['next_hop'].append(
                            managed_object['uribv4Nexthop']['attributes']
                        )

        self.log.apic_mo(
            'uribv4Route.%s' % (key),
            self.ipv4_routes_mo[key]
        )

        self.set_object_cache(
            'uribv4Route',
            self.ipv4_routes_mo[key],
            object_selector=key
        )

        return self.ipv4_routes_mo[key]
