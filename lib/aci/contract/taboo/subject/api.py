class ContractTabooSubjectApi():
    def __init__(self):
        self.taboo_contract_subject_mo = None

    def get_taboo_contract_subject_mo(self):
        if self.taboo_contract_subject_mo is not None:
            return self.taboo_contract_subject_mo

        cache = self.get_object_cache(
            'vzTSubj'
        )
        if cache is not None:
            self.taboo_contract_subject_mo = cache
            self.log.apic_mo(
                'vzTSubj',
                self.taboo_contract_subject_mo
            )
            return self.taboo_contract_subject_mo

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsDenyRule'
        managed_objects = self.get_class(
            'vzTSubj',
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_taboo_contract_subject_mo',
                'API failed'
            )
            return None

        self.taboo_contract_subject_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['vzTSubj']['attributes']
            attributes['vzRsDenyRule'] = self.get_mo_children_attributes(
                'vzTSubj',
                managed_object,
                'vzRsDenyRule'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'vzTSubj',
                managed_object,
                'faultCounts'
            )
            self.taboo_contract_subject_mo.append(
                attributes
            )

        self.log.apic_mo(
            'vzTSubj',
            self.taboo_contract_subject_mo
        )

        self.set_object_cache(
            'vzTSubj',
            self.taboo_contract_subject_mo
        )

        return self.taboo_contract_subject_mo
