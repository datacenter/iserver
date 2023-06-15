class PolicyInterfaceCoppApi():
    def __init__(self):
        self.policy_interface_copp_mo = None

    def get_policy_interface_copp_mo(self):
        if self.policy_interface_copp_mo is not None:
            return self.policy_interface_copp_mo

        cache = self.get_object_cache(
            'coppIfPol'
        )
        if cache is not None:
            self.policy_interface_copp_mo = cache
            self.log.apic_mo(
                'coppIfPol',
                self.policy_interface_copp_mo
            )
            return self.policy_interface_copp_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'coppIfPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_copp_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['coppIfPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'coppIfPol'
            )

            self.policy_interface_copp_mo.append(
                attributes
            )

        self.log.apic_mo(
            'coppIfPol',
            self.policy_interface_copp_mo
        )

        self.set_object_cache(
            'coppIfPol',
            self.policy_interface_copp_mo
        )

        return self.policy_interface_copp_mo
