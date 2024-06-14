class ProtocolHsrpInterfaceApi():
    def __init__(self):
        self.hsrp_interfaces_mo = {}

    def get_protocol_hsrp_interfaces_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.hsrp_interfaces_mo:
            return self.hsrp_interfaces_mo[key]

        cache = self.get_object_cache(
            'hsrpIf',
            object_selector=key
        )
        if cache is not None:
            self.hsrp_interfaces_mo[key] = cache
            self.log.apic_mo(
                'hsrpIf.%s' % (key),
                self.hsrp_interfaces_mo[key]
            )
            return self.hsrp_interfaces_mo[key]

        class_name = 'topology/pod-%s/node-%s/hsrpIf' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-class=hsrpIf,hsrpIfStats&rsp-subtree-include=required'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_hsrp_interfaces_mo',
                'API failed'
            )
            return None

        self.hsrp_interfaces_mo[key] = []
        for managed_object in managed_objects['imdata']:
            if 'hsrpIf' in managed_object:
                attributes = managed_object['hsrpIf']['attributes']
                attributes['stats'] = self.get_mo_child_attributes(
                    'hsrpIf',
                    managed_object,
                    'hsrpIfStats'
                )

                self.hsrp_interfaces_mo[key].append(
                    attributes
                )

        self.log.apic_mo(
            'hsrpIf.%s' % (key),
            self.hsrp_interfaces_mo[key]
        )

        self.set_object_cache(
            'hsrpIf',
            self.hsrp_interfaces_mo[key],
            object_selector=key
        )

        return self.hsrp_interfaces_mo[key]
