from lib import filter_helper


class InterfaceVirtualPortChannelInfo():
    def __init__(self):
        self.interfaces_vpc = {}

    def get_interface_virtual_port_channel_summary(self, pod_id, node_id):
        ports = self.get_interface_virtual_port_channel(
            pod_id,
            node_id
        )

        if ports is None:
            return None

        summary = {}
        summary['__Output'] = {}
        summary['portUp'] = 0
        summary['portDown'] = 0
        summary['portCount'] = 0

        for port in ports:
            summary['portUp'] = summary['portUp'] + port['localMemberUp']
            summary['portDown'] = summary['portDown'] + port['localMemberDown']

        summary['portCount'] = summary['portUp'] + summary['portDown']

        (summary['portSummary'], summary['__Output']['portSummary']) = self.get_interface_summary_output(
            summary['portUp'],
            summary['portDown'],
            summary['portCount']
        )

        return summary

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

        info['apic'] = self.apic_name
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

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        info['member'] = []
        for vpc_interface_mo in managed_object['vpcIf']:
            member_info = self.get_interface_virtual_port_channel_member_info(
                vpc_interface_mo
            )
            member_info['pod_node_name'] = info['pod_node_name']
            member_info['domainId'] = info['id']

            info['member'].append(
                member_info
            )

        info = self.add_interface_virtual_port_channel_members_summary(
            info
        )

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

        self.log.apic_mo(
            'vpcDom.info.%s' % (key),
            self.interfaces_vpc[key]
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

    def get_interface_virtual_port_channel(
            self,
            pod_id,
            node_id,
            interface_filter=None,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_interfaces = self.get_interfaces_virtual_port_channel_info(pod_id, node_id)
        if all_interfaces is None:
            return None

        interfaces = []

        for interface_info in all_interfaces:
            if not self.match_interface_virtual_port_channel(interface_info, interface_filter):
                continue

            for member_info in interface_info['member']:
                member_info['pc'] = self.get_interface_port_channel(
                    pod_id,
                    node_id,
                    interface_port_channel_filter=['name:%s' % (member_info['name'])]
                )

                member_info['vlan'] = []
                if len(member_info['cfgdTrunkVlans']) > 0:
                    member_info['vlan'] = self.get_vlan_stats(
                        pod_id,
                        node_id,
                        vlan_filter=['evlans:%s' % (member_info['cfgdTrunkVlans'])]
                    )

            if fault_info:
                interface_info['faultInst'] = self.get_interface_virtual_port_channel_domain_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultInst'
                )

            if hfault_info:
                interface_info['faultRecord'] = self.get_interface_virtual_port_channel_domain_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                interface_info['eventLog'] = self.get_interface_virtual_port_channel_domain_id_event(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    event_filter=event_filter
                )

            if audit_info:
                interface_info['auditLog'] = self.get_interface_virtual_port_channel_id_audit(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    audit_filter=audit_filter
                )

            interfaces.append(
                interface_info
            )

        interfaces = sorted(
            interfaces,
            key=lambda i: i['id']
        )

        return interfaces
