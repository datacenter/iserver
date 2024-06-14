class ProtocolBfdSessionApi():
    def __init__(self):
        self.bfd_sessions_mo = {}

    def get_protocol_bfd_sessions_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bfd_sessions_mo:
            return self.bfd_sessions_mo[key]

        cache = self.get_object_cache(
            'bfdSess',
            object_selector=key
        )
        if cache is not None:
            self.bfd_sessions_mo[key] = cache
            self.log.apic_mo(
                'bfdSess.%s' % (key),
                self.bfd_sessions_mo[key]
            )
            return self.bfd_sessions_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/bfd/inst' % (pod_id, node_id)
        query = 'query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_bfd_sessions_mo',
                'API failed'
            )
            return None

        self.bfd_sessions_mo[key] = []
        for managed_object in managed_objects['imdata']:
            if 'bfdSess' in managed_object:
                attributes = managed_object['bfdSess']['attributes']
                attributes['healthInst'] = self.get_mo_child_attributes(
                    'bfdSess',
                    managed_object,
                    'healthInst'
                )
                attributes['faultCounts'] = self.get_mo_child_attributes(
                    'bfdSess',
                    managed_object,
                    'faultCounts'
                )
                self.bfd_sessions_mo[key].append(
                    attributes
                )

            if 'bfdSessStats' in managed_object:
                self.set_protocol_bfd_session_stats_mo(
                    managed_object
                )

            if 'bfdPeerV' in managed_object:
                self.set_protocol_bfd_session_peer_mo(
                    managed_object
                )

            if 'bfdIf' in managed_object:
                self.set_protocol_bfd_interface_mo(
                    managed_object
                )

        self.set_protocol_bfd_interface_log(
            key
        )

        self.log.apic_mo(
            'bfdSess.%s' % (key),
            self.bfd_sessions_mo[key]
        )

        self.set_object_cache(
            'bfdSess',
            self.bfd_sessions_mo[key],
            object_selector=key
        )

        return self.bfd_sessions_mo[key]
