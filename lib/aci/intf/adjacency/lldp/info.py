from lib import filter_helper
from lib import ip_helper


class InterfaceAdjacencyLldpInfo():
    def __init__(self):
        self.adjacency_lldp = {}

    def get_lldp_adjacency_endpoint_info(self, managed_object):
        keys = [
            'capability',
            'chassisIdT',
            'chassisIdV',
            'dn',
            'enCap',
            'id',
            'mgmtId',
            'mgmtIp',
            'mgmtPortMac',
            'portDesc',
            'portIdT',
            'portIdV',
            'portVlan',
            'stQual',
            'status',
            'sysDesc',
            'sysName',
            'ttl'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['portVlan'] == 'unspecified':
            info['portVlan'] = ''

        # topology/pod-1/node-201/sys/lldp/inst/if-[mgmt0]/adj-1
        info['apic'] = self.apic_name
        info['pod_id'] = info['dn'].split('/')[1]
        info['node_id'] = info['dn'].split('/')[2]
        info['interface_id'] = info['dn'].split('if-[')[1].split(']')[0]

        info['pod_node_name'] = '%s/%s' % (
            info['pod_id'],
            self.get_node_name(
                info['node_id'].split('-')[1]
            )
        )

        info['portId'] = ''
        if info['portIdT'] in ['local', 'if-name']:
            info['portId'] = info['portIdV']

        info['mac'] = ''
        if info['portIdT'] == 'mac':
            info['mac'] = info['portIdV']

        if info['portIdT'] != 'mac' and ip_helper.is_mac_address(info['chassisIdV']):
            info['mac'] = info['chassisIdV']

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        return info

    def match_lldp_adjacency_endpoint(self, endpoint_info, adjacency_filter):
        if adjacency_filter is None or len(adjacency_filter) == 0:
            return True

        mac_filtering = False
        mac_match = False
        for rule in adjacency_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            if key == 'mac':
                mac_filtering = True
                if ip_helper.is_mac_match(value, endpoint_info['mac']):
                    mac_match = True

        if mac_filtering and not mac_match:
            return False

        for ap_rule in adjacency_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'interface_id':
                if not filter_helper.match_string(value, endpoint_info['interface_id']):
                    return False

            if key == 'device':
                if not filter_helper.match_string(value, endpoint_info['sysName']):
                    return False

        return True

    def get_lldp_adjacency_endpoint(self, pod_id, node_id, adjacency_filter=None, allow_multiple=True):
        managed_objects = self.get_adjacency_lldp_mo(
            pod_id,
            node_id
        )
        if managed_objects is None:
            return None

        endpoints = []
        for managed_object in managed_objects:
            endpoint_info = self.get_lldp_adjacency_endpoint_info(
                managed_object
            )

            if not self.match_lldp_adjacency_endpoint(endpoint_info, adjacency_filter):
                continue

            endpoints.append(
                endpoint_info
            )

        if allow_multiple:
            return endpoints

        if len(endpoints) == 0:
            return None

        return endpoints[0]
