class DomainVmmControllerApi():
    def __init__(self):
        self.domain_vmm_controller_mo = None

    def get_domain_vmm_controller_mo(self):
        if self.domain_vmm_controller_mo is not None:
            return self.domain_vmm_controller_mo

        cache = self.get_object_cache(
            'compCtrlr'
        )
        if cache is not None:
            self.domain_vmm_controller_mo = cache
            self.log.apic_mo(
                'compCtrlr',
                self.domain_vmm_controller_mo
            )
            return self.domain_vmm_controller_mo

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm'
        managed_objects = self.get_class(
            'compCtrlr',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_domain_vmm_controller_mo',
                'API failed'
            )
            return None

        self.domain_vmm_controller_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['compCtrlr']['attributes']
            attributes['compHv'] = self.get_mo_children_attributes(
                'compCtrlr',
                managed_object,
                'compHv'
            )
            attributes['compVm'] = self.get_mo_children_attributes(
                'compCtrlr',
                managed_object,
                'compVm'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'compCtrlr',
                managed_object,
                'faultCounts'
            )
            self.domain_vmm_controller_mo.append(
                attributes
            )

        self.log.apic_mo(
            'compCtrlr',
            self.domain_vmm_controller_mo
        )

        self.set_object_cache(
            'compCtrlr',
            self.domain_vmm_controller_mo
        )

        return self.domain_vmm_controller_mo
