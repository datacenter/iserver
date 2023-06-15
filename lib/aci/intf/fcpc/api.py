class InterfaceFcPcApi():
    def __init__(self):
        self.interface_fcpc_mo = {}

    def get_interface_fcpc_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_fcpc_mo:
            return self.interface_fcpc_mo[key]

        cache = self.get_object_cache(
            'ipv4Addr',
            object_selector=key
        )
        if cache is not None:
            self.interface_fcpc_mo[key] = cache
            self.log.apic_mo(
                'pcFcAggrIf.%s' % (key),
                self.interface_fcpc_mo[key]
            )
            return self.interface_fcpc_mo[key]

        class_name = 'topology/pod-%s/node-%s/pcFcAggrIf' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_fcpc_mo',
                'API failed'
            )
            return None

        self.interface_fcpc_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['pcFcAggrIf']['attributes']
            self.interface_fcpc_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'pcFcAggrIf.%s' % (key),
            self.interface_fcpc_mo[key]
        )

        self.set_object_cache(
            'pcFcAggrIf',
            self.interface_fcpc_mo[key],
            object_selector=key
        )

        return self.interface_fcpc_mo[key]
