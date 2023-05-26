class FilterApi():
    def __init__(self):
        self.filters_mo = None

    def get_filters_mo(self):
        if self.filters_mo is not None:
            return self.filters_mo

        query = 'rsp-subtree=children&rsp-subtree-class=vzEntry'
        managed_objects = self.get_class(
            'vzFilter',
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_filters_mo',
                'API failed'
            )
            return None

        self.filters_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['vzFilter']['attributes']
            attributes['vzEntry'] = self.get_mo_children_attributes(
                'vzFilter',
                managed_object,
                'vzEntry'
            )
            self.filters_mo.append(
                attributes
            )

        self.log.apic_mo(
            'vzFilter',
            self.filters_mo
        )

        return self.filters_mo
