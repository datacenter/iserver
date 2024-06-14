class PolicyGeneralAaeAuditApi():
    def __init__(self):
        self.policy_global_aae_audit_mo = None

    def get_policy_global_aae_audit_mo(self):
        cache = self.get_object_cache(
            'infraAttEntityP.audit'
        )
        if cache is not None:
            self.policy_global_aae_audit_mo = cache
            self.log.apic_mo(
                'infraAttEntityP.audit',
                self.policy_global_aae_audit_mo
            )
            return self.policy_global_aae_audit_mo

        query = 'rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=%s' % (self.api_audit_limit)
        managed_objects = self.get_class(
            'infraAttEntityP',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_policy_global_aae_audit_mo',
                'API failed'
            )
            return None

        self.policy_global_aae_audit_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['aaaModLR']['attributes']
            self.policy_global_aae_audit_mo.append(
                attributes
            )

        self.log.apic_mo(
            'infraAttEntityP.audit',
            self.policy_global_aae_audit_mo
        )

        self.set_object_cache(
            'infraAttEntityP.audit',
            self.policy_global_aae_audit_mo
        )

        return self.policy_global_aae_audit_mo
