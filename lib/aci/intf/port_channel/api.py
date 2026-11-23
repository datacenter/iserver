class InterfacePortChannelApi():
    def __init__(self):
        self.interfaces_pc_mo = {}

    def get_interface_port_channels_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interfaces_pc_mo:
            return self.interfaces_pc_mo[key]

        cache = self.get_object_cache(
            'pcAggrIf',
            object_selector=key
        )
        if cache is not None:
            self.interfaces_pc_mo[key] = cache
            self.log.apic_mo(
                'pcAggrIf.%s' % (key),
                self.interfaces_pc_mo[key]
            )
            return self.interfaces_pc_mo[key]

        class_name = 'topology/pod-%s/node-%s/pcAggrIf' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-include=health,fault-count,required'
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
                'ethpmAggrIf',
                include_grandchildren=True
            )
            attributes['rmonIfOut'] = self.get_mo_child_attributes(
                'pcAggrIf',
                managed_object,
                'rmonIfOut'
            )
            attributes['rmonIfIn'] = self.get_mo_child_attributes(
                'pcAggrIf',
                managed_object,
                'rmonIfIn'
            )
            attributes['rmonEtherStats'] = self.get_mo_child_attributes(
                'pcAggrIf',
                managed_object,
                'rmonEtherStats'
            )
            attributes['pcRsMbrIfs'] = self.get_mo_children_attributes(
                'pcAggrIf',
                managed_object,
                'pcRsMbrIfs',
                include_grandchildren=True
            )
            attributes['healthInst'] = self.get_mo_child_attributes(
                'pcAggrIf',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'pcAggrIf',
                managed_object,
                'faultCounts'
            )

            self.interfaces_pc_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'pcAggrIf.%s' % (key),
            self.interfaces_pc_mo[key]
        )

        self.set_object_cache(
            'pcAggrIf',
            self.interfaces_pc_mo[key],
            object_selector=key
        )

        return self.interfaces_pc_mo[key]
