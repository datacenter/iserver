class PolicyInterfaceLinkLevelApi():
    def __init__(self):
        self.policy_interface_link_level_mo = None

    def get_policy_interface_link_level_mo(self):
        if self.policy_interface_link_level_mo is not None:
            return self.policy_interface_link_level_mo

        cache = self.get_object_cache(
            'fabricHIfPol'
        )
        if cache is not None:
            self.policy_interface_link_level_mo = cache
            self.log.apic_mo(
                'fabricHIfPol',
                self.policy_interface_link_level_mo
            )
            return self.policy_interface_link_level_mo

        query = 'rsp-subtree=children&rsp-subtree-class=relnFrom'
        managed_objects = self.get_class(
            'fabricHIfPol',
            query=query
        )
        if managed_objects is None:
            return None

        self.policy_interface_link_level_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fabricHIfPol']['attributes']
            attributes['relnFrom'] = self.get_policy_interface_reln(
                managed_object,
                'fabricHIfPol'
            )

            self.policy_interface_link_level_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fabricHIfPol',
            self.policy_interface_link_level_mo
        )

        self.set_object_cache(
            'fabricHIfPol',
            self.policy_interface_link_level_mo
        )

        return self.policy_interface_link_level_mo
