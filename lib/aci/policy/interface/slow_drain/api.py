class PolicyInterfaceSlowDrainApi():
    def __init__(self):
        self.policy_interface_slow_drain_mo = None

    def get_policy_interface_slow_drain_mo(self):
        if self.policy_interface_slow_drain_mo is not None:
            return self.policy_interface_slow_drain_mo

        cache = self.get_object_cache(
            'qosSdIfPol'
        )
        if cache is not None:
            self.policy_interface_slow_drain_mo = cache
            self.log.apic_mo(
                'qosSdIfPol',
                self.policy_interface_slow_drain_mo
            )
            return self.policy_interface_slow_drain_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'qosSdIfPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_slow_drain_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['qosSdIfPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'qosSdIfPol'
            )

            self.policy_interface_slow_drain_mo.append(
                attributes
            )

        self.log.apic_mo(
            'qosSdIfPol',
            self.policy_interface_slow_drain_mo
        )

        self.set_object_cache(
            'qosSdIfPol',
            self.policy_interface_slow_drain_mo
        )

        return self.policy_interface_slow_drain_mo
