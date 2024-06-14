class PolicyInterfacePortChannelApi():
    def __init__(self):
        self.policy_interface_port_channel_mo = None

    def get_policy_interface_port_channel_mo(self):
        if self.policy_interface_port_channel_mo is not None:
            return self.policy_interface_port_channel_mo

        cache = self.get_object_cache(
            'lacpLagPol'
        )
        if cache is not None:
            self.policy_interface_port_channel_mo = cache
            self.log.apic_mo(
                'lacpLagPol',
                self.policy_interface_port_channel_mo
            )
            return self.policy_interface_port_channel_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'lacpLagPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.log.apic_mo(
            'lacpLagPol.raw',
            managed_objects
        )

        self.policy_interface_port_channel_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['lacpLagPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'lacpLagPol'
            )

            self.policy_interface_port_channel_mo.append(
                attributes
            )

        self.log.apic_mo(
            'lacpLagPol',
            self.policy_interface_port_channel_mo
        )

        self.set_object_cache(
            'lacpLagPol',
            self.policy_interface_port_channel_mo
        )

        return self.policy_interface_port_channel_mo
