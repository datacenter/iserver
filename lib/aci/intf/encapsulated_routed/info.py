from lib import filter_helper


class InterfaceEncapsulatedRoutedInfo():
    def __init__(self):
        self.interface_encap_routed = {}

    def get_interface_encap_routed_summary(self, pod_id, node_id):
        ports = self.get_interfaces_encap_routed(
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
            if port['up']:
                summary['portUp'] = summary['portUp'] + 1

            if not port['up']:
                summary['portDown'] = summary['portDown'] + 1

        summary['portCount'] = summary['portUp'] + summary['portDown']

        (summary['portSummary'], summary['__Output']['portSummary']) = self.get_interface_summary_output(
            summary['portUp'],
            summary['portDown'],
            summary['portCount']
        )

        return summary

    def get_interface_encap_routed_count(self, pod_id, node_id):
        interfaces = self.get_interfaces_encap_routed(pod_id, node_id)
        return len(interfaces)

    def get_interface_encap_routed_info(self, managed_object):
        keys = [
            'MultiPodDirect',
            'adminSt',
            'delay',
            'dn',
            'encap',
            'ethpmCfgFailedBmp',
            'ethpmCfgFailedTs',
            'ethpmCfgState',
            'id',
            'mplsEnable',
            'mplsMtu',
            'mtu',
            'mtuInherit',
            'pcTag',
            'qosPrio',
            'routerMac',
            'rtdOutDefDn',
            'serviceEnabled'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # Dn format
        # topology/pod-1/node-201/sys/inst-overlay-1/encrtd-[eth1/108.7]
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

        if info['adminSt'] == 'up':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        info['state'] = None
        if managed_object['ethpmEncRtdIf'] is not None:
            info['state'] = {}

            keys = [
                'currErrIndex',
                'fsmState',
                'hwBdId',
                'hwResourceId',
                'iod',
                'lastErrors',
                'operBitset',
                'operMtu',
                'operSt',
                'operStQual',
                'siCfgFlags'
            ]

            for key in keys:
                info['state'][key] = None
                if key in managed_object['ethpmEncRtdIf']:
                    info['state'][key] = managed_object['ethpmEncRtdIf'][key]

            if info['state']['operSt'] == 'up':
                info['__Output']['state.operSt'] = 'Green'
                if info['state']['operStQual'] == 'none':
                    info['state']['operStQual'] = ''
            else:
                info['__Output']['state.operSt'] = 'Red'

        info['donorIf'] = ''
        info['__Output']['donorIf'] = 'Yellow'

        info['up'] = False
        if info['adminSt'] == 'up' and info['state']['operSt'] == 'up':
            info['up'] = True

        return info

    def get_interfaces_encap_routed_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_encap_routed:
            return self.interface_encap_routed[key]

        interfaces_mo = self.get_interface_encap_routed_mo(pod_id, node_id)
        if interfaces_mo is None:
            return None

        self.interface_encap_routed[key] = []
        for interface_mo in interfaces_mo:
            self.interface_encap_routed[key].append(
                self.get_interface_encap_routed_info(
                    interface_mo
                )
            )

        self.log.apic_mo(
            'l3EncRtdIf.info.%s' % (key),
            self.interface_encap_routed[key]
        )

        return self.interface_encap_routed[key]

    def match_interface_encap_routed(self, interface_info, interface_filter):
        if interface_filter is None or len(interface_filter) == 0:
            return True

        for ap_rule in interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'id':
                if not filter_helper.match_string(value, interface_info['id']):
                    return False

            if key == 'admin':
                if value != 'any':
                    if not filter_helper.match_string(value, interface_info['adminSt']):
                        return False

            if key == 'oper':
                if value != 'any':
                    if not filter_helper.match_string(value, interface_info['state']['operSt']):
                        return False

        return True

    def get_interfaces_encap_routed(self, pod_id, node_id, interface_filter=None):
        all_interfaces = self.get_interfaces_encap_routed_info(pod_id, node_id)
        if all_interfaces is None:
            return None

        interfaces = []

        ipv4_addresses_info = self.get_node_interface_ipv4(
            pod_id,
            node_id
        )

        for interface_info in all_interfaces:
            if not self.match_interface_encap_routed(interface_info, interface_filter):
                continue

            interface_search_pattern = '%s' % (interface_info['id'])
            for item in ipv4_addresses_info:
                if interface_search_pattern in item['id']:
                    if item['donorIf'] != 'unspecified':
                        interface_info['donorIf'] = item['donorIf']

            interfaces.append(
                interface_info
            )

        interfaces = sorted(
            interfaces,
            key=lambda i: i['id']
        )

        return interfaces

    def get_interface_encap_routed(self, pod_id, node_id, port_id):
        interfaces = self.get_interfaces_encap_routed(
            pod_id,
            node_id,
            interface_filter=['id:%s' % (port_id)]
        )

        if interfaces is None or len(interfaces) != 1:
            return None

        return interfaces[0]
