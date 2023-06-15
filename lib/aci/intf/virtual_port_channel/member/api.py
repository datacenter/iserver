class InterfaceVirtualPortChannelMemberApi():
    def __init__(self):
        self.interface_vpc_members_mo = {}

    def get_interface_virtual_port_channel_members_mo(self, pod_id, node_id, vpc_domain_id):
        key = '%s.%s.%s' % (pod_id, node_id, vpc_domain_id)
        if key in self.interface_vpc_members_mo:
            return self.interface_vpc_members_mo[key]

        cache = self.get_object_cache(
            'vpcIf',
            object_selector=key
        )
        if cache is not None:
            self.interface_vpc_members_mo[key] = cache
            self.log.apic_mo(
                'vpcIf.%s' % (key),
                self.interface_vpc_members_mo[key]
            )
            return self.interface_vpc_members_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/vpc/inst/dom-%s' % (pod_id, node_id, vpc_domain_id)
        query = 'query-target=children&target-subtree-class=vpcIf'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_virtual_port_channel_members_mo',
                'API failed'
            )
            return None

        self.interface_vpc_members_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.interface_vpc_members_mo[key].append(
                managed_object['vpcIf']['attributes']
            )

        self.log.apic_mo(
            'vpcIf.%s' % (key),
            self.interface_vpc_members_mo[key]
        )

        self.set_object_cache(
            'vpcIf',
            self.interface_vpc_members_mo[key],
            object_selector=key
        )

        return self.interface_vpc_members_mo[key]
