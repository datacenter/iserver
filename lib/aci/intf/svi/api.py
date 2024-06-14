class InterfaceSviApi():
    def __init__(self):
        self.interface_svi_mo = {}

    def get_interface_svi_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_svi_mo:
            return self.interface_svi_mo[key]

        cache = self.get_object_cache(
            'sviIf',
            object_selector=key
        )
        if cache is not None:
            self.interface_svi_mo[key] = cache
            self.log.apic_mo(
                'sviIf.%s' % (key),
                self.interface_svi_mo[key]
            )
            return self.interface_svi_mo[key]

        class_name = 'topology/pod-%s/node-%s/l2BD' % (pod_id, node_id)
        query = 'rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_svi_mo',
                'API failed'
            )
            return None

        self.interface_svi_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l2BD']['attributes']
            for section in managed_object['l2BD']['children']:
                for section_key in section:
                    if section_key == 'sviIf':
                        attributes[section_key] = {}
                        for attribute in section[section_key]['attributes']:
                            attributes[section_key][attribute] = section[section_key]['attributes'][attribute]

                        for sub_section in section[section_key]['children']:
                            for sub_section_key in sub_section:
                                attributes[sub_section_key] = {}
                                for attribute in sub_section[sub_section_key]['attributes']:
                                    attributes[sub_section_key][attribute] = sub_section[sub_section_key]['attributes'][attribute]

            self.interface_svi_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'sviIf.%s' % (key),
            self.interface_svi_mo[key]
        )

        self.set_object_cache(
            'sviIf',
            self.interface_svi_mo[key],
            object_selector=key
        )

        return self.interface_svi_mo[key]
