from lib import filter_helper
from lib import ip_helper


class ProtocolBgpNeighborInfo():
    def __init__(self):
        self.bgp_neighbors = {}

    def get_protocol_bgp_neighbor_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        # "dn": "topology/pod-1/node-201/sys/bgp/inst/dom-common:smi5Gc-cvim4-N6_VRF/peer-[<ip>/28]"
        info['bgpDomainName'] = info['dn'].split('/')[6][4:]

        info['__Output']['name'] = 'Yellow'
        info['__Output']['bgpDomainName'] = 'Yellow'
        info['__Output']['state.addr'] = 'Yellow'
        info['__Output']['asn'] = 'Blue'

        if info['ctrl'] == 'bfd':
            info['bfdTick'] = '\u2713'
        else:
            info['bfdTick'] = '\u2717'

        if info['state']['connAttempts'] == 'na':
            info['state']['connAttempts'] = 0

        info['state']['connSummary'] = '%s/%s/%s' % (
            info['state']['connAttempts'],
            info['state']['connDrop'],
            info['state']['connEst']
        )
        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['state']['operSt'] == 'established':
            info['__Output']['state.operSt'] = 'Green'
        else:
            info['__Output']['state.operSt'] = 'Red'

        if info['curPfxPeers'] != '0':
            info['__Output']['curPfxPeers'] = 'Blue'

        if info['state']['connDrop'] != '0':
            info['__Output']['state.connDrop'] = 'Red'

        if 'af-ipv4-ucast' in info['state']:
            if info['state']['af-ipv4-ucast']['acceptedPaths'] != '0':
                info['__Output']['state.af-ipv4-ucast.acceptedPaths'] = 'Blue'

        info['paths'] = []

        if 'af-ipv4-ucast' in info['state']:
            if info['state']['af-ipv4-ucast']['acceptedPaths'] != '0':
                info['paths'].append(
                    'IPv4-ucast:%s' % (
                        info['state']['af-ipv4-ucast']['acceptedPaths']
                    )
                )

        if 'af-ipv6-ucast' in info['state']:
            if info['state']['af-ipv6-ucast']['acceptedPaths'] != '0':
                info['paths'].append(
                    'IPv6-ucast:%s' % (
                        info['state']['af-ipv6-ucast']['acceptedPaths']
                    )
                )

        if 'af-vpnv4-ucast' in info['state']:
            if info['state']['af-vpnv4-ucast']['acceptedPaths'] != '0':
                info['paths'].append(
                    'VPNv4-ucast:%s' % (
                        info['state']['af-vpnv4-ucast']['acceptedPaths']
                    )
                )

        if 'af-vpnv6-ucast' in info['state']:
            if info['state']['af-vpnv6-ucast']['acceptedPaths'] != '0':
                info['paths'].append(
                    'VPNv6-ucast:%s' % (
                        info['state']['af-vpnv6-ucast']['acceptedPaths']
                    )
                )

        return info

    def get_protocol_bgp_neighbors_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bgp_neighbors:
            return self.bgp_neighbors[key]

        bgp_neighbors_mo = self.get_protocol_bgp_neighbors_mo(pod_id, node_id)
        if bgp_neighbors_mo is not None:
            self.bgp_neighbors[key] = []
            for bgp_neighbor_mo in bgp_neighbors_mo:
                self.bgp_neighbors[key].append(
                    self.get_protocol_bgp_neighbor_info(
                        bgp_neighbor_mo
                    )
                )

        self.log.apic_mo(
            'bgp.neighbors.info.%s' % (key),
            self.bgp_neighbors[key]
        )

        return self.bgp_neighbors[key]

    def match_protocol_bgp_neighbor(self, bgp_neighbor_info, bgp_neighbor_filter):
        if bgp_neighbor_filter is None or len(bgp_neighbor_filter) == 0:
            return True

        for ap_rule in bgp_neighbor_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])
            if key == 'asn':
                if not filter_helper.match_string(value, bgp_neighbor_info['asn']):
                    return False

            if key == 'vrf':
                if not filter_helper.match_string(value, bgp_neighbor_info['bgpDomainName']):
                    return False

            if key == 'rtr-ip':
                if not filter_helper.match_string(value, bgp_neighbor_info['state']['rtrId']):
                    return False

            if key == 'rtr-subnet':
                if not ip_helper.is_ipv4_in_cidr(bgp_neighbor_info['state']['rtrId'], value):
                    return False

            if key == 'nbr-ip':
                if not filter_helper.match_string(value, bgp_neighbor_info['state']['addr']):
                    return False

            if key == 'nbr-subnet':
                if not ip_helper.is_ipv4_in_cidr(bgp_neighbor_info['state']['addr'], value):
                    return False

            if key == 'state':
                if value != 'any':
                    if value == 'up':
                        if not filter_helper.match_string('established', bgp_neighbor_info['state']['operSt']):
                            return False

                    if value == 'down':
                        if not filter_helper.match_string('idle', bgp_neighbor_info['state']['operSt']):
                            return False

            if key == 'type':
                if value != 'any':
                    if not filter_helper.match_string(value, bgp_neighbor_info['state']['type']):
                        return False

            if key == 'interface':
                if not filter_helper.match_string(value, bgp_neighbor_info['srcIf']):
                    return False

        return True

    def get_protocol_bgp_neighbors(
            self,
            pod_id,
            node_id,
            bgp_neighbor_filter=None,
            stats_info=False,
            prefix_info=False
            ):
        all_bgp_neighbors = self.get_protocol_bgp_neighbors_info(pod_id, node_id)
        if all_bgp_neighbors is None:
            return None

        bgp_neighbors = []

        for bgp_neighbor_info in all_bgp_neighbors:
            if not self.match_protocol_bgp_neighbor(bgp_neighbor_info, bgp_neighbor_filter):
                continue

            if stats_info:
                bgp_neighbor_info['stats'] = self.get_protocol_bgp_neighbor_stats(
                    pod_id,
                    node_id,
                    bgp_neighbor_info['bgpDomainName'],
                    bgp_neighbor_info['addr'],
                    bgp_neighbor_info['state']['addr']
                )

                if prefix_info:
                    bgp_neighbor_info['route'] = self.get_protocol_ipv4_routes(
                        pod_id,
                        node_id,
                        bgp_neighbor_info['bgpDomainName'],
                        route_filter=['bgp', 'nh:%s' % (bgp_neighbor_info['state']['addr'])]
                    )

            bgp_neighbors.append(
                bgp_neighbor_info
            )

        bgp_neighbors = sorted(
            bgp_neighbors,
            key=lambda i: (
                i['bgpDomainName'].lower(),
                i['addr']
            )
        )

        return bgp_neighbors
