from lib import filter_helper
from lib import ip_helper


class InterfaceLoopbackInfo():
    def __init__(self, log_id=None):
        self.interface_lb = {}

    def get_interfaces_loopback_count(self, pod_id, node_id):
        interfaces = self.get_interfaces_loopback(pod_id, node_id)
        return len(interfaces)

    def get_interface_looback_summary(self, pod_id, node_id):
        ports = self.get_interfaces_loopback(
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

    def get_interface_loopback_info(self, managed_object):
        self.log.apic_mo(
            'l3LbRtdIf',
            managed_object
        )

        keys = [
            'adminSt',
            'dn',
            'id',
            'qosPrio',
            'rtdOutDefDn',
            'status',
            'type'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['iod'] = int(info['id'].strip('lo'))

        # Dn format
        # topology/pod-1/node-201/sys/inst-overlay-1/lb-[lo0]
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
        if managed_object['ethpmLbRtdIf'] is not None:
            info['state'] = {}

            keys = [
                'currErrIndex',
                'iod',
                'lastErrors',
                'operSt',
                'operStQual'
            ]

            for key in keys:
                info['state'][key] = None
                if key in managed_object['ethpmLbRtdIf']:
                    info['state'][key] = managed_object['ethpmLbRtdIf'][key]

            if info['state']['operSt'] == 'up':
                info['__Output']['state.operSt'] = 'Green'
                if info['state']['operStQual'] == 'none':
                    info['state']['operStQual'] = ''
            else:
                info['__Output']['state.operSt'] = 'Red'

        info['up'] = False
        if info['adminSt'] == 'up' and info['state']['operSt'] == 'up':
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

        return info

    def get_interfaces_loopback_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_lb:
            return self.interface_lb[key]

        interfaces_mo = self.get_interface_loopback_mo(pod_id, node_id)
        if interfaces_mo is None:
            return None

        self.interface_lb[key] = []
        for interface_mo in interfaces_mo:
            self.interface_lb[key].append(
                self.get_interface_loopback_info(
                    interface_mo
                )
            )

        self.log.apic_mo(
            'l3LbRtdIf.info.%s' % (key),
            self.interface_lb[key]
        )

        return self.interface_lb[key]

    def match_interface_loopback(self, interface_info, interface_filter):
        if interface_filter is None or len(interface_filter) == 0:
            return True

        for ap_rule in interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'id':
                if not filter_helper.match_string(value, interface_info['id']):
                    return False

            if key == 'ip':
                if 'ipv4' in interface_info:
                    if interface_info['ipv4'] is None:
                        return False

                    if not filter_helper.match_string('%s/32' % (value), interface_info['ipv4']['addr']):
                        return False

            if key == 'subnet':
                if 'ipv4' in interface_info:
                    if interface_info['ipv4'] is None:
                        return False

                    if not ip_helper.is_ipv4_in_cidr(interface_info['ipv4']['addr'].split('/')[0], value):
                        return False

            if key == 'fault':
                if value == 'any':
                    if not interface_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_interface_loopback',
                        'Unsupported fault filtering value: %s' % (value)
                    )

        return True

    def get_interfaces_loopback(
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
        all_interfaces = self.get_interfaces_loopback_info(pod_id, node_id)
        if all_interfaces is None:
            return None

        interfaces = []

        ipv4_addresses_info = self.get_node_address_ipv4(
            pod_id,
            node_id
        )

        for interface_info in all_interfaces:
            if not self.match_interface_loopback(interface_info, interface_filter):
                continue

            interface_info['ipv4'] = None
            interface_search_pattern = 'if-[%s]' % (interface_info['id'])
            for ipv4_address_info in ipv4_addresses_info:
                if interface_search_pattern in ipv4_address_info['dn']:
                    interface_info['ipv4'] = ipv4_address_info

            if not self.match_interface_loopback(interface_info, interface_filter):
                continue

            if fault_info:
                interface_info['faultInst'] = self.get_interface_loopback_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultInst'
                )

            if hfault_info:
                interface_info['faultRecord'] = self.get_interface_loopback_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                interface_info['eventLog'] = self.get_interface_loopback_id_event(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    event_filter=event_filter
                )

            if audit_info:
                interface_info['auditLog'] = self.get_interface_loopback_id_audit(
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

    def get_interface_loopback(self, pod_id, node_id, port_id):
        interfaces = self.get_interfaces_loopback(
            pod_id,
            node_id,
            interface_filter=['id:%s' % (port_id)]
        )

        if interfaces is None or len(interfaces) != 1:
            return None

        return interfaces[0]
