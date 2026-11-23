class PolicyInterfaceLinkFlapApi():
    def __init__(self):
        self.policy_interface_link_flap_mo = None

    def get_policy_interface_link_flap_mo(self):
        if self.policy_interface_link_flap_mo is not None:
            return self.policy_interface_link_flap_mo

        cache = self.get_object_cache(
            'fabricLinkFlapPol'
        )
        if cache is not None:
            self.policy_interface_link_flap_mo = cache
            self.log.apic_mo(
                'fabricLinkFlapPol',
                self.policy_interface_link_flap_mo
            )
            return self.policy_interface_link_flap_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'fabricLinkFlapPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_link_flap_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fabricLinkFlapPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'fabricLinkFlapPol'
            )

            self.policy_interface_link_flap_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fabricLinkFlapPol',
            self.policy_interface_link_flap_mo
        )

        self.set_object_cache(
            'fabricLinkFlapPol',
            self.policy_interface_link_flap_mo
        )

        return self.policy_interface_link_flap_mo
