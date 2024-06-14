class DomainAaaApi():
    def __init__(self):
        self.domain_aaa_mo = None

    def get_domain_aaa_mo(self):
        if self.domain_aaa_mo is not None:
            return self.domain_aaa_mo

        cache = self.get_object_cache(
            'aaaDomain'
        )
        if cache is not None:
            self.domain_aaa_mo = cache
            self.log.apic_mo(
                'aaaDomain',
                self.domain_aaa_mo
            )
            return self.domain_aaa_mo

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count'
        managed_objects = self.get_class(
            'aaaDomain',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            return None

        self.domain_aaa_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['aaaDomain']['attributes']
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'aaaDomain',
                managed_object,
                'faultCounts'
            )
            self.domain_aaa_mo.append(
                attributes
            )

        self.log.apic_mo(
            'aaaDomain',
            self.domain_aaa_mo
        )

        self.set_object_cache(
            'aaaDomain',
            self.domain_aaa_mo
        )

        return self.domain_aaa_mo
