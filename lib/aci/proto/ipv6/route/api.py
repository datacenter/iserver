class ProtocolIpv6RouteApi():
    def __init__(self):
        self.ipv6_routes_mo = {}

    def get_protocol_ipv6_routes_mo(self, pod_id, node_id, ipv6_domain_name):
        key = '%s.%s.%s' % (pod_id, node_id, '.'.join(ipv6_domain_name.split(':')))
        if key in self.ipv6_routes_mo:
            return self.ipv6_routes_mo[key]

        cache = self.get_object_cache(
            'uribv6Route',
            object_selector=key
        )
        if cache is not None:
            self.ipv6_routes_mo[key] = cache
            self.log.apic_mo(
                'uribv6Route.%s' % (key),
                self.ipv6_routes_mo[key]
            )
            return self.ipv6_routes_mo[key]

        # url: https://<apic>/api/node/mo/topology/pod-1/node-201/sys/uribv6/dom-common:smi5Gc-cvim1-N6_VRF.json?query-target=subtree&target-subtree-class=uribv6Route&page=0&page-size=15
        distinguished_name = 'topology/pod-%s/node-%s/sys/uribv6/dom-%s' % (
            pod_id,
            node_id,
            ipv6_domain_name
        )
        query = 'query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        self.log.apic_mo(
            'uribv6Route.raw.%s' % (key),
            managed_objects
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_ipv6_routes_mo',
                'API failed'
            )
            return None

        self.ipv6_routes_mo[key] = []
        for managed_object in managed_objects['imdata']:
            if 'uribv6Route' in managed_object:
                attributes = managed_object['uribv6Route']['attributes']
                attributes['healthInst'] = self.get_mo_child_attributes(
                    'uribv6Route',
                    managed_object,
                    'healthInst'
                )
                attributes['faultCounts'] = self.get_mo_child_attributes(
                    'uribv6Route',
                    managed_object,
                    'faultCounts'
                )
                self.ipv6_routes_mo[key].append(
                    attributes
                )

        for managed_object in managed_objects['imdata']:
            if 'uribv6Nexthop' in managed_object:
                next_hop_rt = managed_object['uribv6Nexthop']['attributes']['dn'].split('/')[7]
                for entry in self.ipv6_routes_mo[key]:
                    if next_hop_rt in entry['dn']:
                        if 'next_hop' not in entry:
                            entry['next_hop'] = []

                        entry['next_hop'].append(
                            managed_object['uribv6Nexthop']['attributes']
                        )

        self.log.apic_mo(
            'uribv6Route.%s' % (key),
            self.ipv6_routes_mo[key]
        )

        self.set_object_cache(
            'uribv6Route',
            self.ipv6_routes_mo[key],
            object_selector=key
        )

        return self.ipv6_routes_mo[key]
