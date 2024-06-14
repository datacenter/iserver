class ProtocolBgpNeighborStatsApi():
    def __init__(self):
        self.bgp_nbr_stats_mo = {}

    def get_protocol_bgp_neighbor_stats_mo(self, pod_id, node_id, bgp_domain_name, bgp_peer_addr, bgp_state_addr):
        key = '%s.%s.%s.%s.%s' % (
            pod_id,
            node_id,
            bgp_domain_name,
            bgp_peer_addr,
            bgp_state_addr
        )
        if key in self.bgp_nbr_stats_mo:
            return self.bgp_nbr_stats_mo[key]

        cache = self.get_object_cache(
            'bgpPeerEntryStats',
            object_selector=key
        )
        if cache is not None:
            self.bgp_nbr_stats_mo[key] = cache
            self.log.apic_mo(
                'bgpPeerEntryStats.%s' % (key),
                self.bgp_nbr_stats_mo[key]
            )
            return self.bgp_nbr_stats_mo[key]

        # https://<apic>/api/node/mo/topology/pod-1/node-201/sys/bgp/inst/dom-common:smi5Gc-cvim4-N3-N4_VRF/peer-[<ip>/32]/ent-[<ip>]/peerstats.json
        distinguished_name = 'topology/pod-%s/node-%s/sys/bgp/inst/dom-%s/peer-[%s]/ent-[%s]/peerstats' % (
            pod_id,
            node_id,
            bgp_domain_name,
            bgp_peer_addr,
            bgp_state_addr
        )
        managed_objects = self.get_managed_object(
            distinguished_name
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_bgp_neighbor_stats_mo',
                'API failed'
            )
            return None

        if int(managed_objects['totalCount']) > 1:
            self.log.error(
                'get_protocol_bgp_neighbor_stats_mo',
                'Unexpected object count: %s' % (key)
            )
            return None

        if int(managed_objects['totalCount']) == 0:
            self.bgp_nbr_stats_mo[key] = {}
        else:
            self.bgp_nbr_stats_mo[key] = managed_objects['imdata'][0]['bgpPeerEntryStats']['attributes']

        self.log.apic_mo(
            'bgpPeerEntryStats.%s' % (key),
            self.bgp_nbr_stats_mo[key]
        )

        self.set_object_cache(
            'bgpPeerEntryStats',
            self.bgp_nbr_stats_mo[key],
            object_selector=key
        )

        return self.bgp_nbr_stats_mo[key]
