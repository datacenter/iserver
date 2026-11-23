class L3OutAuditApi():
    def __init__(self):
        self.l3out_audit_mo = None

    def get_l3out_audit_mo(self):
        cache = self.get_object_cache(
            'l3extOut.audit'
        )
        if cache is not None:
            self.l3out_audit_mo = cache
            self.log.apic_mo(
                'l3extOut.audit',
                self.l3out_audit_mo
            )
            return self.l3out_audit_mo

        query = 'rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=%s' % (self.api_audit_limit)
        managed_objects = self.get_class(
            'l3extOut',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_l3out_audit_mo',
                'API failed'
            )
            return None

        self.l3out_audit_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['aaaModLR']['attributes']
            self.l3out_audit_mo.append(
                attributes
            )

        self.log.apic_mo(
            'l3extOut.audit',
            self.l3out_audit_mo
        )

        self.set_object_cache(
            'l3extOut.audit',
            self.l3out_audit_mo
        )

        return self.l3out_audit_mo
