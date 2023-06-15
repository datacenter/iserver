class ProtocolArpAdjacencyApi():
    def __init__(self):
        self.arp_adjacencies_mo = {}

    def get_protocol_arp_adjacencies_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.arp_adjacencies_mo:
            return self.arp_adjacencies_mo[key]

        cache = self.get_object_cache(
            'arpAdjEp',
            object_selector=key
        )
        if cache is not None:
            self.arp_adjacencies_mo[key] = cache
            self.log.apic_mo(
                'arpAdjEp.%s' % (key),
                self.arp_adjacencies_mo[key]
            )
            return self.arp_adjacencies_mo[key]

        class_name = 'topology/pod-%s/node-%s/arpDom' % (pod_id, node_id)
        query = 'query-target=subtree&target-subtree-class=arpAdjEp'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_arp_adjacencies_mo',
                'API failed'
            )
            return None

        self.arp_adjacencies_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.arp_adjacencies_mo[key].append(
                managed_object['arpAdjEp']['attributes']
            )

        self.log.apic_mo(
            'arpAdjEp.%s' % (key),
            self.arp_adjacencies_mo[key]
        )

        self.set_object_cache(
            'arpAdjEp',
            self.arp_adjacencies_mo[key],
            object_selector=key
        )

        return self.arp_adjacencies_mo[key]
