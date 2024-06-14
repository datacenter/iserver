class InterfaceFaultCountsApi():
    def __init__(self):
        self.interface_fault_counts_mo = {}

    def get_interface_fault_counts_mo(self, pod_id, node_id, interface_type, interface_id):
        key = '%s.%s.%s' % (
            pod_id,
            node_id,
            interface_id
        )
        if key in self.interface_fault_counts_mo:
            return self.interface_fault_counts_mo[key]

        cache = self.get_object_cache(
            'fltCnts',
            object_selector=key
        )
        if cache is not None:
            self.interface_fault_counts_mo[key] = cache
            self.log.apic_mo(
                'fltCnts.%s' % (key),
                self.interface_fault_counts_mo[key]
            )
            return self.interface_fault_counts_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/%s-[%s]/fltCnts' % (
            pod_id,
            node_id,
            interface_type,
            interface_id
        )
        managed_objects = self.get_managed_object(
            distinguished_name
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_fault_counts_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_interface_fault_counts_mo',
                'Unexpected object count'
            )
            return None

        self.interface_fault_counts_mo[key] = managed_objects['imdata'][0]['faultCounts']['attributes']

        self.log.apic_mo(
            'fltCnts.%s' % (key),
            self.interface_fault_counts_mo[key]
        )

        self.set_object_cache(
            'fltCnts',
            self.interface_fault_counts_mo[key],
            object_selector=key
        )

        return self.interface_fault_counts_mo[key]
