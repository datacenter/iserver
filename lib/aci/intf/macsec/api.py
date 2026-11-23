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

        cache = self.get_object_cache(
            'macsecIf',
            object_selector=key
        )
        if cache is not None:
            self.interface_macsec_mo[key] = cache
            self.log.apic_mo(
                'macsecIf.%s' % (key),
                self.interface_macsec_mo[key]
            )
            return self.interface_macsec_mo[key]

        class_name = 'topology/pod-%s/node-%s/macsecIf' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-include=health,fault-count,required'
        managed_objects = self.get_class(
            class_name,
            query=query
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
            attributes['healthInst'] = self.get_mo_child_attributes(
                'macsecIf',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'macsecIf',
                managed_object,
                'faultCounts'
            )
            self.interface_macsec_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'macsecIf.%s' % (key),
            self.interface_macsec_mo[key]
        )

        self.set_object_cache(
            'macsecIf',
            self.interface_macsec_mo[key],
            object_selector=key
        )

        return self.interface_macsec_mo[key]
