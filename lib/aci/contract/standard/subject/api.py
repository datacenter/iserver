class ContractSubjectApi():
    def __init__(self):
        self.subjects_mo = None

    def get_subjects_mo(self):
        if self.subjects_mo is not None:
            return self.subjects_mo

        cache = self.get_object_cache(
            'vzSubj'
        )
        if cache is not None:
            self.subjects_mo = cache
            self.log.apic_mo(
                'vzSubj',
                self.subjects_mo
            )
            return self.subjects_mo

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsSubjFiltAtt'
        managed_objects = self.get_class(
            'vzSubj',
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_subjects_mo',
                'API failed'
            )
            return None

        self.subjects_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['vzSubj']['attributes']
            attributes['vzRsSubjFiltAtt'] = self.get_mo_children_attributes(
                'vzSubj',
                managed_object,
                'vzRsSubjFiltAtt'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'vzSubj',
                managed_object,
                'faultCounts'
            )
            self.subjects_mo.append(
                attributes
            )

        self.log.apic_mo(
            'vzSubj',
            self.subjects_mo
        )

        self.set_object_cache(
            'vzSubj',
            self.subjects_mo
        )

        return self.subjects_mo
