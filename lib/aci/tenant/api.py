class TenantApi():
    def __init__(self):
        self.tenant_mo = None

    def get_tenant_mo(self):
        if self.tenant_mo is not None:
            return self.tenant_mo

        cache = self.get_object_cache(
            'fvTenant'
        )
        if cache is not None:
            self.tenant_mo = cache
            self.log.apic_mo(
                'fvTenant',
                self.tenant_mo
            )
            return self.tenant_mo

        query = 'rsp-subtree=children&rsp-subtree-include=health,fault-count'
        managed_objects = self.get_class(
            'fvTenant',
            query=query
        )
        if managed_objects is None:
            return None

        self.tenant_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvTenant']['attributes']
            attributes['healthInst'] = self.get_mo_child_attributes(
                'fvTenant',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'fvTenant',
                managed_object,
                'faultCounts'
            )
            self.tenant_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fvTenant',
            self.tenant_mo
        )

        self.set_object_cache(
            'fvTenant',
            self.tenant_mo
        )

        return self.tenant_mo
