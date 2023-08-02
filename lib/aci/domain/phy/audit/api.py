class DomainPhyAuditApi():
    def __init__(self):
        self.domain_phy_audit_mo = None

    def get_domain_phy_audit_mo(self):
        cache = self.get_object_cache(
            'physDomP.audit'
        )
        if cache is not None:
            self.domain_phy_audit_mo = cache
            self.log.apic_mo(
                'physDomP.audit',
                self.domain_phy_audit_mo
            )
            return self.domain_phy_audit_mo

        query = 'rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=%s' % (self.api_audit_limit)
        managed_objects = self.get_class(
            'physDomP',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_domain_phy_audit_mo',
                'API failed'
            )
            return None

        self.domain_phy_audit_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['aaaModLR']['attributes']
            self.domain_phy_audit_mo.append(
                attributes
            )

        self.log.apic_mo(
            'physDomP.audit',
            self.domain_phy_audit_mo
        )

        self.set_object_cache(
            'physDomP.audit',
            self.domain_phy_audit_mo
        )

        return self.domain_phy_audit_mo
