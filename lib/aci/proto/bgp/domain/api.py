class ProtocolBgpDomainApi():
    def __init__(self):
        self.bgp_domains_mo = {}

    def get_protocol_bgp_domains_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bgp_domains_mo:
            return self.bgp_domains_mo[key]

        cache = self.get_object_cache(
            'bgpDom',
            object_selector=key
        )
        if cache is not None:
            self.bgp_domains_mo[key] = cache
            self.log.apic_mo(
                'bgpDom.%s' % (key),
                self.bgp_domains_mo[key]
            )
            return self.bgp_domains_mo[key]

        class_name = 'topology/pod-%s/node-%s/bgpDom' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-include=health,fault-count'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_bgp_domains_mo',
                'API failed'
            )
            return None

        self.bgp_domains_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['bgpDom']['attributes']
            attributes['healthInst'] = self.get_mo_child_attributes(
                'bgpDom',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'bgpDom',
                managed_object,
                'faultCounts'
            )
            self.bgp_domains_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'bgpDom.%s' % (key),
            self.bgp_domains_mo[key]
        )

        self.set_object_cache(
            'bgpDom',
            self.bgp_domains_mo[key],
            object_selector=key
        )

        return self.bgp_domains_mo[key]
