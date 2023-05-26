from lib import filter_helper


class InterfaceVirtualPortChannelInfo():
    def __init__(self):
        self.interfaces_vpc = {}

    def get_interface_virtual_port_channel_info(self, managed_object):
        keys = [
            'compatQual',
            'compatQualStr',
            'compatSt',
            'deadIntvl',
            'dn',
            'dualActiveSt',
            'id',
            'lacpRole',
            'localMAC',
            'localPrio',
            'operRole',
            'operSt',
            'orphanPortList',
            'peerIp',
            'peerMAC',
            'peerPrio',
            'peerSt',
            'peerStQual',
            'peerVersion',
            'rolePrio',
            'summOperRole',
            'sysMac',
            'sysPrio',
            'virtualIp',
            'vpcMAC',
            'vpcPrio'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # "topology/pod-1/node-201/sys/vpc/inst/dom-100"
        info['podId'] = info['dn'].split('/')[1].split('-')[1]
        info['nodeId'] = info['dn'].split('/')[2].split('-')[1]

        info['apic'] = self.apic_label
        info['pod_node_name'] = 'pod-%s/%s' % (
            info['podId'],
            self.get_node_name(
                info['nodeId']
            )
        )

        info['__Output']['id'] = 'Blue'

        if info['peerSt'] == 'up':
            info['__Output']['peerSt'] = 'Green'
            info['peerStQual'] = ''
            info['up'] = True
        else:
            info['__Output']['peerSt'] = 'Red'
            info['up'] = False

        if info['compatSt'] == 'pass':
            info['__Output']['compatSt'] = 'Green'
            info['compatQualStr'] = ''
        else:
            info['__Output']['compatSt'] = 'Red'

        return info

    def get_interfaces_virtual_port_channel_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interfaces_vpc:
            return self.interfaces_vpc[key]

        interfaces_vpc_mo = self.get_interfaces_virtual_port_channel_mo(pod_id, node_id)
        if interfaces_vpc_mo is None:
            return None

        self.interfaces_vpc[key] = []
        for interface_vpc_mo in interfaces_vpc_mo:
            self.interfaces_vpc[key].append(
                self.get_interface_virtual_port_channel_info(
                    interface_vpc_mo
                )
            )

        return self.interfaces_vpc[key]

    def match_interface_virtual_port_channel(self, interface_info, interface_filter):
        if interface_filter is None or len(interface_filter) == 0:
            return True

        for ap_rule in interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'id':
                if not filter_helper.match_string(value, interface_info['id']):
                    return False

            if key == 'state':
                if value != 'any':
                    if not filter_helper.match_string(value, interface_info['peerSt']):
                        return False

            if key == 'member':
                if 'memberSt' in interface_info:
                    if value != 'any':
                        if not filter_helper.match_string(value, interface_info['memberSt']):
                            return False

        return True

    def get_interface_virtual_port_channel(self, pod_id, node_id, interface_filter=None, members_info=False):
        all_interfaces = self.get_interfaces_virtual_port_channel_info(pod_id, node_id)
        if all_interfaces is None:
            return None

        interfaces = []

        for interface_info in all_interfaces:
            if not self.match_interface_virtual_port_channel(interface_info, interface_filter):
                continue

            if members_info:
                interface_info['members'] = self.get_interface_virtual_port_channel_members(
                    pod_id,
                    node_id,
                    interface_info['id']
                )
                interface_info = self.add_interface_virtual_port_channel_members_summary(
                    interface_info
                )

                if not self.match_interface_virtual_port_channel(interface_info, interface_filter):
                    continue

            interfaces.append(
                interface_info
            )

        interfaces = sorted(
            interfaces,
            key=lambda i: i['id']
        )

        return interfaces
