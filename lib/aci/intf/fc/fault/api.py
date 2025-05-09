class InterfaceFcFaultApi():
    def __init__(self):
        self.interface_fc_fault_mo = {}
        self.interface_fc_fault_record_mo = {}

    def get_interface_fc_fault_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_fc_fault_mo:
            return self.interface_fc_fault_mo[key]

        cache = self.get_object_cache(
            'l1FcPhysIf.fault',
            object_selector=key
        )
        if cache is not None:
            self.interface_fc_fault_mo[key] = cache
            self.log.apic_mo(
                'l1FcPhysIf.fault.%s' % (key),
                self.interface_fc_fault_mo[key]
            )
            return self.interface_fc_fault_mo[key]

        class_name = 'topology/pod-%s/node-%s/l1FcPhysIf' % (pod_id, node_id)
        query = 'rsp-subtree-include=faults,no-scoped,subtree'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_fc_fault_mo',
                'API failed'
            )
            return None

        self.interface_fc_fault_mo[key] = []
        for managed_object in managed_objects['imdata']:
            if 'faultInst' in managed_object:
                attributes = managed_object['faultInst']['attributes']
                attributes['object'] = 'faultInst'
                attributes['delegated'] = False

            if 'faultDelegate' in managed_object:
                attributes = managed_object['faultDelegate']['attributes']
                attributes['object'] = 'faultInst'
                attributes['delegated'] = True

            self.interface_fc_fault_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'l1FcPhysIf.fault.%s' % (key),
            self.interface_fc_fault_mo[key]
        )

        self.set_object_cache(
            'l1FcPhysIf.fault',
            self.interface_fc_fault_mo[key],
            object_selector=key
        )

        return self.interface_fc_fault_mo[key]

    def get_interface_fc_fault_record_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_fc_fault_record_mo:
            return self.interface_fc_fault_record_mo[key]

        cache = self.get_object_cache(
            'l1FcPhysIf.faultRecord',
            object_selector=key
        )
        if cache is not None:
            self.interface_fc_fault_record_mo[key] = cache
            self.log.apic_mo(
                'l1FcPhysIf.faultRecord.%s' % (key),
                self.interface_fc_fault_record_mo[key]
            )
            return self.interface_fc_fault_record_mo[key]

        class_name = 'topology/pod-%s/node-%s/l1FcPhysIf' % (pod_id, node_id)
        query = 'rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=%s' % (self.api_fault_limit)
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_fc_fault_record_mo',
                'API failed'
            )
            return None

        self.interface_fc_fault_record_mo[key] = []
        for managed_object in managed_objects['imdata']:
            if 'faultRecord' in managed_object:
                attributes = managed_object['faultRecord']['attributes']
                attributes['object'] = 'faultRecord'
                attributes['delegated'] = False

            if 'faultDelegate' in managed_object:
                attributes = managed_object['faultDelegate']['attributes']
                attributes['object'] = 'faultRecord'
                attributes['delegated'] = True

            self.interface_fc_fault_record_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'l1FcPhysIf.faultRecord.%s' % (key),
            self.interface_fc_fault_record_mo[key]
        )

        self.set_object_cache(
            'l1FcPhysIf.faultRecord',
            self.interface_fc_fault_record_mo[key],
            object_selector=key
        )

        return self.interface_fc_fault_record_mo[key]
