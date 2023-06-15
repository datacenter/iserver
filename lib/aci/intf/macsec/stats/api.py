class InterfaceMacSecStatsApi():
    def __init__(self):
        self.interface_macsec_stats_mo = {}

    def get_interface_macsec_stats_mo(self, pod_id, node_id, interface_id):
        key = '%s.%s.%s' % (
            pod_id,
            node_id,
            interface_id
        )
        if key in self.interface_macsec_stats_mo:
            return self.interface_macsec_stats_mo[key]

        cache = self.get_object_cache(
            'macsecIfStats',
            object_selector=key
        )
        if cache is not None:
            self.interface_macsec_stats_mo[key] = cache
            self.log.apic_mo(
                'macsecIfStats.%s' % (key),
                self.interface_macsec_stats_mo[key]
            )
            return self.interface_macsec_stats_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/macsec/inst/if-[%s]' % (
            pod_id,
            node_id,
            interface_id
        )
        query = 'query-target=children&target-subtree-class=macsecIfStats'

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_macsec_stats_mo',
                'API failed'
            )
            return None

        self.log.apic_mo(
            'macsecIfStats.%s' % (key),
            managed_objects
        )

        if managed_objects['totalCount'] == '0':
            self.interface_macsec_stats_mo[key] = []
            return self.interface_macsec_stats_mo[key]

        self.interface_macsec_stats_mo[key] = managed_objects['imdata'][0]['macsecIfStats']['attributes']

        self.log.apic_mo(
            'macsecIfStats.%s' % (key),
            self.interface_macsec_stats_mo[key]
        )

        self.set_object_cache(
            'macsecIfStats',
            self.interface_macsec_stats_mo[key],
            object_selector=key
        )

        return self.interface_macsec_stats_mo[key]
