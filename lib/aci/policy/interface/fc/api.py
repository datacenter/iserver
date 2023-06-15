class PolicyInterfaceFcApi():
    def __init__(self):
        self.policy_interface_fc_mo = None

    def get_policy_interface_fc_mo(self):
        if self.policy_interface_fc_mo is not None:
            return self.policy_interface_fc_mo

        cache = self.get_object_cache(
            'fcIfPol'
        )
        if cache is not None:
            self.policy_interface_fc_mo = cache
            self.log.apic_mo(
                'fcIfPol',
                self.policy_interface_fc_mo
            )
            return self.policy_interface_fc_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'fcIfPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_fc_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fcIfPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'fcIfPol'
            )

            self.policy_interface_fc_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fcIfPol',
            self.policy_interface_fc_mo
        )

        self.set_object_cache(
            'fcIfPol',
            self.policy_interface_fc_mo
        )

        return self.policy_interface_fc_mo
