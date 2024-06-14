class InterfaceVirtualPortChannelAuditApi():
    def __init__(self):
        self.interface_virtual_port_channel_audit_mo = {}

    def get_interface_virtual_port_channel_audit_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_virtual_port_channel_audit_mo:
            return self.interface_virtual_port_channel_audit_mo[key]

        cache = self.get_object_cache(
            'vpcDom.audit',
            object_selector=key
        )
        if cache is not None:
            self.interface_virtual_port_channel_audit_mo[key] = cache
            self.log.apic_mo(
                'vpcDom.audit.%s' % (key),
                self.interface_virtual_port_channel_audit_mo[key]
            )
            return self.interface_virtual_port_channel_audit_mo[key]

        class_name = 'topology/pod-%s/node-%s/vpcDom' % (pod_id, node_id)
        query = 'rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=%s' % (self.api_audit_limit)
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_virtual_port_channel_audit_mo',
                'API failed'
            )
            return None

        self.interface_virtual_port_channel_audit_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['aaaModLR']['attributes']
            self.interface_virtual_port_channel_audit_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'vpcDom.audit.%s' % (key),
            self.interface_virtual_port_channel_audit_mo[key]
        )

        self.set_object_cache(
            'vpcDom.audit',
            self.interface_virtual_port_channel_audit_mo[key],
            object_selector=key
        )

        return self.interface_virtual_port_channel_audit_mo[key]
