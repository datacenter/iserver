class DomainVmmApi():
    def __init__(self):
        self.domain_vmm_mo = None

    def get_domain_vmm_mo(self):
        if self.domain_vmm_mo is not None:
            return self.domain_vmm_mo

        cache = self.get_object_cache(
            'vmmDomP'
        )
        if cache is not None:
            self.domain_vmm_mo = cache
            self.log.apic_mo(
                'vmmDomP',
                self.domain_vmm_mo
            )
            return self.domain_vmm_mo

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD'
        managed_objects = self.get_class(
            'vmmDomP',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_domain_vmm_mo',
                'API failed'
            )
            return None

        self.domain_vmm_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['vmmDomP']['attributes']
            attributes['vmmVSwitchPolicyCont'] = self.get_mo_child_attributes(
                'vmmDomP',
                managed_object,
                'vmmVSwitchPolicyCont'
            )
            attributes['vmmUsrAccP'] = self.get_mo_children_attributes(
                'vmmDomP',
                managed_object,
                'vmmUsrAccP'
            )
            attributes['vmmUplinkPCont'] = self.get_mo_child_attributes(
                'vmmDomP',
                managed_object,
                'vmmUplinkPCont'
            )
            attributes['infraRtDomP'] = self.get_mo_children_attributes(
                'vmmDomP',
                managed_object,
                'infraRtDomP'
            )
            attributes['vmmCtrlrP'] = self.get_mo_children_attributes(
                'vmmDomP',
                managed_object,
                'vmmCtrlrP'
            )
            attributes['infraRsVlanNs'] = self.get_mo_child_attributes(
                'vmmDomP',
                managed_object,
                'infraRsVlanNs'
            )
            attributes['aaaDomainRef'] = self.get_mo_children_attributes(
                'vmmDomP',
                managed_object,
                'aaaDomainRef'
            )
            attributes['vmmEpPD'] = self.get_mo_children_attributes(
                'vmmDomP',
                managed_object,
                'vmmEpPD'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'vmmDomP',
                managed_object,
                'faultCounts'
            )
            self.domain_vmm_mo.append(
                attributes
            )

        self.log.apic_mo(
            'vmmDomP',
            self.domain_vmm_mo
        )

        self.set_object_cache(
            'vmmDomP',
            self.domain_vmm_mo
        )

        return self.domain_vmm_mo
