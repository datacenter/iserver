class InterfaceLacpApi():
    def __init__(self):
        self.interfaces_lacp_mo = {}

    def get_interfaces_lacp_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interfaces_lacp_mo:
            return self.interfaces_lacp_mo[key]

        cache = self.get_object_cache(
            'lacpIf',
            object_selector=key
        )
        if cache is not None:
            self.interfaces_lacp_mo[key] = cache
            self.log.apic_mo(
                'lacpIf.%s' % (key),
                self.interfaces_lacp_mo[key]
            )
            return self.interfaces_lacp_mo[key]

        class_name = 'topology/pod-%s/node-%s/lacpIf' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-class=lacpIfStats'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interfaces_lacp_mo',
                'API failed'
            )
            return False

        self.interfaces_lacp_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['lacpIf']['attributes']
            attributes['stats'] = self.get_mo_child_attributes(
                'lacpIf',
                managed_object,
                'lacpIfStats'
            )

            self.interfaces_lacp_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'lacpIf.%s' % (key),
            self.interfaces_lacp_mo[key]
        )

        self.set_object_cache(
            'lacpIf',
            self.interfaces_lacp_mo[key],
            object_selector=key
        )

        return self.interfaces_lacp_mo[key]
