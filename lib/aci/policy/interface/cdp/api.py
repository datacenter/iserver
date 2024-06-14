class PolicyInterfaceCdpApi():
    def __init__(self):
        self.policy_interface_cdp_mo = None

    def get_policy_interface_cdp_mo(self):
        if self.policy_interface_cdp_mo is not None:
            return self.policy_interface_cdp_mo

        cache = self.get_object_cache(
            'cdpIfPol'
        )
        if cache is not None:
            self.policy_interface_cdp_mo = cache
            self.log.apic_mo(
                'cdpIfPol',
                self.policy_interface_cdp_mo
            )
            return self.policy_interface_cdp_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'cdpIfPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_cdp_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['cdpIfPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'cdpIfPol'
            )

            self.policy_interface_cdp_mo.append(
                attributes
            )

        self.log.apic_mo(
            'cdpIfPol',
            self.policy_interface_cdp_mo
        )

        self.set_object_cache(
            'cdpIfPol',
            self.policy_interface_cdp_mo
        )

        return self.policy_interface_cdp_mo
