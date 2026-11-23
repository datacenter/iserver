from lib import filter_helper
from lib import ip_helper


class InterfaceSviInfo():
    def __init__(self):
        self.interface_svi = {}

    def get_interface_svi_summary(self, pod_id, node_id):
        ports = self.get_interfaces_svi(
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

    def get_interface_svi_count(self, pod_id, node_id):
        interfaces = self.get_interfaces_svi(pod_id, node_id)
        return len(interfaces)

    def get_interface_svi_info(self, managed_object):
        if 'sviIf' not in managed_object:
            return None

        keys = [
            'accEncap',
            'addr',
            'adminSt',
            'bdDefDn',
            'bridgeMode',
            'dn',
            'epMoveDetectMode',
            'epOperSt',
            'epOperStQual',
            'epUpSeqNum',
            'fabEncap',
            'fwdCtrl',
            'fwdMode',
            'hwId',
            'hwResourceId',
            'id',
            'ipv6McastAllow',
            'mcastAllow',
            'mcastOperSt',
            'operSt',
            'pcTag',
            'qiqL2ProtTunMask',
            'qosPrio',
            'serviceEnabled',
            'servicepcTag',
            'type',
            'unkMacUcastAct',
            'unkMcastAct',
            'v6unkMcastAct'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

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

        if info['adminSt'] == 'active':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        keys = [
            'adminSt',
            'bw',
            'carDel',
            'delay',
            'descr',
            'id',
            'iod',
            'mac',
            'medium',
            'mtu',
            'operSt',
            'operStQual',
            'rn',
            'vlanId',
            'vlanT',
            'vmac',
            'vmacChgQual',
            'faultCounts'
        ]

        info['sviIf'] = {}
        for key in keys:
            info['sviIf'][key] = None
            if key in managed_object['sviIf']:
                info['sviIf'][key] = managed_object['sviIf'][key]

        info['__Output']['sviIf.id'] = 'Blue'

        if info['sviIf']['adminSt'] == 'up':
            info['__Output']['sviIf.adminSt'] = 'Green'
        else:
            info['__Output']['sviIf.adminSt'] = 'Red'

        if info['sviIf']['operSt'] == 'up':
            info['__Output']['sviIf.operSt'] = 'Green'
            if info['sviIf']['operStQual'] == 'none':
                info['sviIf']['operStQual'] = ''
        else:
            info['__Output']['sviIf.operSt'] = 'Red'

        info['up'] = False
        if info['adminSt'] == 'active' and info['operSt'] == 'up':
            if info['sviIf']['adminSt'] == 'up' and info['sviIf']['operSt'] == 'up':
                info['up'] = True

        info['counters'] = {}
        info['counters']['inOctets'] = managed_object['rmonIfIn']['octets']
        info['counters']['inPackets'] = managed_object['rmonIfIn']['ucastPkts']
        info['counters']['inMcast'] = managed_object['rmonIfIn']['multicastPkts']
        info['counters']['inDiscards'] = managed_object['rmonIfIn']['discards']
        info['counters']['inErrors'] = managed_object['rmonIfIn']['errors']
        info['counters']['outOctets'] = managed_object['rmonIfOut']['octets']
        info['counters']['outPackets'] = managed_object['rmonIfOut']['ucastPkts']
        info['counters']['outMcast'] = managed_object['rmonIfOut']['multicastPkts']
        info['counters']['outDiscards'] = managed_object['rmonIfOut']['discards']
        info['counters']['outErrors'] = managed_object['rmonIfOut']['errors']

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        info['accEncapT'] = info['accEncap']
        if info['accEncap'] == 'unknown':
            info['accEncapT'] = '--'

        info['sviIf']['type'] = '--'
        if info['sviIf']['vlanT'] == 'bd-regular':
            info['sviIf']['type'] = 'Reg'
        if info['sviIf']['vlanT'] == 'bd-external':
            info['sviIf']['type'] = 'Ext'

        return info

    def get_interfaces_svi_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_svi:
            return self.interface_svi[key]

        interfaces_mo = self.get_interface_svi_mo(pod_id, node_id)
        if interfaces_mo is None:
            return None

        self.interface_svi[key] = []
        for interface_mo in interfaces_mo:
            interface_info = self.get_interface_svi_info(
                interface_mo
            )
            if interface_info is not None:
                self.interface_svi[key].append(
                    interface_info
                )

        self.log.apic_mo(
            'sviIf.info.%s' % (key),
            self.interface_svi[key]
        )

        return self.interface_svi[key]

    def match_interface_svi(self, interface_info, interface_filter):
        if interface_filter is None or len(interface_filter) == 0:
            return True

        for ap_rule in interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])
            found = False

            if key == 'id':
                found = True
                if not filter_helper.match_string(value, interface_info['sviIf']['id']):
                    return False

            if key == 'mac':
                found = True
                if not ip_helper.is_mac_match(value, interface_info['sviIf']['mac']):
                    return False

            if key == 'vlan':
                found = True
                matched = False

                if value.startswith('gt'):
                    if not filter_helper.match_integer(value, int(interface_info['sviIf']['vlanId'])):
                        return False
                    matched = True

                if value.startswith('ge'):
                    if not filter_helper.match_integer(value, int(interface_info['sviIf']['vlanId'])):
                        return False
                    matched = True

                if value.startswith('lt'):
                    if not filter_helper.match_integer(value, int(interface_info['sviIf']['vlanId'])):
                        return False
                    matched = True

                if value.startswith('le'):
                    if not filter_helper.match_integer(value, int(interface_info['sviIf']['vlanId'])):
                        return False
                    matched = True

                if '-' in value:
                    if not filter_helper.match_integer(value, int(interface_info['sviIf']['vlanId'])):
                        return False
                    matched = True

                if not matched:
                    if not filter_helper.match_string(value, interface_info['sviIf']['vlanId']):
                        return False

            if key == 'fabric':
                found = True
                if not filter_helper.match_string(value, interface_info['fabEncap']):
                    return False

            if key == 'access':
                found = True
                if not filter_helper.match_string(value, interface_info['accEncap']):
                    return False

            if key == 'admin':
                found = True
                if value != 'any':
                    if not filter_helper.match_string(value, interface_info['adminSt']):
                        return False

            if key == 'oper':
                found = True
                if value != 'any':
                    if not filter_helper.match_string(value, interface_info['operSt']):
                        return False

            if key == 'type':
                found = True
                if value != 'any':
                    if value == 'int':
                        if not filter_helper.match_string('bd-regular', interface_info['sviIf']['vlanT']):
                            return False

                    if value == 'ext':
                        if not filter_helper.match_string('bd-external', interface_info['sviIf']['vlanT']):
                            return False

            if key == 'ip':
                found = True
                if 'ipv4_address' in interface_info:
                    found = False
                    for ip_address in interface_info['ipv4_address']:
                        if ip_helper.is_ipv4_in_cidr(value, ip_address):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'subnet':
                found = True
                if 'ipv4_address' in interface_info:
                    found = False
                    for ip_address in interface_info['ipv4_address']:
                        if ip_helper.is_subnet_in_subnet(ip_address, value):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'fault':
                found = True
                if value == 'any':
                    if not interface_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_interface_svi',
                        'Unsupported fault filtering value: %s' % (value)
                    )

            if not found:
                self.log.error(
                    'match_interface_svi',
                    'Unsupported filtering key: %s' % (key)
                )

        return True

    def get_interfaces_svi(
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
        all_interfaces = self.get_interfaces_svi_info(pod_id, node_id)
        if all_interfaces is None:
            return None

        interfaces = []

        ipv4_addresses_info = self.get_node_address_ipv4(
            pod_id,
            node_id
        )

        for interface_info in all_interfaces:
            if not self.match_interface_svi(interface_info, interface_filter):
                continue

            interface_info['ipv4_address'] = []
            interface_info['ipv4_info'] = []
            search_pattern = 'if-[%s]' % (
                interface_info['sviIf']['id']
            )
            for ipv4_address_info in ipv4_addresses_info:
                if search_pattern in ipv4_address_info['dn']:
                    address_info = {}
                    address_info['__Output'] = {}
                    address_info['addr'] = ipv4_address_info['addr']
                    address_info['iaddr'] = ip_helper.ipv4_to_int(
                        ipv4_address_info['addr'].split('/')[0]
                    )
                    address_info['operSt'] = ipv4_address_info['operSt']
                    address_info['operStQual'] = ipv4_address_info['operStQual']
                    address_info['type'] = ipv4_address_info['type']
                    address_info['vpcPeer'] = ipv4_address_info['vpcPeer']

                    if address_info['operSt'] == 'up':
                        address_info['__Output']['operSt'] = 'Green'
                        address_info['operStQual'] = ''
                    else:
                        address_info['__Output']['operSt'] = 'Red'

                    interface_info['ipv4_info'].append(
                        address_info
                    )

                    interface_info['ipv4_address'].append(
                        ipv4_address_info['addr']
                    )

            interface_info['ipv4_info'] = sorted(
                interface_info['ipv4_info'],
                key=lambda i: i['iaddr']
            )

            interface_info['ipv4_addressT'] = []
            for ipv4_info in interface_info['ipv4_info']:
                if ipv4_info['type'] == 'primary' and len(interface_info['ipv4_info']) > 1:
                    interface_info['ipv4_addressT'].append(
                        '%s (pri)' % (
                            ipv4_info['addr']
                        )
                    )
                    continue

                interface_info['ipv4_addressT'].append(
                    ipv4_info['addr']
                )

            if not self.match_interface_svi(interface_info, interface_filter):
                continue

            if fault_info:
                interface_info['faultInst'] = self.get_interface_svi_vlan_fault(
                    pod_id,
                    node_id,
                    interface_info['sviIf']['id'],
                    'faultInst'
                )

            if hfault_info:
                interface_info['faultRecord'] = self.get_interface_svi_vlan_fault(
                    pod_id,
                    node_id,
                    interface_info['sviIf']['id'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                interface_info['eventLog'] = self.get_interface_svi_vlan_event(
                    pod_id,
                    node_id,
                    interface_info['sviIf']['id'],
                    event_filter=event_filter
                )

            if audit_info:
                interface_info['auditLog'] = self.get_interface_svi_id_audit(
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
            key=lambda i: int(i['id'])
        )

        return interfaces

    def get_interface_svi(self, pod_id, node_id, interface_id):
        interfaces = self.get_interfaces_svi(
            pod_id,
            node_id,
            interface_filter=['id:%s' % (interface_id)]
        )

        if interfaces is None or len(interfaces) != 1:
            return None

        return interfaces[0]
