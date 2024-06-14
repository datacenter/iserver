class PolicyInterfacePortChannelMemberApi():
    def __init__(self):
        self.policy_interface_port_channel_member_mo = None

    def get_policy_interface_port_channel_member_mo(self):
        if self.policy_interface_port_channel_member_mo is not None:
            return self.policy_interface_port_channel_member_mo

        cache = self.get_object_cache(
            'lacpIfPol'
        )
        if cache is not None:
            self.policy_interface_port_channel_member_mo = cache
            self.log.apic_mo(
                'lacpIfPol',
                self.policy_interface_port_channel_member_mo
            )
            return self.policy_interface_port_channel_member_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'lacpIfPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_port_channel_member_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['lacpIfPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'lacpIfPol'
            )

            self.policy_interface_port_channel_member_mo.append(
                attributes
            )

        self.log.apic_mo(
            'lacpIfPol',
            self.policy_interface_port_channel_member_mo
        )

        self.set_object_cache(
            'lacpIfPol',
            self.policy_interface_port_channel_member_mo
        )

        return self.policy_interface_port_channel_member_mo
