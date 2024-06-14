class PolicyInterfaceLldpApi():
    def __init__(self):
        self.policy_interface_lldp_mo = None

    def get_policy_interface_lldp_mo(self):
        if self.policy_interface_lldp_mo is not None:
            return self.policy_interface_lldp_mo

        cache = self.get_object_cache(
            'lldpIfPol'
        )
        if cache is not None:
            self.policy_interface_lldp_mo = cache
            self.log.apic_mo(
                'lldpIfPol',
                self.policy_interface_lldp_mo
            )
            return self.policy_interface_lldp_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'lldpIfPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_lldp_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['lldpIfPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'lldpIfPol'
            )

            self.policy_interface_lldp_mo.append(
                attributes
            )

        self.log.apic_mo(
            'lldpIfPol',
            self.policy_interface_lldp_mo
        )

        self.set_object_cache(
            'lldpIfPol',
            self.policy_interface_lldp_mo
        )

        return self.policy_interface_lldp_mo
