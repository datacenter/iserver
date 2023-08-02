class EpgApi():
    def __init__(self):
        self.epg_mo = None

    def get_epg_mo(self):
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

        query = 'rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt'
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
            attributes['fvRsProtBy'] = self.get_mo_children_attributes(
                'fvAEPg',
                managed_object,
                'fvRsProtBy'
            )
            attributes['fvMatchEPg'] = self.get_mo_children_attributes(
                'fvAEPg',
                managed_object,
                'fvRtMatchEPg'
            )
            attributes['fvRsPathAtt'] = self.get_mo_children_attributes(
                'fvAEPg',
                managed_object,
                'fvRsPathAtt'
            )
            attributes['fvRsDomAtt'] = self.get_mo_children_attributes(
                'fvAEPg',
                managed_object,
                'fvRsDomAtt'
            )
            attributes['healthInst'] = self.get_mo_child_attributes(
                'fvAEPg',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'fvAEPg',
                managed_object,
                'faultCounts'
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
