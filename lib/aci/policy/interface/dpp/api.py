class PolicyInterfaceDppApi():
    def __init__(self):
        self.policy_interface_dpp_mo = None

    def get_policy_interface_dpp_mo(self):
        if self.policy_interface_dpp_mo is not None:
            return self.policy_interface_dpp_mo

        cache = self.get_object_cache(
            'qosDppPol'
        )
        if cache is not None:
            self.policy_interface_dpp_mo = cache
            self.log.apic_mo(
                'qosDppPol',
                self.policy_interface_dpp_mo
            )
            return self.policy_interface_dpp_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'qosDppPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_dpp_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['qosDppPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'qosDppPol'
            )

            self.policy_interface_dpp_mo.append(
                attributes
            )

        self.log.apic_mo(
            'qosDppPol',
            self.policy_interface_dpp_mo
        )

        self.set_object_cache(
            'qosDppPol',
            self.policy_interface_dpp_mo
        )

        return self.policy_interface_dpp_mo
