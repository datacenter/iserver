class DomainPhyApi():
    def __init__(self):
        self.domain_phy_mo = None

    def get_domain_phy_mo(self):
        if self.domain_phy_mo is not None:
            return self.domain_phy_mo

        cache = self.get_object_cache(
            'physDomP'
        )
        if cache is not None:
            self.domain_phy_mo = cache
            self.log.apic_mo(
                'physDomP',
                self.domain_phy_mo
            )
            return self.domain_phy_mo

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef'
        managed_objects = self.get_class(
            'physDomP',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_domain_phy_mo',
                'API failed'
            )
            return None

        self.domain_phy_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['physDomP']['attributes']
            attributes['infraRsVlanNs'] = self.get_mo_child_attributes(
                'physDomP',
                managed_object,
                'infraRsVlanNs'
            )
            attributes['infraRtDomP'] = self.get_mo_children_attributes(
                'physDomP',
                managed_object,
                'infraRtDomP'
            )
            attributes['infraRtDomAtt'] = self.get_mo_children_attributes(
                'physDomP',
                managed_object,
                'infraRtDomAtt'
            )
            attributes['aaaDomainRef'] = self.get_mo_children_attributes(
                'physDomP',
                managed_object,
                'aaaDomainRef'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'physDomP',
                managed_object,
                'faultCounts'
            )

            self.domain_phy_mo.append(
                attributes
            )

        self.log.apic_mo(
            'physDomP',
            self.domain_phy_mo
        )

        self.set_object_cache(
            'physDomP',
            self.domain_phy_mo
        )

        return self.domain_phy_mo
