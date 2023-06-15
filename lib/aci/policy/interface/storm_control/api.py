class PolicyInterfaceStormControlApi():
    def __init__(self):
        self.policy_interface_storm_control_mo = None

    def get_policy_interface_storm_control_mo(self):
        if self.policy_interface_storm_control_mo is not None:
            return self.policy_interface_storm_control_mo

        cache = self.get_object_cache(
            'stormctrlIfPol'
        )
        if cache is not None:
            self.policy_interface_storm_control_mo = cache
            self.log.apic_mo(
                'stormctrlIfPol',
                self.policy_interface_storm_control_mo
            )
            return self.policy_interface_storm_control_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'stormctrlIfPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_storm_control_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['stormctrlIfPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'stormctrlIfPol'
            )

            self.policy_interface_storm_control_mo.append(
                attributes
            )

        self.log.apic_mo(
            'stormctrlIfPol',
            self.policy_interface_storm_control_mo
        )

        self.set_object_cache(
            'stormctrlIfPol',
            self.policy_interface_storm_control_mo
        )

        return self.policy_interface_storm_control_mo
