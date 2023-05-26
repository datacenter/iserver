class InterfaceFcApi():
    def __init__(self):
        self.interface_fc_mo = {}

    def get_interface_fc_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_fc_mo:
            return self.interface_fc_mo[key]

        class_name = 'topology/pod-%s/node-%s/l1FcPhysIf' % (pod_id, node_id)
        query = 'query-target=subtree&target-subtree-class=l1RtFcBrConf'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_fc_mo',
                'API failed'
            )
            return None

        self.interface_fc_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l1FcPhysIf']['attributes']
            attributes['ethpmLbRtdIf'] = self.get_mo_child_attributes(
                'l1FcPhysIf',
                managed_object,
                'l1RtFcBrConf'
            )
            self.interface_fc_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'l1FcPhysIf.%s' % (key),
            self.interface_fc_mo[key]
        )

        return self.interface_fc_mo[key]
