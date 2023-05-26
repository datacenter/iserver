class InterfaceMacSecApi():
    def __init__(self):
        self.interface_macsec_mo = {}

    def get_interface_macsec_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_macsec_mo:
            return self.interface_macsec_mo[key]

        class_name = 'topology/pod-%s/node-%s/macsecIf' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_macsec_mo',
                'API failed'
            )
            return None

        self.interface_macsec_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['macsecIf']['attributes']
            self.interface_macsec_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'macsecIf.%s' % (key),
            self.interface_macsec_mo[key]
        )

        return self.interface_macsec_mo[key]
