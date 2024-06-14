class ProtocolBfdSessionPeerApi():
    def __init__(self):
        self.bfd_session_peer_mo = {}

    def set_protocol_bfd_session_peer_mo(self, managed_object):
        # "dn": "topology/pod-1/node-2208/sys/bfd/inst/session-1090519051/peerv"

        stats_dn = managed_object['bfdPeerV']['attributes']['dn']
        pod_id = stats_dn.split('/')[1][4:]
        node_id = stats_dn.split('/')[2][5:]
        session_id = stats_dn.split('/')[6][8:]
        key = '%s.%s.%s' % (pod_id, node_id, session_id)

        self.bfd_session_peer_mo[key] = managed_object['bfdPeerV']['attributes']

        self.log.apic_mo(
            'bfdPeerV.%s' % (key),
            self.bfd_session_peer_mo[key]
        )

        self.set_object_cache(
            'bfdPeerV',
            self.bfd_session_peer_mo[key],
            object_selector=key
        )

    def get_protocol_bfd_session_peer_mo(self, pod_id, node_id, session_id):
        key = '%s.%s.%s' % (pod_id, node_id, session_id)
        if key in self.bfd_session_peer_mo:
            return self.bfd_session_peer_mo[key]

        cache = self.get_object_cache(
            'bfdPeerV',
            object_selector=key
        )
        if cache is not None:
            self.bfd_session_peer_mo[key] = cache
            self.log.apic_mo(
                'bfdPeerV.%s' % (key),
                self.bfd_session_peer_mo[key]
            )
            return self.bfd_session_peer_mo[key]

        # url: https://<apic>/api/node/mo/topology/pod-1/node-201/sys/bfd/inst/session-1090519172.json?query-target=children&target-subtree-class=bfdPeerV&subscription=yes
        distinguished_name = 'topology/pod-%s/node-%s/sys/bfd/inst/session-%s' % (pod_id, node_id, session_id)
        query = 'query-target=children&target-subtree-class=bfdPeerV'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_bfd_session_peer_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_protocol_bfd_session_peer_mo',
                'Unexpected objects count'
            )
            return None

        self.bfd_session_peer_mo[key] = managed_objects['imdata'][0]['bfdPeerV']['attributes']

        self.log.apic_mo(
            'bfdPeerV.%s' % (key),
            self.bfd_session_peer_mo[key]
        )

        self.set_object_cache(
            'bfdPeerV',
            self.bfd_session_peer_mo[key],
            object_selector=key
        )

        return self.bfd_session_peer_mo[key]
