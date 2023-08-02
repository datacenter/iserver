class ProtocolIpv4DomainApi():
    def __init__(self):
        self.ipv4_domains_mo = {}

    def get_protocol_ipv4_domains_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.ipv4_domains_mo:
            return self.ipv4_domains_mo[key]

        cache = self.get_object_cache(
            'uribv4Dom',
            object_selector=key
        )
        if cache is not None:
            self.ipv4_domains_mo[key] = cache
            self.log.apic_mo(
                'uribv4Dom.%s' % (key),
                self.ipv4_domains_mo[key]
            )
            return self.ipv4_domains_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/uribv4' % (pod_id, node_id)
        query = 'query-target=children&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Dom'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )
        if managed_objects is None:
            self.log.error(
                'get_protocol_ipv4_domains_mo',
                'API failed'
            )
            return None

        self.ipv4_domains_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['uribv4Dom']['attributes']
            attributes['healthInst'] = self.get_mo_child_attributes(
                'uribv4Dom',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'uribv4Dom',
                managed_object,
                'faultCounts'
            )
            self.ipv4_domains_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'uribv4Dom.%s' % (key),
            self.ipv4_domains_mo[key]
        )

        self.set_object_cache(
            'uribv4Dom',
            self.ipv4_domains_mo[key],
            object_selector=key
        )

        return self.ipv4_domains_mo[key]
