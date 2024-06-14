from lib import filter_helper


class ProtocolCdpNeighborInfo():
    def __init__(self):
        self.cdp_neighbors = {}

    def get_protocol_cdp_neighbor_info(self, managed_object):
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

        # topology/pod-1/node-201/sys/cdp/inst/if-[mgmt0]/adj-1
        info['interfaceId'] = info['dn'].split('if-')[1].split(']')[0][1:]
        info['__Output']['interfaceId'] = 'Yellow'

        if info['nativeVlan'] == 'unspecified':
            info['nativeVlan'] = ''

        return info

    def get_protocol_cdp_neighbors_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.cdp_neighbors:
            return self.cdp_neighbors[key]

        cdp_neighbors_mo = self.get_protocol_cdp_neighbors_mo(pod_id, node_id)
        if cdp_neighbors_mo is not None:
            self.cdp_neighbors[key] = []
            for cdp_neighbor_mo in cdp_neighbors_mo:
                self.cdp_neighbors[key].append(
                    self.get_protocol_cdp_neighbor_info(
                        cdp_neighbor_mo
                    )
                )

        self.log.apic_mo(
            'cdpAdjEp.info.%s' % (key),
            self.cdp_neighbors[key]
        )

        return self.cdp_neighbors[key]

    def match_protocol_cdp_neighbor(self, cdp_neighbor_info, cdp_neighbor_filter):
        if cdp_neighbor_filter is None or len(cdp_neighbor_filter) == 0:
            return True

        for ap_rule in cdp_neighbor_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'system':
                if not filter_helper.match_string(value, cdp_neighbor_info['sysName']):
                    return False

            if key == 'platform':
                if not filter_helper.match_string(value, cdp_neighbor_info['platId']):
                    return False

            if key == 'cap':
                if not filter_helper.match_string(value, cdp_neighbor_info['cap']):
                    return False

            if key == 'interface':
                if not filter_helper.match_string(value, cdp_neighbor_info['interfaceId']):
                    return False

        return True

    def get_protocol_cdp_neighbors(self, pod_id, node_id, cdp_neighbor_filter=None):
        all_cdp_neighbors = self.get_protocol_cdp_neighbors_info(pod_id, node_id)
        if all_cdp_neighbors is None:
            return None

        cdp_neighbors = []

        for cdp_neighbor_info in all_cdp_neighbors:
            if not self.match_protocol_cdp_neighbor(cdp_neighbor_info, cdp_neighbor_filter):
                continue

            cdp_neighbors.append(
                cdp_neighbor_info
            )

        cdp_neighbors = sorted(
            cdp_neighbors,
            key=lambda i: i['sysName']
        )

        return cdp_neighbors
