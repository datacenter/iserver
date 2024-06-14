class PolicyInterfaceL2Api():
    def __init__(self):
        self.policy_interface_l2_mo = None

    def get_policy_interface_l2_mo(self):
        if self.policy_interface_l2_mo is not None:
            return self.policy_interface_l2_mo

        cache = self.get_object_cache(
            'l2IfPol'
        )
        if cache is not None:
            self.policy_interface_l2_mo = cache
            self.log.apic_mo(
                'l2IfPol',
                self.policy_interface_l2_mo
            )
            return self.policy_interface_l2_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'l2IfPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_l2_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l2IfPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'l2IfPol'
            )

            self.policy_interface_l2_mo.append(
                attributes
            )

        self.log.apic_mo(
            'l2IfPol',
            self.policy_interface_l2_mo
        )

        self.set_object_cache(
            'l2IfPol',
            self.policy_interface_l2_mo
        )

        return self.policy_interface_l2_mo
