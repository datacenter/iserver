class ProtocolLldpStatsApi():
    def __init__(self):
        self.protocol_lldp_stats_mo = {}

    def get_protocol_lldp_stats_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.protocol_lldp_stats_mo:
            return self.protocol_lldp_stats_mo[key]

        cache = self.get_object_cache(
            'lldpInstStats',
            object_selector=key
        )
        if cache is not None:
            self.protocol_lldp_stats_mo[key] = cache
            self.log.apic_mo(
                'lldpInstStats.%s' % (key),
                self.protocol_lldp_stats_mo[key]
            )
            return self.protocol_lldp_stats_mo[key]

        class_name = 'topology/pod-%s/node-%s/lldpInstStats' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name,
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_lldp_stats_mo',
                'API failed'
            )
            return None

        if int(managed_objects['totalCount']) > 1:
            self.log.error(
                'get_protocol_lldp_stats_mo',
                'Unexpected object count: %s' % (key)
            )
            return None

        if int(managed_objects['totalCount']) == 0:
            self.protocol_lldp_stats_mo[key] = {}
        else:
            self.protocol_lldp_stats_mo[key] = managed_objects['imdata'][0]['lldpInstStats']['attributes']

        self.log.apic_mo(
            'lldpInstStats.%s' % (key),
            self.protocol_lldp_stats_mo[key]
        )

        self.set_object_cache(
            'lldpInstStats',
            self.protocol_lldp_stats_mo[key],
            object_selector=key
        )

        return self.protocol_lldp_stats_mo[key]
