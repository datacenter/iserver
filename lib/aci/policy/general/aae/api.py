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

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP'
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
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'infraAttEntityP',
                managed_object,
                'faultCounts'
            )
            attributes['infraRsFuncToEpg'] = []

            self.policy_global_aae_mo.append(
                attributes
            )

        query = 'query-target=subtree&target-subtree-class=infraAttEntityP&target-subtree-class=infraRsFuncToEpg'
        managed_objects = self.get_managed_object(
            'uni/infra',
            query=query,
            node_mo=True
        )
        if managed_objects is None:
            return None

        for managed_object in managed_objects['imdata']:
            if 'infraRsFuncToEpg' in managed_object:
                # "dn": "uni/infra/attentp-k8s_phys_AAEP/gen-default/rsfuncToEpg-[uni/tn-k8s/ap-k8s_ANP/epg-csr1_lan]"
                ref_dn = '/'.join(
                    managed_object['infraRsFuncToEpg']['attributes']['dn'].split('/')[:3]
                )
                for policy_mo in self.policy_global_aae_mo:
                    if policy_mo['dn'] == ref_dn:
                        policy_mo['infraRsFuncToEpg'].append(
                            managed_object['infraRsFuncToEpg']['attributes']
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
