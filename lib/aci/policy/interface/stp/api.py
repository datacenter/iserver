class PolicyInterfaceStpApi():
    def __init__(self):
        self.policy_interface_stp_mo = None

    def get_policy_interface_stp_mo(self):
        if self.policy_interface_stp_mo is not None:
            return self.policy_interface_stp_mo

        cache = self.get_object_cache(
            'stpIfPol'
        )
        if cache is not None:
            self.policy_interface_stp_mo = cache
            self.log.apic_mo(
                'stpIfPol',
                self.policy_interface_stp_mo
            )
            return self.policy_interface_stp_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'stpIfPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_stp_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['stpIfPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'stpIfPol'
            )

            self.policy_interface_stp_mo.append(
                attributes
            )

        self.log.apic_mo(
            'stpIfPol',
            self.policy_interface_stp_mo
        )

        self.set_object_cache(
            'stpIfPol',
            self.policy_interface_stp_mo
        )

        return self.policy_interface_stp_mo
