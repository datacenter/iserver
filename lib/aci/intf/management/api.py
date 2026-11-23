class InterfaceMgmtApi():
    def __init__(self):
        self.interface_mgmt_mo = {}

    def get_interface_management_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_mgmt_mo:
            return self.interface_mgmt_mo[key]

        cache = self.get_object_cache(
            'mgmtMgmtIf',
            object_selector=key
        )
        if cache is not None:
            self.interface_mgmt_mo[key] = cache
            self.log.apic_mo(
                'mgmtMgmtIf.%s' % (key),
                self.interface_mgmt_mo[key]
            )
            return self.interface_mgmt_mo[key]

        class_name = 'topology/pod-%s/node-%s/mgmtMgmtIf' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-include=health,fault-count,required'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_management_mo',
                'API failed'
            )
            return None

        self.interface_mgmt_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['mgmtMgmtIf']['attributes']
            attributes['healthInst'] = self.get_mo_child_attributes(
                'mgmtMgmtIf',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'mgmtMgmtIf',
                managed_object,
                'faultCounts'
            )
            self.interface_mgmt_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'mgmtMgmtIf.%s' % (key),
            self.interface_mgmt_mo[key]
        )

        self.set_object_cache(
            'mgmtMgmtIf',
            self.interface_mgmt_mo[key],
            object_selector=key
        )

        return self.interface_mgmt_mo[key]
