class EpgAuditApi():
    def __init__(self):
        self.epg_audit_mo = None

    def get_epg_audit_mo(self):
        cache = self.get_object_cache(
            'fvAEPg.audit'
        )
        if cache is not None:
            self.epg_audit_mo = cache
            self.log.apic_mo(
                'fvAEPg.audit',
                self.epg_audit_mo
            )
            return self.epg_audit_mo

        query = 'rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=%s' % (self.api_audit_limit)
        managed_objects = self.get_class(
            'fvAEPg',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_epg_audit_mo',
                'API failed'
            )
            return None

        self.epg_audit_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['aaaModLR']['attributes']
            self.epg_audit_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fvAEPg.audit',
            self.epg_audit_mo
        )

        self.set_object_cache(
            'fvAEPg.audit',
            self.epg_audit_mo
        )

        return self.epg_audit_mo
