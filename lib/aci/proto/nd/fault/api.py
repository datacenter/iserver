class ProtocolNdFaultApi():
    def __init__(self):
        self.proto_nd_fault_mo = {}
        self.proto_nd_fault_record_mo = {}

    def get_protocol_nd_fault_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.proto_nd_fault_mo:
            return self.proto_nd_fault_mo[key]

        cache = self.get_object_cache(
            'ndDom.fault',
            object_selector=key
        )
        if cache is not None:
            self.proto_nd_fault_mo[key] = cache
            self.log.apic_mo(
                'ndDom.fault.%s' % (key),
                self.proto_nd_fault_mo[key]
            )
            return self.proto_nd_fault_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/nd' % (pod_id, node_id)
        query = 'rsp-subtree-include=faults,no-scoped,subtree'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_nd_fault_mo',
                'API failed'
            )
            return None

        self.proto_nd_fault_mo[key] = []
        for managed_object in managed_objects['imdata']:
            if 'faultInst' in managed_object:
                attributes = managed_object['faultInst']['attributes']
                attributes['object'] = 'faultInst'
                attributes['delegated'] = False

            if 'faultDelegate' in managed_object:
                attributes = managed_object['faultDelegate']['attributes']
                attributes['object'] = 'faultInst'
                attributes['delegated'] = True

            self.proto_nd_fault_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'ndDom.fault.%s' % (key),
            self.proto_nd_fault_mo[key]
        )

        self.set_object_cache(
            'ndDom.fault',
            self.proto_nd_fault_mo[key],
            object_selector=key
        )

        return self.proto_nd_fault_mo[key]

    def get_protocol_nd_fault_record_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.proto_nd_fault_record_mo:
            return self.proto_nd_fault_record_mo[key]

        cache = self.get_object_cache(
            'ndDom.faultRecord',
            object_selector=key
        )
        if cache is not None:
            self.proto_nd_fault_record_mo[key] = cache
            self.log.apic_mo(
                'ndDom.faultRecord.%s' % (key),
                self.proto_nd_fault_record_mo[key]
            )
            return self.proto_nd_fault_record_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/nd' % (pod_id, node_id)
        query = 'rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=%s' % (self.api_fault_limit)
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_nd_fault_record_mo',
                'API failed'
            )
            return None

        self.proto_nd_fault_record_mo[key] = []
        for managed_object in managed_objects['imdata']:
            if 'faultRecord' in managed_object:
                attributes = managed_object['faultRecord']['attributes']
                attributes['object'] = 'faultRecord'
                attributes['delegated'] = False

            if 'faultDelegate' in managed_object:
                attributes = managed_object['faultDelegate']['attributes']
                attributes['object'] = 'faultRecord'
                attributes['delegated'] = True

            self.proto_nd_fault_record_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'ndDom.faultRecord.%s' % (key),
            self.proto_nd_fault_record_mo[key]
        )

        self.set_object_cache(
            'ndDom.faultRecord',
            self.proto_nd_fault_record_mo[key],
            object_selector=key
        )

        return self.proto_nd_fault_record_mo[key]
