class ProtocolBfdFaultApi():
    def __init__(self):
        self.bfd_fault_mo = {}

    def get_protocol_bfd_fault_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bfd_fault_mo:
            return self.bfd_fault_mo[key]

        cache = self.get_object_cache(
            'bfdInst.fault',
            object_selector=key
        )
        if cache is not None:
            self.bfd_fault_mo[key] = cache
            self.log.apic_mo(
                'bfdInst.fault.%s' % (key),
                self.bfd_fault_mo[key]
            )
            return self.bfd_fault_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/bfd/inst' % (pod_id, node_id)
        query = 'rsp-subtree-include=faults,fault-records,no-scoped,subtree'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_bfd_fault_mo',
                'API failed'
            )
            return None

        self.bfd_fault_mo[key] = []
        for managed_object in managed_objects['imdata']:
            if 'faultRecord' in managed_object:
                attributes = managed_object['faultRecord']['attributes']
                attributes['object'] = 'faultRecord'

            if 'faultInst' in managed_object:
                attributes = managed_object['faultInst']['attributes']
                attributes['object'] = 'faultInst'

            self.bfd_fault_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'bfdInst.fault.%s' % (key),
            self.bfd_fault_mo[key]
        )

        self.set_object_cache(
            'bfdInst.fault',
            self.bfd_fault_mo[key],
            object_selector=key
        )

        return self.bfd_fault_mo[key]
