class PolicyGeneralAaeApi():
    def __init__(self):
        self.mo_policy_global_aae = None

    def initialize_policy_global_aae(self):
        if self.mo_policy_global_aae is not None:
            return True

        query = 'rsp-subtree=children&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP'
        managed_objects = self.get_class(
            'infraAttEntityP',
            query=query
        )

        if managed_objects is None:
            return False

        self.log.apic_mo(
            'infraAttEntityP.mo',
            managed_objects
        )

        self.mo_policy_global_aae = []
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

            self.mo_policy_global_aae.append(
                attributes
            )

        self.log.apic_mo(
            'infraAttEntityP',
            self.mo_policy_global_aae
        )

        return True
