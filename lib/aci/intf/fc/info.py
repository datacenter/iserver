from lib import filter_helper


class InterfaceFcInfo():
    def __init__(self):
        self.interface_fc = {}

    def get_interface_fc_summary(self, pod_id, node_id):
        ports = self.get_interfaces_fc(
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

    def get_interface_fc_count(self, pod_id, node_id):
        interfaces = self.get_interfaces_fc(pod_id, node_id)
        return len(interfaces)

    def get_interface_fc_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
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

        if managed_object['l1RtFcBrConf'] is not None:
            info['state'] = {}
            for key in managed_object['l1RtFcBrConf']:
                info['state'][key] = managed_object['l1RtFcBrConf'][key]

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

    def get_interfaces_fc_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_fc:
            return self.interface_fc[key]

        interfaces_mo = self.get_interface_fc_mo(pod_id, node_id)
        if interfaces_mo is None:
            return None

        self.interface_fc[key] = []
        for interface_mo in interfaces_mo:
            self.interface_fc[key].append(
                self.get_interface_fc_info(
                    interface_mo
                )
            )

        self.log.apic_mo(
            'l1FcPhysIf.info.%s' % (key),
            self.interface_fc[key]
        )

        return self.interface_fc[key]

    def match_interface_fc(self, interface_info, interface_filter):
        if interface_filter is None or len(interface_filter) == 0:
            return True

        for ap_rule in interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'id':
                if not filter_helper.match_string(value, interface_info['id']):
                    return False

            if key == 'fault':
                if value == 'any':
                    if not interface_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_interface_fc',
                        'Unsupported fault filtering value: %s' % (value)
                    )

        return True

    def get_interfaces_fc(
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
        all_interfaces = self.get_interfaces_fc_info(pod_id, node_id)
        if all_interfaces is None:
            return None

        interfaces = []

        for interface_info in all_interfaces:
            if not self.match_interface_fc(interface_info, interface_filter):
                continue

            if fault_info:
                interface_info['faultInst'] = self.get_interface_fc_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultInst'
                )

            if hfault_info:
                interface_info['faultRecord'] = self.get_interface_fc_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                interface_info['eventLog'] = self.get_interface_fc_id_event(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    event_filter=event_filter
                )

            if audit_info:
                interface_info['auditLog'] = self.get_interface_fc_id_audit(
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

    def get_interface_fc(self, pod_id, node_id, port_id):
        interfaces = self.get_interfaces_fc(
            pod_id,
            node_id,
            interface_filter=['id:%s' % (port_id)]
        )

        if interfaces is None or len(interfaces) != 1:
            return None

        return interfaces[0]
