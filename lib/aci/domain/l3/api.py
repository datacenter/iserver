class DomainL3Api():
    def __init__(self):
        self.domain_l3_mo = None

    def get_domain_l3_mo(self):
        if self.domain_l3_mo is not None:
            return self.domain_l3_mo

        cache = self.get_object_cache(
            'l3extDomP'
        )
        if cache is not None:
            self.domain_l3_mo = cache
            self.log.apic_mo(
                'l3extDomP',
                self.domain_l3_mo
            )
            return self.domain_l3_mo

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef'
        managed_objects = self.get_class(
            'l3extDomP',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_domain_l3_mo',
                'API failed'
            )
            return None

        self.domain_l3_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l3extDomP']['attributes']
            attributes['infraRsVlanNs'] = self.get_mo_child_attributes(
                'l3extDomP',
                managed_object,
                'infraRsVlanNs'
            )
            attributes['infraRtDomP'] = self.get_mo_children_attributes(
                'l3extDomP',
                managed_object,
                'infraRtDomP'
            )
            attributes['extnwRtL3DomAtt'] = self.get_mo_children_attributes(
                'l3extDomP',
                managed_object,
                'extnwRtL3DomAtt'
            )
            attributes['aaaDomainRef'] = self.get_mo_children_attributes(
                'l3extDomP',
                managed_object,
                'aaaDomainRef'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'l3extDomP',
                managed_object,
                'faultCounts'
            )

            self.domain_l3_mo.append(
                attributes
            )

        self.log.apic_mo(
            'l3extDomP',
            self.domain_l3_mo
        )

        self.set_object_cache(
            'l3extDomP',
            self.domain_l3_mo
        )

        return self.domain_l3_mo
