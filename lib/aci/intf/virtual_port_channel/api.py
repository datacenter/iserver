class InterfaceVirtualPortChannelApi():
    def __init__(self):
        self.interfaces_vpc_mo = {}

    def get_interfaces_virtual_port_channel_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interfaces_vpc_mo:
            return self.interfaces_vpc_mo[key]

        cache = self.get_object_cache(
            'vpcDom',
            object_selector=key
        )
        if cache is not None:
            self.interfaces_vpc_mo[key] = cache
            self.log.apic_mo(
                'vpcDom.%s' % (key),
                self.interfaces_vpc_mo[key]
            )
            return self.interfaces_vpc_mo[key]

        class_name = 'topology/pod-%s/node-%s/vpcDom' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-include=health,fault-count,required'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interfaces_virtual_port_channel_mo',
                'API failed'
            )
            return None

        self.interfaces_vpc_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['vpcDom']['attributes']
            attributes['vpcIf'] = self.get_mo_children_attributes(
                'vpcDom',
                managed_object,
                'vpcIf',
                include_grandchildren=True
            )
            attributes['healthInst'] = self.get_mo_child_attributes(
                'vpcDom',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'vpcDom',
                managed_object,
                'faultCounts'
            )
            self.interfaces_vpc_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'vpcDom.%s' % (key),
            self.interfaces_vpc_mo[key]
        )

        self.set_object_cache(
            'vpcDom',
            self.interfaces_vpc_mo[key],
            object_selector=key
        )

        return self.interfaces_vpc_mo[key]
