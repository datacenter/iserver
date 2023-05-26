class TabooSubjectApi():
    def __init__(self):
        self.taboo_subjects_mo = None

    def get_taboo_subjects_mo(self):
        if self.taboo_subjects_mo is not None:
            return self.taboo_subjects_mo

        query = 'rsp-subtree=children&rsp-subtree-class=vzRsDenyRule'
        managed_objects = self.get_class(
            'vzTSubj',
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_taboo_subjects_mo',
                'API failed'
            )
            return None

        self.log.apic_mo(
            'vzTSubj',
            managed_objects
        )

        self.taboo_subjects_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['vzTSubj']['attributes']
            attributes['vzRsDenyRule'] = self.get_mo_children_attributes(
                'vzTSubj',
                managed_object,
                'vzRsDenyRule'
            )
            self.taboo_subjects_mo.append(
                attributes
            )

        self.log.apic_mo(
            'vzTSubj',
            self.taboo_subjects_mo
        )

        return self.taboo_subjects_mo
