class PolicyGeneralAaeApi():
    def __init__(self):
        self.policy_global_aae_mo = None

    def get_policy_global_aae_mo(self):
        if self.policy_global_aae_mo is not None:
            return self.policy_global_aae_mo

        cache = self.get_object_cache(
            'infraAttEntityP'
        )
        if cache is not None:
            self.policy_global_aae_mo = cache
            self.log.apic_mo(
                'infraAttEntityP',
                self.policy_global_aae_mo
            )
            return self.policy_global_aae_mo

        query = 'rsp-subtree=children&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP'
        managed_objects = self.get_class(
            'infraAttEntityP',
            query=query
        )

        if managed_objects is None:
            return None

        self.policy_global_aae_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['infraAttEntityP']['attributes']
            attributes['infraRtAttEntP'] = self.get_mo_children_attributes(
                'infraAttEntityP',
                managed_object,
                'infraRtAttEntP'
            )
            attributes['infraRsDomP'] = self.get_mo_children_attributes(
                'infraAttEntityP',
                managed_object,
                'infraRsDomP'
            )
            attributes['infraProvAcc'] = self.get_mo_child_attributes(
                'infraAttEntityP',
                managed_object,
                'infraProvAcc'
            )

            self.policy_global_aae_mo.append(
                attributes
            )

        self.log.apic_mo(
            'infraAttEntityP',
            self.policy_global_aae_mo
        )

        self.set_object_cache(
            'infraAttEntityP',
            self.policy_global_aae_mo
        )

        return self.policy_global_aae_mo
