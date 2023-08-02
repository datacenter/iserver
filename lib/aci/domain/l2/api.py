class DomainL2Api():
    def __init__(self):
        self.domain_l2_mo = None

    def get_domain_l2_mo(self):
        if self.domain_l2_mo is not None:
            return self.domain_l2_mo

        cache = self.get_object_cache(
            'l2extDomP'
        )
        if cache is not None:
            self.domain_l2_mo = cache
            self.log.apic_mo(
                'l2extDomP',
                self.domain_l2_mo
            )
            return self.domain_l2_mo

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef'
        managed_objects = self.get_class(
            'l2extDomP',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_domain_l2_mo',
                'API failed'
            )
            return None

        self.domain_l2_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l2extDomP']['attributes']
            attributes['infraRsVlanNs'] = self.get_mo_child_attributes(
                'l2extDomP',
                managed_object,
                'infraRsVlanNs'
            )
            attributes['infraRtDomP'] = self.get_mo_children_attributes(
                'l2extDomP',
                managed_object,
                'infraRtDomP'
            )
            attributes['l2extRtL2DomAtt'] = self.get_mo_children_attributes(
                'l2extDomP',
                managed_object,
                'l2extRtL2DomAtt'
            )
            attributes['aaaDomainRef'] = self.get_mo_children_attributes(
                'l2extDomP',
                managed_object,
                'aaaDomainRef'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'l2extDomP',
                managed_object,
                'faultCounts'
            )

            self.domain_l2_mo.append(
                attributes
            )

        self.log.apic_mo(
            'l2extDomP',
            self.domain_l2_mo
        )

        self.set_object_cache(
            'l2extDomP',
            self.domain_l2_mo
        )

        return self.domain_l2_mo
