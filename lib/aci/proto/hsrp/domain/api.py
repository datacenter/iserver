class ProtocolHsrpDomainApi():
    def __init__(self):
        self.hsrp_domains_mo = {}

    def get_protocol_hsrp_domains_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.hsrp_domains_mo:
            return self.hsrp_domains_mo[key]

        cache = self.get_object_cache(
            'hsrpDom',
            object_selector=key
        )
        if cache is not None:
            self.hsrp_domains_mo[key] = cache
            self.log.apic_mo(
                'hsrpDom.%s' % (key),
                self.hsrp_domains_mo[key]
            )
            return self.hsrp_domains_mo[key]

        class_name = 'topology/pod-%s/node-%s/hsrpDom' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-include=health,fault-count'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_hsrp_domains_mo',
                'API failed'
            )
            return None

        self.hsrp_domains_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['hsrpDom']['attributes']
            attributes['healthInst'] = self.get_mo_child_attributes(
                'hsrpDom',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'hsrpDom',
                managed_object,
                'faultCounts'
            )
            self.hsrp_domains_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'hsrpDom.%s' % (key),
            self.hsrp_domains_mo[key]
        )

        self.set_object_cache(
            'hsrpDom',
            self.hsrp_domains_mo[key],
            object_selector=key
        )

        return self.hsrp_domains_mo[key]
