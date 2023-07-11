class InterfaceSviFaultApi():
    def __init__(self):
        self.interface_svi_fault_mo = {}

    def get_interface_svi_fault_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_svi_fault_mo:
            return self.interface_svi_fault_mo[key]

        cache = self.get_object_cache(
            'svi.fault',
            object_selector=key
        )
        if cache is not None:
            self.interface_svi_fault_mo[key] = cache
            self.log.apic_mo(
                'svi.fault.%s' % (key),
                self.interface_svi_fault_mo[key]
            )
            return self.interface_svi_fault_mo[key]

        class_name = 'topology/pod-%s/node-%s/l2BD' % (pod_id, node_id)
        query = 'rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=faults,fault-records,no-scoped,subtree'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_svi_fault_mo',
                'API failed'
            )
            return None

        self.interface_svi_fault_mo[key] = []
        for managed_object in managed_objects['imdata']:
            if 'faultRecord' in managed_object:
                attributes = managed_object['faultRecord']['attributes']
                attributes['object'] = 'faultRecord'

            if 'faultInst' in managed_object:
                attributes = managed_object['faultInst']['attributes']
                attributes['object'] = 'faultInst'

            self.interface_svi_fault_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'svi.fault.%s' % (key),
            self.interface_svi_fault_mo[key]
        )

        self.set_object_cache(
            'svi.fault',
            self.interface_svi_fault_mo[key],
            object_selector=key
        )

        return self.interface_svi_fault_mo[key]
