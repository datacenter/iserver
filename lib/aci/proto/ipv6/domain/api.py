class ProtocolIpv6DomainApi():
    def __init__(self):
        self.ipv6_domains_mo = {}

    def get_protocol_ipv6_domains_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.ipv6_domains_mo:
            return self.ipv6_domains_mo[key]

        cache = self.get_object_cache(
            'uribv6Dom',
            object_selector=key
        )
        if cache is not None:
            self.ipv6_domains_mo[key] = cache
            self.log.apic_mo(
                'uribv6Dom.%s' % (key),
                self.ipv6_domains_mo[key]
            )
            return self.ipv6_domains_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/uribv6' % (pod_id, node_id)
        query = 'query-target=children&rsp-subtree-include=fault-count&target-subtree-class=uribv6Dom'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )
        if managed_objects is None:
            self.log.error(
                'get_protocol_ipv6_domains_mo',
                'API failed'
            )
            return None

        self.ipv6_domains_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['uribv6Dom']['attributes']
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'uribv6Dom',
                managed_object,
                'faultCounts'
            )
            self.ipv6_domains_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'uribv6Dom.%s' % (key),
            self.ipv6_domains_mo[key]
        )

        self.set_object_cache(
            'uribv6Dom',
            self.ipv6_domains_mo[key],
            object_selector=key
        )

        return self.ipv6_domains_mo[key]
