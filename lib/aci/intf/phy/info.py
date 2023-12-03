import json

from lib import filter_helper
from lib import ip_helper


class InterfacePhyInfo():
    def __init__(self):
        self.interface_phy = {}

    def get_interfaces_phy_summary(self, pod_id, node_id):
        interfaces = self.get_interfaces_phy(
            pod_id,
            node_id
        )

        if interfaces is None:
            return None

        summary = {}
        summary['__Output'] = {}
        summary['uplinkUp'] = 0
        summary['uplinkDown'] = 0
        summary['uplinkCount'] = 0
        summary['downlinkUp'] = 0
        summary['downlinkDown'] = 0
        summary['downlinkCount'] = 0
        summary['portUp'] = 0
        summary['portDown'] = 0
        summary['portCount'] = 0

        speeds = [
            '100M',
            '1G',
            '10G',
            '25G',
            '40G',
            '100G',
            '400G'
        ]
        for speed in speeds:
            summary['%sUp' % (speed)] = 0
            summary['%sDown' % (speed)] = 0

        for interface in interfaces:
            if interface['up']:
                if interface['uplink']:
                    summary['uplinkUp'] = summary['uplinkUp'] + 1
                if interface['downlink']:
                    summary['downlinkUp'] = summary['downlinkUp'] + 1
                if interface['stats'] is not None:
                    if interface['stats']['operSpeed'] in speeds:
                        summary['%sUp' % (interface['stats']['operSpeed'])] = summary['%sUp' % (interface['stats']['operSpeed'])] + 1

            if not interface['up']:
                if interface['uplink']:
                    summary['uplinkDown'] = summary['uplinkDown'] + 1
                if interface['downlink']:
                    summary['downlinkDown'] = summary['downlinkDown'] + 1
                if interface['stats'] is not None:
                    if interface['stats']['operSpeed'] in speeds:
                        summary['%sDown' % (interface['stats']['operSpeed'])] = summary['%sDown' % (interface['stats']['operSpeed'])] + 1

        summary['uplinkCount'] = summary['uplinkUp'] + summary['uplinkDown']
        summary['downlinkCount'] = summary['downlinkUp'] + summary['downlinkDown']
        summary['portUp'] = summary['uplinkUp'] + summary['downlinkUp']
        summary['portDown'] = summary['uplinkDown'] + summary['downlinkDown']
        summary['portCount'] = summary['portUp'] + summary['portDown']

        for speed in speeds:
            summary['%sCount' % (speed)] = summary['%sUp' % (speed)] + summary['%sDown' % (speed)]

        (summary['uplinkSummary'], summary['__Output']['uplinkSummary']) = self.get_interface_summary_output(
            summary['uplinkUp'],
            summary['uplinkDown'],
            summary['uplinkCount']
        )

        (summary['downlinkSummary'], summary['__Output']['downlinkSummary']) = self.get_interface_summary_output(
            summary['downlinkUp'],
            summary['downlinkDown'],
            summary['downlinkCount']
        )

        (summary['portSummary'], summary['__Output']['portSummary']) = self.get_interface_summary_output(
            summary['portUp'],
            summary['portDown'],
            summary['portCount']
        )

        for speed in speeds:
            (summary['%sSummary' % (speed)], summary['__Output']['%sSummary' % (speed)]) = self.get_interface_summary_output(
                summary['%sUp' % (speed)],
                summary['%sDown' % (speed)],
                summary['%sCount' % (speed)]
            )

        return summary

    def get_port_count(self, pod_id, node_id):
        ports = self.get_ports(
            pod_id,
            node_id
        )

        if ports is None:
            return 0

        return len(ports)

    def get_interface_phy_info(self, managed_object):
        keys = [
            'adminSt',
            'autoNeg',
            'bw',
            'delay',
            'descr',
            'dfeDelayMs',
            'dn',
            'dot1qEtherType',
            'fecMode',
            'id',
            'layer',
            'linkDebounce',
            'mdix',
            'medium',
            'mode',
            'mtu',
            'name',
            'portPhyMediaType',
            'portT',
            'routerMac',
            'spanMode',
            'speed',
            'switchingSt',
            'usage'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # Dn format
        # [0]: topology/pod-{id}/node-{id}/sys/phys-[{id}]
        # [1]: sys/phys-[{id}]

        info['portId'] = int(info['id'].split('/')[1])
        info['portName'] = info['id'][3:]
        info['podId'] = info['dn'].split('/')[1][4:]
        info['nodeId'] = info['dn'].split('/')[2][5:]
        info['nodeName'] = self.get_node_name(info['nodeId'])

        info['apic'] = self.apic_name
        info['pod_node_name'] = 'pod-%s/%s' % (
            info['podId'],
            self.get_node_name(
                info['nodeId']
            )
        )

        info['uplink'] = False
        info['downlink'] = False

        if info['portT'] == 'leaf':
            info['uplink'] = False
            info['downlink'] = True

        if info['portT'] == 'fab':
            info['uplink'] = True
            info['downlink'] = False

        info['layerT'] = ''
        if info['layer'] == 'Layer2':
            info['layerT'] = 'switched'
        if info['layer'] == 'Layer3':
            info['layerT'] = 'routed'

        info['__Output']['id'] = 'Blue'
        if info['adminSt'] == 'up':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['switchingSt'] == 'enabled':
            info['__Output']['switchingSt'] = 'Green'
        else:
            info['__Output']['switchingSt'] = 'Red'

        interfaces_stats = self.get_interface_phy_ether_stats(
            info['podId'],
            info['nodeId'],
            interface_filter=['dn:%s' % (info['dn'])]
        )
        if len(interfaces_stats) == 0:
            info['stats'] = None
        if len(interfaces_stats) == 1:
            info['stats'] = interfaces_stats[0]
        if len(interfaces_stats) > 1:
            self.log.error(
                'get_interface_phy_info',
                'Unexpected ether stats object count: %s' % (info['dn'])
            )
            self.log.error(
                'get_interface_phy_info',
                json.dumps(interfaces_stats, indent=4)
            )

        info['up'] = False
        if info['stats'] is not None:
            if info['adminSt'] == 'up' and info['switchingSt'] == 'enabled' and info['stats']['operSt'] == 'up':
                info['up'] = True

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        info = self.my_output.merge_output(info)

        return info

    def get_interfaces_phy_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_phy:
            return self.interface_phy[key]

        interfaces_mo = self.get_interface_phy_mo(pod_id, node_id)
        if interfaces_mo is None:
            return None

        self.interface_phy[key] = []
        for interface_mo in interfaces_mo:
            self.interface_phy[key].append(
                self.get_interface_phy_info(
                    interface_mo
                )
            )

        self.log.apic_mo(
            'l1PhysIf.info.%s' % (key),
            self.interface_phy[key]
        )

        return self.interface_phy[key]

    def match_interface_phy_epg_stats(self, epg_stats_info, interface_filter):
        if interface_filter is None or len(interface_filter) == 0:
            return True

        for ap_rule in interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'epg':
                if not filter_helper.match_string(value, epg_stats_info['vlan']['epgDn']):
                    return False

            if key == 'vlan':
                if not filter_helper.match_id(epg_stats_info['vlan']['id'], value):
                    return False

            if key == 'evlan':
                if not filter_helper.match_id(epg_stats_info['vlan']['evlan'], value):
                    return False

            if key == 'fvxlan':
                if not filter_helper.match_id(epg_stats_info['vlan']['fvxlan'], value):
                    return False

        return True

    def filter_interface_phy_epg_stats(self, epgs_stats_info, interface_filter):
        filtered = []

        for epg_stats_info in epgs_stats_info:
            if self.match_interface_phy_epg_stats(epg_stats_info, interface_filter):
                filtered.append(
                    epg_stats_info
                )

        return filtered

    def match_interface_phy(self, interface_info, interface_filter):
        if interface_filter is None or len(interface_filter) == 0:
            return True

        for ap_rule in interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'ctx':
                found = False
                for context in value.split(','):
                    (pod_id, node_id, interface_id) = context.split(':')
                    if filter_helper.match_string(pod_id, 'pod-%s' % (interface_info['podId'])):
                        if filter_helper.match_string(node_id, 'node-%s' % (interface_info['nodeId'])):
                            if filter_helper.match_string(interface_id, interface_info['id']):
                                found = True
                                break

                if not found:
                    return False

            if key == 'id':
                if not filter_helper.match_string(value, interface_info['id']):
                    return False

            if key == 'ids':
                found = False
                for interface_id in value.split(','):
                    if filter_helper.match_string(interface_id, interface_info['id']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'dn':
                if not filter_helper.match_string(value, interface_info['dn']):
                    return False

            if key == 'switching':
                if not filter_helper.match_string(value, interface_info['switchingSt']):
                    return False

            if key == 'oper':
                if interface_info['stats'] is None:
                    return False

                if not filter_helper.match_string(value, interface_info['stats']['operSt']):
                    return False

            if key == 'type':
                if not filter_helper.match_string(value, interface_info['portT']):
                    return False

            if key == 'layer':
                if not filter_helper.match_string(value, interface_info['layerT']):
                    return False

            if key == 'mac':
                if interface_info['stats'] is None:
                    return False

                if not ip_helper.is_mac_match(value, interface_info['stats']['backplaneMac']):
                    return False

            if key == 'speed':
                if interface_info['stats'] is None:
                    return False

                if not filter_helper.match_string(value, interface_info['stats']['operSpeed']):
                    return False

            if key == 'fec':
                if interface_info['stats'] is None:
                    return False

                if not filter_helper.match_string(value, interface_info['stats']['operFecMode']):
                    return False

            if key == 'trans':
                if 'fc_stats' in interface_info:
                    if interface_info['fc_stats'] is None:
                        return False

                    if not filter_helper.match_string(value, interface_info['fc_stats']['guiCiscoPID']):
                        return False

            if key == 'optics':
                if 'fc_stats' in interface_info:
                    if interface_info['fc_stats'] is None:
                        return False

                    if not filter_helper.match_string(value, interface_info['fc_stats']['type']):
                        return False

            if key == 'pc':
                if interface_info['stats'] is None:
                    return False

                if value == 'enabled' and len(interface_info['stats']['bundleIndex']) == 0:
                    return False

                if value == 'enabled' and len(interface_info['stats']['bundleIndex']) > 0:
                    return False

            if key == 'epg':
                if 'epg_stats' in interface_info:
                    if interface_info['epg_stats'] is None:
                        return False

                    found = False
                    for epg_stats in interface_info['epg_stats']:
                        if epg_stats['vlan'] is not None:
                            if filter_helper.match_string(value, epg_stats['vlan']['epgDn']):
                                found = True
                                break

                    if not found:
                        return False

            if key == 'vlan':
                if 'epg_stats' in interface_info:
                    if interface_info['epg_stats'] is None:
                        return False

                    found = False
                    for epg_stats in interface_info['epg_stats']:
                        if epg_stats['vlan'] is not None:
                            if filter_helper.match_id(epg_stats['vlan']['id'], value):
                                found = True
                                break

                    if not found:
                        return False

            if key == 'evlan':
                if 'epg_stats' in interface_info:
                    if interface_info['epg_stats'] is None:
                        return False

                    found = False
                    for epg_stats in interface_info['epg_stats']:
                        if epg_stats['vlan'] is not None:
                            if filter_helper.match_id(epg_stats['vlan']['evlan'], value):
                                found = True
                                break

                    if not found:
                        return False

            if key == 'fvxlan':
                if 'epg_stats' in interface_info:
                    if interface_info['epg_stats'] is None:
                        return False

                    found = False
                    for epg_stats in interface_info['epg_stats']:
                        if epg_stats['vlan'] is not None:
                            if filter_helper.match_id(epg_stats['vlan']['fvxlan'], value):
                                found = True
                                break

                    if not found:
                        return False

            if key == 'nei':
                if 'cdp' in interface_info and 'lldp' in interface_info:
                    found = False

                    if interface_info['cdp'] is not None:
                        for cdp_info in interface_info['cdp']:
                            if filter_helper.match_string(value, cdp_info['sysName']):
                                found = True
                                break

                    if interface_info['lldp'] is not None:
                        for lldp_info in interface_info['lldp']:
                            if filter_helper.match_string(value, lldp_info['sysName']):
                                found = True
                                break

                    if not found:
                        return False

            if key == 'fault':
                if value == 'any':
                    if not interface_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_interface_phy',
                        'Unsupported fault filtering value: %s' % (value)
                    )

        return True

    def get_interfaces_phy(
            self,
            pod_id,
            node_id,
            interface_filter=None,
            ether_stats_info=False,
            fc_stats_info=False,
            epg_stats_info=False,
            load_info=False,
            eee_info=False,
            cdp_info=False,
            lldp_info=False,
            policy_info=False,
            qos_info=False,
            qos_references=None,
            cap_info=False,
            pc_info=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_interfaces = self.get_interfaces_phy_info(pod_id, node_id)
        if all_interfaces is None:
            return None

        interfaces = []

        for interface_info in all_interfaces:
            if not self.match_interface_phy(interface_info, interface_filter):
                continue

            if epg_stats_info:
                interface_info['epg_stats'] = None
                if interface_info['stats'] is not None:
                    interface_info['epg_stats'] = self.get_interface_phy_epg_stats(
                        interface_info['podId'],
                        interface_info['nodeId'],
                        interface_info['id'],
                        vlan_info=True,
                        vlans=interface_info['stats']['allowedVlans']
                    )

                if not self.match_interface_phy(interface_info, interface_filter):
                    continue

                if interface_info['epg_stats'] is not None:
                    interface_info['epg_stats'] = self.my_output.merge_output(
                        self.filter_interface_phy_epg_stats(
                            interface_info['epg_stats'],
                            interface_filter
                        )
                    )

            if ether_stats_info:
                interface_info['ether_stats'] = self.get_interface_phy_rmon_stats(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    interface_info['id']
                )

            if fc_stats_info:
                interface_info['fc_stats'] = None
                interface_fc_stats = self.get_interface_phy_fc_stats(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    interface_filter=['dn:%s' % (interface_info['dn'])]
                )
                if interface_fc_stats is not None:
                    if len(interface_fc_stats) != 1:
                        self.log.error(
                            'get_interfaces_phy',
                            'Unexpected fc stats count (%s): %s' % (
                                len(interface_fc_stats),
                                interface_info['dn']
                            )
                        )
                    else:
                        interface_info['fc_stats'] = interface_fc_stats[0]

                if not self.match_interface_phy(interface_info, interface_filter):
                    continue

            if load_info:
                interface_info['load'] = self.get_interface_phy_load_stats(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    interface_info['id']
                )

            if eee_info:
                interface_info['eee'] = self.get_interface_phy_eee_stats(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    interface_info['id']
                )

            if cdp_info:
                interface_info['cdp'] = self.get_cdp_adjacency_endpoint(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    interface_info['id'],
                    allow_multiple=True
                )

            if lldp_info:
                interface_info['lldp'] = self.get_lldp_adjacency_endpoint(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    adjacency_filter=['interface_id:%s' % (interface_info['id'])],
                    allow_multiple=True
                )

            if cdp_info or lldp_info:
                if not self.match_interface_phy(interface_info, interface_filter):
                    continue

            if policy_info:
                interface_info['policy_selector'] = self.get_interface_policy_group_selector(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    interface_info['portName'],
                    group_info=True
                )

            if qos_info:
                qos_filter = ['interface_id:%s' % (interface_info['id'])]
                if interface_filter is not None:
                    for value in interface_filter:
                        if value.startswith('qos:'):
                            qos_filter.append(value)

                interface_info['qos'] = self.get_interfaces_phy_qos_stats(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    qos_filter=qos_filter,
                    qos_references=qos_references
                )

                if len(interface_info['qos']) == 0:
                    continue

            if cap_info:
                interface_info['load'] = self.get_interface_phy_cap_stats(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    interface_info['id']
                )

            if pc_info:
                interface_info['pc'] = self.get_interface_phy_pc_stats(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    interface_info['id']
                )

            if fault_info:
                interface_info['faultInst'] = self.get_interface_phy_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultInst'
                )

            if hfault_info:
                interface_info['faultRecord'] = self.get_interface_phy_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                interface_info['eventLog'] = self.get_interface_phy_id_event(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    event_filter=event_filter
                )

            if audit_info:
                interface_info['auditLog'] = self.get_interface_phy_id_audit(
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
            key=lambda i: i['portId']
        )

        return interfaces

    def get_interface_phy(
            self,
            pod_id,
            node_id,
            interface_id,
            ether_stats_info=False,
            fc_stats_info=False,
            epg_stats_info=False,
            load_info=False,
            eee_info=False,
            cdp_info=False,
            lldp_info=False,
            policy_info=False,
            qos_info=False,
            qos_references=None,
            cap_info=False,
            pc_info=False
            ):
        interfaces = self.get_interfaces_phy(
            pod_id,
            node_id,
            interface_filter=['id:%s' % (interface_id)],
            ether_stats_info=ether_stats_info,
            fc_stats_info=fc_stats_info,
            epg_stats_info=epg_stats_info,
            load_info=load_info,
            eee_info=eee_info,
            cdp_info=cdp_info,
            lldp_info=lldp_info,
            policy_info=policy_info,
            qos_info=qos_info,
            qos_references=qos_references,
            cap_info=cap_info,
            pc_info=pc_info
        )

        if interfaces is None or len(interfaces) != 1:
            return None

        return interfaces[0]
