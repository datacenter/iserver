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

        info['apic'] = self.apic_label
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

    def get_interface_management(self, pod_id, node_id, cdp_info=False, lldp_info=False, faults_info=False, state_info=False, stats_info=False):
        interfaces = self.get_interfaces_management_info(pod_id, node_id)
        if interfaces is None:
            return None

        for interface_info in interfaces:
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
                    lldp_filter=['interface_id:%s' % (interface_info['id'])],
                    allow_multiple=False
                )

            if faults_info:
                interface_info['faults'] = self.get_interface_fault_counts(
                    interface_info['podId'],
                    interface_info['nodeId'],
                    'mgmt',
                    interface_info['id']
                )

            interface_info['state'] = self.get_interface_management_state(
                interface_info['podId'],
                interface_info['nodeId'],
                interface_info['id']
            )

            interface_info['stats'] = self.get_interface_management_stats(
                interface_info['podId'],
                interface_info['nodeId'],
                interface_info['id']
            )

            interface_info = self.my_output.merge_output(
                interface_info
            )

        return interfaces
