from lib import filter_helper


class InterfaceMacSecInfo():
    def __init__(self):
        self.interface_macsec = {}

    def get_interface_macsec_summary(self, pod_id, node_id):
        ports = self.get_interfaces_macsec(
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

    def get_interface_macsec_count(self, pod_id, node_id):
        interfaces = self.get_interfaces_macsec(pod_id, node_id)
        return len(interfaces)

    def get_interface_macsec_info(self, managed_object):
        keys = [
            'adminSt',
            'cipherSuite',
            'cipherSuiteOper',
            'confOffset',
            'confOffsetOper',
            'dn',
            'id',
            'keyChain',
            'keySvrPrio',
            'lastSakKeyTime',
            'mkaNegSt',
            'name',
            'operSt',
            'operStQual',
            'peerCount',
            'portId',
            'replayWindow',
            'sakExpiryTime',
            'sakStatus',
            'secPolicy',
            'sessOperSt',
            'srvStatusFlags',
            'txSCI',
            'txSSCI',
            'vlanTagCtrl'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['iod'] = int(info['id'].split('/')[1])

        # Dn format
        # topology/pod-1/node-201/sys/macsec/inst/if-[eth1/97]
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

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        if info['adminSt'] == 'enabled' and info['operSt'] == 'up':
            info['up'] = True
        else:
            info['up'] = False

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_interfaces_macsec_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_macsec:
            return self.interface_macsec[key]

        interfaces_mo = self.get_interface_macsec_mo(pod_id, node_id)
        if interfaces_mo is None:
            return None

        self.interface_macsec[key] = []
        for interface_mo in interfaces_mo:
            self.interface_macsec[key].append(
                self.get_interface_macsec_info(
                    interface_mo
                )
            )

        self.log.apic_mo(
            'macsecIf.info.%s' % (key),
            self.interface_macsec[key]
        )

        return self.interface_macsec[key]

    def match_interface_macsec(self, interface_info, interface_filter):
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
                    if not filter_helper.match_string(value, interface_info['operSt']):
                        return False

            if key == 'type':
                if 'portT' in interface_info:
                    if value != 'any':
                        if not filter_helper.match_string(value, interface_info['portT']):
                            return False

            if key == 'fault':
                if value == 'any':
                    if not interface_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_interface_macsec',
                        'Unsupported fault filtering value: %s' % (value)
                    )

        return True

    def get_interfaces_macsec(
            self,
            pod_id,
            node_id,
            interface_filter=None,
            stats_info=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_interfaces = self.get_interfaces_macsec_info(pod_id, node_id)
        if all_interfaces is None:
            return None

        phy_ports = self.get_interfaces_phy(
            pod_id,
            node_id
        )

        interfaces = []

        for interface_info in all_interfaces:
            if not self.match_interface_macsec(interface_info, interface_filter):
                continue

            for phy_port in phy_ports:
                if interface_info['id'] == phy_port['id']:
                    interface_info['portT'] = phy_port['portT']

            if not self.match_interface_macsec(interface_info, interface_filter):
                continue

            if stats_info:
                interface_info['tx'] = self.get_interface_macsec_tx(
                    pod_id,
                    node_id,
                    interface_info['id']
                )

                interface_info['rx'] = self.get_interface_macsec_rx(
                    pod_id,
                    node_id,
                    interface_info['id']
                )

                interface_info['stats'] = self.get_interface_macsec_stats(
                    pod_id,
                    node_id,
                    interface_info['id']
                )

                interface_info['castats'] = self.get_interface_macsec_castats(
                    pod_id,
                    node_id,
                    interface_info['id']
                )

            if fault_info:
                interface_info['faultInst'] = self.get_interface_macsec_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultInst'
                )

            if hfault_info:
                interface_info['faultRecord'] = self.get_interface_macsec_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                interface_info['eventLog'] = self.get_interface_macsec_id_event(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    event_filter=event_filter
                )

            if audit_info:
                interface_info['auditLog'] = self.get_interface_macsec_id_audit(
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
            key=lambda i: i['iod']
        )

        return interfaces

    def get_interface_macsec(self, pod_id, node_id, port_id, stats_info=False):
        interfaces = self.get_interfaces_macsec(
            pod_id,
            node_id,
            interface_filter=['id:%s' % (port_id)],
            stats_info=stats_info
        )

        if interfaces is None or len(interfaces) != 1:
            return None

        return interfaces[0]
