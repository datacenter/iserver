class EpgApi():
    def __init__(self):
        self.epg_mo = None
        self.epg_deployed_leaves_mo = None

    def get_epgs_mo(self):
        if self.epg_mo is not None:
            return self.epg_mo

        cache = self.get_object_cache(
            'fvAEPg'
        )
        if cache is not None:
            self.epg_mo = cache
            self.log.apic_mo(
                'fvAEPg',
                self.epg_mo
            )
            return self.epg_mo

        query = 'rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg'
        managed_objects = self.get_class(
            'fvAEPg',
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_epgs_mo',
                'API failed'
            )
            return None

        self.epg_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvAEPg']['attributes']
            attributes['fvBD'] = self.get_mo_children_attributes(
                'fvAEPg',
                managed_object,
                'fvRsBd'
            )
            attributes['fvRsCons'] = self.get_mo_children_attributes(
                'fvAEPg',
                managed_object,
                'fvRsCons'
            )
            attributes['fvRsProv'] = self.get_mo_children_attributes(
                'fvAEPg',
                managed_object,
                'fvRsProv'
            )
            attributes['fvMatchEPg'] = self.get_mo_children_attributes(
                'fvAEPg',
                managed_object,
                'fvRtMatchEPg'
            )
            self.epg_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fvAEPg',
            self.epg_mo
        )

        self.set_object_cache(
            'fvAEPg',
            self.epg_mo
        )

        return self.epg_mo

    def get_epgs_deployed_leaves_mo(self):
        if self.epg_deployed_leaves_mo is not None:
            return self.epg_deployed_leaves_mo

        cache = self.get_object_cache(
            'fvAREpP'
        )
        if cache is not None:
            self.epg_deployed_leaves_mo = cache
            self.log.apic_mo(
                'fvAREpP',
                self.epg_deployed_leaves_mo
            )
            return self.epg_deployed_leaves_mo

        query = 'rsp-subtree=children&rsp-subtree-class=fvLocale'
        managed_objects = self.get_class(
            'fvAREpP',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'add_epgs_deployed_leaves_mo',
                'API failed'
            )
            return None

        self.epg_deployed_leaves_mo = []
        for managed_object in managed_objects['imdata']:
            if 'fvEpP' in managed_object:
                attributes = managed_object['fvEpP']['attributes']
                attributes['fvLocale'] = self.get_mo_children_attributes(
                    'fvEpP',
                    managed_object,
                    'fvLocale'
                )
                self.epg_deployed_leaves_mo.append(
                    attributes
                )

        self.log.apic_mo(
            'fvAREpP',
            self.epg_deployed_leaves_mo
        )

        self.set_object_cache(
            'fvAREpP',
            self.epg_deployed_leaves_mo
        )

        return self.epg_deployed_leaves_mo
