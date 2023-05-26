class TabooApi():
    def __init__(self):
        self.taboos_mo = None

    def get_taboos_mo(self):
        if self.taboos_mo is not None:
            return self.taboos_mo

        query = 'rsp-subtree=children&rsp-subtree-class=vzTSubj,vzRtProtBy'
        managed_objects = self.get_class(
            'vzTaboo',
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_taboos_mo',
                'API failed'
            )
            return None

        self.taboos_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['vzTaboo']['attributes']
            attributes['vzTSubj'] = self.get_mo_children_attributes(
                'vzTaboo',
                managed_object,
                'vzTSubj'
            )
            attributes['vzRtProtBy'] = self.get_mo_children_attributes(
                'vzTaboo',
                managed_object,
                'vzRtProtBy'
            )
            self.taboos_mo.append(
                attributes
            )

        self.log.apic_mo(
            'vzTaboo',
            self.taboos_mo
        )

        return self.taboos_mo
