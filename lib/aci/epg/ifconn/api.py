class EpgIfConnApi():
    def __init__(self):
        self.epg_ifconn_mo = None

    def get_epg_ifconn_mo(self):
        if self.epg_ifconn_mo is not None:
            return self.epg_ifconn_mo

        cache = self.get_object_cache(
            'fvIfConn'
        )
        if cache is not None:
            self.epg_ifconn_mo = cache
            self.log.apic_mo(
                'fvIfConn',
                self.epg_ifconn_mo
            )
            return self.epg_ifconn_mo

        managed_objects = self.get_class(
            'fvIfConn'
        )

        if managed_objects is None:
            self.log.error(
                'epg_ifconn_mo',
                'API failed'
            )
            return None

        self.epg_ifconn_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvIfConn']['attributes']
            self.epg_ifconn_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fvIfConn',
            self.epg_ifconn_mo
        )

        self.set_object_cache(
            'fvIfConn',
            self.epg_ifconn_mo
        )

        return self.epg_ifconn_mo
