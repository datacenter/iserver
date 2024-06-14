class EpgLocaleApi():
    def __init__(self):
        self.epg_locale_mo = None

    def get_epg_locale_mo(self):
        if self.epg_locale_mo is not None:
            return self.epg_locale_mo

        cache = self.get_object_cache(
            'fvLocale'
        )
        if cache is not None:
            self.epg_locale_mo = cache
            self.log.apic_mo(
                'fvLocale',
                self.epg_locale_mo
            )
            return self.epg_locale_mo

        managed_objects = self.get_class(
            'fvLocale'
        )

        if managed_objects is None:
            self.log.error(
                'epg_locale_mo',
                'API failed'
            )
            return None

        self.epg_locale_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvLocale']['attributes']
            self.epg_locale_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fvLocale',
            self.epg_locale_mo
        )

        self.set_object_cache(
            'fvLocale',
            self.epg_locale_mo
        )

        return self.epg_locale_mo
