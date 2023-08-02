from lib import filter_helper


class InterfaceMgmtInfo():
    def __init__(self):
        self.interface_mgmt = {}

    def get_interface_management_count(self, pod_id, node_id):
        interfaces = self.get_interface_management(pod_id, node_id)
        return len(interfaces)

    def get_interface_management_summary(self, pod_id, node_id):
        ports = self.get_interface_management(
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

    def get_interface_management_info(self, managed_object):
        keys = [
            'adminSt',
            'autoNeg',
            'dn',
            'fcotChannelNumber',
            'id',
            'mtu',
            'name',
            'snmpTrapSt',
            'speed',
            'status',
            'switchingSt'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # Dn format
        # [0]: topology/pod-{id}/node-{id}/sys/mgmt-[{id}]
        info['podId'] = info['dn'].split('/')[1].split('-')[1]
        info['nodeId'] = info['dn'].split('/')[2].split('-')[1]

        info['apic'] = self.apic_name
        info['pod_node_name'] = 'pod-%s/%s' % (
            info['podId'],
            self.get_node_name(
                info['nodeId']
            )
        )

        if info['adminSt'] == 'up':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['switchingSt'] == 'enabled':
            info['__Output']['switchingSt'] = 'Green'
        else:
            info['__Output']['switchingSt'] = 'Red'

        info['up'] = False
        if info['adminSt'] == 'up':
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

    def get_interfaces_management_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_mgmt:
            return self.interface_mgmt[key]

        interfaces_mgmt_mo = self.get_interface_management_mo(pod_id, node_id)
        if interfaces_mgmt_mo is None:
            return None

        self.interface_mgmt[key] = []
        for interface_mgmt_mo in interfaces_mgmt_mo:
            self.interface_mgmt[key].append(
                self.get_interface_management_info(
                    interface_mgmt_mo
                )
            )

        self.log.apic_mo(
            'intfMgmt.info.%s' % (key),
            self.interface_mgmt[key]
        )

        return self.interface_mgmt[key]

    def match_interface_management(self, interface_info, interface_filter):
        if interface_filter is None or len(interface_filter) == 0:
            return True

        for ap_rule in interface_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'id':
                if not filter_helper.match_string(value, interface_info['id']):
                    return False

            # if key == 'admin':
            #     if value != 'any':
            #         if not filter_helper.match_string(value, interface_info['adminSt']):
            #             return False

            # if key == 'oper':
            #     if value != 'any':
            #         if not filter_helper.match_string(value, interface_info['state']['operSt']):
            #             return False

            if key == 'fault':
                if value == 'any':
                    if not interface_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_interface_management',
                        'Unsupported fault filtering value: %s' % (value)
                    )

        return True

    def get_interface_management(
            self,
            pod_id,
            node_id,
            interface_filter=None,
            state_info=False,
            stats_info=False,
            cdp_info=False,
            lldp_info=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        interfaces = self.get_interfaces_management_info(pod_id, node_id)
        if interfaces is None:
            return None

        for interface_info in interfaces:
            if not self.match_interface_management(interface_info, interface_filter):
                continue

            if state_info:
                interface_info['state'] = self.get_interface_management_state(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    interface_info['id']
                )

            if cdp_info:
                interface_info['cdp'] = self.get_cdp_adjacency_endpoint(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    interface_info['id'],
                    allow_multiple=False
                )

            if lldp_info:
                interface_info['lldp'] = self.get_lldp_adjacency_endpoint(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    adjacency_filter=['interface_id:%s' % (interface_info['id'])],
                    allow_multiple=False
                )

            if stats_info:
                interface_info['counters'] = self.get_interface_fault_counts(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    'mgmt',
                    interface_info['id']
                )

                interface_info['stats'] = self.get_interface_management_stats(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    interface_info['id']
                )

            if fault_info:
                interface_info['faultInst'] = self.get_interface_management_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultInst'
                )

            if hfault_info:
                interface_info['faultRecord'] = self.get_interface_management_id_fault(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                interface_info['eventLog'] = self.get_interface_management_id_event(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    event_filter=event_filter
                )

            if audit_info:
                interface_info['auditLog'] = self.get_interface_management_id_audit(
                    pod_id,
                    node_id,
                    interface_info['id'],
                    audit_filter=audit_filter
                )

            interface_info = self.my_output.merge_output(
                interface_info
            )

        return interfaces
