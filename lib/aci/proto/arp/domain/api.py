class ProtocolArpDomainApi():
    def __init__(self):
        self.arp_domain_mo = {}

    def get_protocol_arp_domains_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.arp_domain_mo:
            return self.arp_domain_mo[key]

        cache = self.get_object_cache(
            'arpDom',
            object_selector=key
        )
        if cache is not None:
            self.arp_domain_mo[key] = cache
            self.log.apic_mo(
                'arpDom.%s' % (key),
                self.arp_domain_mo[key]
            )
            return self.arp_domain_mo[key]

        class_name = 'topology/pod-%s/node-%s/arpDom' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_arp_domains_mo',
                'API failed'
            )
            return None

        self.arp_domain_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.arp_domain_mo[key].append(
                managed_object['arpDom']['attributes']
            )

        self.log.apic_mo(
            'arpDom.%s' % (key),
            self.arp_domain_mo[key]
        )

        self.set_object_cache(
            'arpDom',
            self.arp_domain_mo[key],
            object_selector=key
        )

        return self.arp_domain_mo[key]
