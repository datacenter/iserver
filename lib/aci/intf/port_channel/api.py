class InterfacePortChannelApi():
    def __init__(self):
        self.interfaces_pc_mo = {}

    def get_interface_port_channels_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interfaces_pc_mo:
            return self.interfaces_pc_mo[key]

        class_name = 'topology/pod-%s/node-%s/pcAggrIf' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-class=ethpmAggrIf'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_port_channels_mo',
                'API failed'
            )
            return None

        self.interfaces_pc_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['pcAggrIf']['attributes']
            attributes['ethpmAggrIf'] = self.get_mo_child_attributes(
                'pcAggrIf',
                managed_object,
                'ethpmAggrIf'
            )

            self.interfaces_pc_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'pcAggrIf.%s' % (key),
            self.interfaces_pc_mo[key]
        )

        return self.interfaces_pc_mo[key]
