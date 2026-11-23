import copy

from lib import filter_helper
from lib.aci.proto.cdp.interface.stats.main import ProtocolCdpInterfaceStats


class ProtocolCdpInterfaceInfo(ProtocolCdpInterfaceStats):
    def __init__(self):
        ProtocolCdpInterfaceStats.__init__(self)
        self.cdp_interfaces = {}

    def get_cdp_active_interface_count(self, interfaces):
        count = 0
        for interface in interfaces:
            if 'neighborCount' in interface and interface['neighborCount'] > 0:
                count = count + 1
        return count

    def add_protocol_cdp_interface_neighbor_info(self, interfaces, neighbors, remove_no_neighbors=False):
        for interface in interfaces:
            interface['neighborCount'] = 0
            interface_neighbors = []

            for neighbor in neighbors:
                if neighbor['interfaceId'] == interface['id']:
                    interface['neighborCount'] = interface['neighborCount'] + 1
                    interface_neighbors.append(
                        neighbor['sysName']
                    )

            interface['neighborList'] = ', '.join(interface_neighbors)

        if remove_no_neighbors:
            new_interfaces = []
            for interface in interfaces:
                if interface['neighborCount'] > 0:
                    new_interfaces.append(
                        interface
                    )

            interfaces = copy.deepcopy(new_interfaces)

        return interfaces

    def get_protocol_cdp_interface_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            if key == 'stats':
                info['stats'] = self.get_protocol_cdp_interface_stats_info(managed_object[key])
                info['stats'] = self.my_output.merge_output(
                    info['stats']
                )
            else:
                info[key] = managed_object[key]

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        info['__Output']['id'] = 'Yellow'

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
            info['operStQual'] = ''
        else:
            info['__Output']['operSt'] = 'Red'

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        return info

    def get_protocol_cdp_interfaces_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.cdp_interfaces:
            return self.cdp_interfaces[key]

        cdp_interfaces_mo = self.get_protocol_cdp_interfaces_mo(pod_id, node_id)
        if cdp_interfaces_mo is not None:
            self.cdp_interfaces[key] = []
            for cdp_interface_mo in cdp_interfaces_mo:
                self.cdp_interfaces[key].append(
                    self.get_protocol_cdp_interface_info(
                        cdp_interface_mo
                    )
                )

        self.log.apic_mo(
            'cdpIf.info.%s' % (key),
            self.cdp_interfaces[key]
        )

        return self.cdp_interfaces[key]

    def match_protocol_cdp_interface(self, cdp_interface_info, cdp_interface_filter):
        if cdp_interface_filter is None or len(cdp_interface_filter) == 0:
            return True

        for ap_rule in cdp_interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'interface':
                if not filter_helper.match_string(value, cdp_interface_info['id']):
                    return False

        return True

    def get_protocol_cdp_interfaces(self, pod_id, node_id, cdp_interface_filter=None):
        all_cdp_interfaces = self.get_protocol_cdp_interfaces_info(pod_id, node_id)
        if all_cdp_interfaces is None:
            return None

        cdp_interfaces = []

        for cdp_interface_info in all_cdp_interfaces:
            if not self.match_protocol_cdp_interface(cdp_interface_info, cdp_interface_filter):
                continue

            cdp_interfaces.append(
                cdp_interface_info
            )

        cdp_interfaces = sorted(
            cdp_interfaces,
            key=lambda i: i['id']
        )

        return cdp_interfaces
