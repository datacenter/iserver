class InterfaceVirtualPortChannelApi():
    def __init__(self):
        self.interfaces_vpc_mo = {}

    def get_interfaces_virtual_port_channel_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interfaces_vpc_mo:
            return self.interfaces_vpc_mo[key]

        class_name = 'topology/pod-%s/node-%s/vpcDom' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name
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
            self.interfaces_vpc_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'vpcDom.%s' % (key),
            self.interfaces_vpc_mo[key]
        )

        return self.interfaces_vpc_mo[key]
