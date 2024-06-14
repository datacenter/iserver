class ProtocolBfdSessionStatsApi():
    def __init__(self):
        self.bfd_session_stats_mo = {}

    def set_protocol_bfd_session_stats_mo(self, managed_object):
        # "dn": "topology/pod-1/node-2208/sys/bfd/inst/session-1090519041/stats"

        stats_dn = managed_object['bfdSessStats']['attributes']['dn']
        pod_id = stats_dn.split('/')[1][4:]
        node_id = stats_dn.split('/')[2][5:]
        session_id = stats_dn.split('/')[6][8:]
        key = '%s.%s.%s' % (pod_id, node_id, session_id)

        self.bfd_session_stats_mo[key] = managed_object['bfdSessStats']['attributes']

        self.log.apic_mo(
            'bfdSessStats.%s' % (key),
            self.bfd_session_stats_mo[key]
        )

        self.set_object_cache(
            'bfdSessStats',
            self.bfd_session_stats_mo[key],
            object_selector=key
        )

    def get_protocol_bfd_session_stats_mo(self, pod_id, node_id, session_id):
        key = '%s.%s.%s' % (pod_id, node_id, session_id)
        if key in self.bfd_session_stats_mo:
            return self.bfd_session_stats_mo[key]

        cache = self.get_object_cache(
            'bfdSessStats',
            object_selector=key
        )
        if cache is not None:
            self.bfd_session_stats_mo[key] = cache
            self.log.apic_mo(
                'bfdSessStats.%s' % (key),
                self.bfd_session_stats_mo[key]
            )
            return self.bfd_session_stats_mo[key]

        # url: https://<apic>/api/node/mo/topology/pod-1/node-201/sys/bfd/inst/session-1090519172.json?query-target=children&target-subtree-class=bfdPeerV&subscription=yes
        distinguished_name = 'topology/pod-%s/node-%s/sys/bfd/inst/session-%s' % (pod_id, node_id, session_id)
        query = 'query-target=children&target-subtree-class=bfdSessStats'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_bfd_session_stats',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_protocol_bfd_session_stats',
                'Unexpected objects count'
            )
            return None

        self.bfd_session_stats_mo[key] = managed_objects['imdata'][0]['bfdSessStats']['attributes']

        self.log.apic_mo(
            'bfdSessStats.%s' % (key),
            self.bfd_session_stats_mo[key]
        )

        self.set_object_cache(
            'bfdSessStats',
            self.bfd_session_stats_mo[key],
            object_selector=key
        )

        return self.bfd_session_stats_mo[key]
