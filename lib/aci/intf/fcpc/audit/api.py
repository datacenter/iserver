class InterfaceFcPcAuditApi():
    def __init__(self):
        self.interface_fcpc_audit_mo = {}

    def get_interface_fcpc_audit_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_fcpc_audit_mo:
            return self.interface_fcpc_audit_mo[key]

        cache = self.get_object_cache(
            'pcFcAggrIf.audit',
            object_selector=key
        )
        if cache is not None:
            self.interface_fcpc_audit_mo[key] = cache
            self.log.apic_mo(
                'pcFcAggrIf.audit.%s' % (key),
                self.interface_fcpc_audit_mo[key]
            )
            return self.interface_fcpc_audit_mo[key]

        class_name = 'topology/pod-%s/node-%s/pcFcAggrIf' % (pod_id, node_id)
        query = 'rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=%s' % (self.api_audit_limit)
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_fcpc_audit_mo',
                'API failed'
            )
            return None

        self.interface_fcpc_audit_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['aaaModLR']['attributes']
            self.interface_fcpc_audit_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'pcFcAggrIf.audit.%s' % (key),
            self.interface_fcpc_audit_mo[key]
        )

        self.set_object_cache(
            'pcFcAggrIf.audit',
            self.interface_fcpc_audit_mo[key],
            object_selector=key
        )

        return self.interface_fcpc_audit_mo[key]
