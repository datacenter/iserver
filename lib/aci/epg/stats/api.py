class EpgStatsApi():
    def __init__(self):
        self.epg_stats_mo = None

    def get_epg_stats_mo(self):
        if self.epg_stats_mo is not None:
            return self.epg_stats_mo

        cache = self.get_object_cache(
            'fvAPathAtt'
        )
        if cache is not None:
            self.epg_stats_mo = cache
            self.log.apic_mo(
                'fvAPathAtt',
                self.epg_stats_mo
            )
            return self.epg_stats_mo

        managed_objects = self.get_class(
            'fvAPathAtt'
        )

        if managed_objects is None:
            self.log.error(
                'get_epg_stats_mo',
                'API failed'
            )
            return None

        self.epg_stats_mo = []
        for managed_object in managed_objects['imdata']:
            types = [
                'fvStPathAtt',
                'fvStNodeAtt',
                'fvAttEntityPathAtt',
                'fvDyPathAtt',
                'fvPhyNodeAtt',
                'fvDyNodeAtt'
            ]
            added = False
            for managed_object_type in types:
                if managed_object_type in managed_object:
                    attributes = managed_object[managed_object_type]['attributes']
                    attributes['type'] = managed_object_type
                    self.epg_stats_mo.append(
                        attributes
                    )
                    added = True
                    break

            if not added:
                self.log.error(
                    'get_epg_stats_mo',
                    'Unsupported object: %s' % (managed_object)
                )

        self.log.apic_mo(
            'fvAPathAtt',
            self.epg_stats_mo
        )

        self.set_object_cache(
            'fvAPathAtt',
            self.epg_stats_mo
        )

        return self.epg_stats_mo
