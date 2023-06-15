class DomainVmmEpgApi():
    def __init__(self):
        self.domain_vmm_epg_mo = None

    def get_domain_vmm_epg_mo(self):
        if self.domain_vmm_epg_mo is not None:
            return self.domain_vmm_epg_mo

        cache = self.get_object_cache(
            'vmmEpPD'
        )
        if cache is not None:
            self.domain_vmm_epg_mo = cache
            self.log.apic_mo(
                'vmmEpPD',
                self.domain_vmm_epg_mo
            )
            return self.domain_vmm_epg_mo

        managed_objects = self.get_class(
            'vmmEpPD',
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_domain_vmm_epg_mo',
                'API failed'
            )
            return None

        self.domain_vmm_epg_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['vmmEpPD']['attributes']
            self.domain_vmm_epg_mo.append(
                attributes
            )

        self.log.apic_mo(
            'vmmEpPD',
            self.domain_vmm_epg_mo
        )

        self.set_object_cache(
            'vmmEpPD',
            self.domain_vmm_epg_mo
        )

        return self.domain_vmm_epg_mo
