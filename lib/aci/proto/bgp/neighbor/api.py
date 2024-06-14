import copy


class ProtocolBgpNeighborApi():
    def __init__(self):
        self.bgp_neighbors_mo = {}

    def get_protocol_bgp_neighbors_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bgp_neighbors_mo:
            return self.bgp_neighbors_mo[key]

        cache = self.get_object_cache(
            'bgpPeer',
            object_selector=key
        )
        if cache is not None:
            self.bgp_neighbors_mo[key] = cache
            self.log.apic_mo(
                'bgpPeer.%s' % (key),
                self.bgp_neighbors_mo[key]
            )
            return self.bgp_neighbors_mo[key]

        class_name = 'topology/pod-%s/node-%s/bgpDom' % (pod_id, node_id)
        query = 'query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_bgp_neighbors_mo',
                'API failed'
            )
            return None

        bgp_peers = []
        for managed_object in managed_objects['imdata']:
            if 'bgpPeer' in managed_object:
                bgp_peer_attributes = managed_object['bgpPeer']['attributes']
                bgp_peer_attributes['state'] = []
                bgp_peers.append(
                    bgp_peer_attributes
                )

        for managed_object in managed_objects['imdata']:
            if 'bgpPeerEntry' in managed_object:
                entry_bgp_domain = managed_object['bgpPeerEntry']['attributes']['dn'].split('/')[6]
                entry_bgp_peer_dn = managed_object['bgpPeerEntry']['attributes']['dn'].split('/')[7]
                for bgp_peer in bgp_peers:
                    if entry_bgp_domain in bgp_peer['dn'] and entry_bgp_peer_dn in bgp_peer['dn']:
                        bgp_peer['state'].append(
                            managed_object['bgpPeerEntry']['attributes']
                        )

        for managed_object in managed_objects['imdata']:
            if 'bgpPeerAfEntry' in managed_object:
                # "topology/pod-1/node-201/sys/bgp/inst/dom-overlay-1/peer-[<ip>/32]/ent-[<ip>]/af-vpnv4-ucast"
                af_bgp_peer_dn = managed_object['bgpPeerAfEntry']['attributes']['dn'].split('/')[7]
                af_bgp_entry_dn = managed_object['bgpPeerAfEntry']['attributes']['dn'].split('/')[8]
                af_name = managed_object['bgpPeerAfEntry']['attributes']['dn'].split('/')[-1]
                for bgp_peer in bgp_peers:
                    if af_bgp_peer_dn in bgp_peer['dn']:
                        for state in bgp_peer['state']:
                            if af_bgp_entry_dn in state['dn']:
                                state[af_name] = managed_object['bgpPeerAfEntry']['attributes']

        class_name = 'bgpLocalAsnP'
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_bgp_neighbors_mo',
                'API bgpLocalAsnP failed'
            )

        if managed_objects is not None:
            self.log.apic_mo(
                'bgpLocalAsnP',
                managed_objects
            )

            for managed_object in managed_objects['imdata']:
                if 'bgpLocalAsnP' in managed_object:
                    # [0]: uni/controller/mdpPolCont/localDomP-{name}/provider-{name}/infraPeerP-[{addr}]/localasn
                    # [1]: uni/tn-{name}/out-{name}/lnodep-{name}/lifp-{name}/vlifp-[{nodeDn}]-[{encap}]/infraPeerP-[{addr}]/localasn
                    # [2]: uni/tn-{name}/out-{name}/lnodep-{name}/lifp-{name}/rspathL3OutAtt-[{tDn}]/infraPeerP-[{addr}]/localasn
                    # [3]: uni/tn-{name}/out-{name}/lnodep-{name}/infraPeerP-[{addr}]/localasn
                    # [4]: uni/tn-{name}/out-{name}/lnodep-{name}/lifp-{name}/vlifp-[{nodeDn}]-[{encap}]/peerP-[{addr}]/localasn
                    # [5]: uni/tn-{name}/out-{name}/lnodep-{name}/lifp-{name}/rspathL3OutAtt-[{tDn}]/peerP-[{addr}]/localasn
                    # [6]: uni/tn-{name}/out-{name}/lnodep-{name}/peerP-[{addr}]/localasn

                    dn_mo = managed_object['bgpLocalAsnP']['attributes']['dn']
                    if dn_mo.split('/')[5].split('-')[0] == 'vlifp':
                        # [1]: uni/tn-{name}/out-{name}/lnodep-{name}/lifp-{name}/vlifp-[{nodeDn}]-[{encap}]/infraPeerP-[{addr}]/localasn
                        # [4]: uni/tn-{name}/out-{name}/lnodep-{name}/lifp-{name}/vlifp-[{nodeDn}]-[{encap}]/peerP-[{addr}]/localasn
                        # uni/tn-k8s/out-vk8s_1/lnodep-node-205-206/lifp-floating_svi/vlifp-[topology/pod-1/node-205]-[vlan-500]/peerP-[<ip>/28]/localasn
                        l3out_name = dn_mo.split('/')[2][4:]
                        lnodep_name = dn_mo.split('/')[3][7:]
                        lifp_name = dn_mo.split('/')[4][5:]
                        peer_address = None
                        if len(dn_mo.split('/infraPeerP-[')) > 1:
                            peer_address = dn_mo.split('/infraPeerP-[')[1].split(']')[0]
                        if len(dn_mo.split('/peerP-[')) > 1:
                            peer_address = dn_mo.split('/peerP-[')[1].split(']')[0]

                        if peer_address is not None:
                            for bgp_peer in bgp_peers:
                                if bgp_peer['addr'] == peer_address:
                                    bgp_peer['l3out'] = l3out_name
                                    bgp_peer['lnodep'] = lnodep_name
                                    bgp_peer['lifp'] = lifp_name
                                    bgp_peer['localAsn'] = managed_object['bgpLocalAsnP']['attributes']['localAsn']
                                    bgp_peer['asnPropagate'] = managed_object['bgpLocalAsnP']['attributes']['asnPropagate']

        flat_bgp_peers = []
        for bgp_peer in bgp_peers:
            for state in bgp_peer['state']:
                new_entry = copy.deepcopy(bgp_peer)
                new_entry['state'] = copy.deepcopy(state)
                flat_bgp_peers.append(new_entry)

        self.bgp_neighbors_mo[key] = copy.deepcopy(flat_bgp_peers)

        self.log.apic_mo(
            'bgpPeer.%s' % (key),
            self.bgp_neighbors_mo[key]
        )

        self.set_object_cache(
            'bgpPeer',
            self.bgp_neighbors_mo[key],
            object_selector=key
        )

        return self.bgp_neighbors_mo[key]
