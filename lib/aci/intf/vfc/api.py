class InterfaceVfcApi():
    def __init__(self):
        self.interface_vfc_mo = {}

    def get_interface_vfc_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_vfc_mo:
            return self.interface_vfc_mo[key]

        cache = self.get_object_cache(
            'l2VfcIf',
            object_selector=key
        )
        if cache is not None:
            self.interface_vfc_mo[key] = cache
            self.log.apic_mo(
                'l2VfcIf.%s' % (key),
                self.interface_vfc_mo[key]
            )
            return self.interface_vfc_mo[key]

        class_name = 'topology/pod-%s/node-%s/l2VfcIf' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_vfc_mo',
                'API failed'
            )
            return None

        self.interface_vfc_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l2VfcIf']['attributes']
            self.interface_vfc_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'l2VfcIf.%s' % (key),
            self.interface_vfc_mo[key]
        )

        self.set_object_cache(
            'l2VfcIf',
            self.interface_vfc_mo[key],
            object_selector=key
        )

        return self.interface_vfc_mo[key]
