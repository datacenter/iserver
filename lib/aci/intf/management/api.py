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
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_management_mo',
                'API failed'
            )
            return None

        self.interface_mgmt_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.interface_mgmt_mo[key].append(
                managed_object['mgmtMgmtIf']['attributes']
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
