class ProtocolLldpFaultInfo():
    def __init__(self):
        self.lldp_fault = {}
        self.lldp_fault_record = {}

    def get_protocol_lldp_fault_info(self, managed_object):
        info = self.get_system_fault_info(
            managed_object
        )

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        # "affected": "topology/pod-1/node-2208/sys/lldp/inst/if-[eth1/4/3]/adj-1"
        info['interface_id'] = None

        if not managed_object['delegated']:
            if 'affected' in info:
                if 'sys/lldp/inst/if-[' in info['affected']:
                    info['interface_id'] = info['affected'].split('sys/lldp/inst/if-[')[1].split(']')[0]

        # "dn": "subj-[topology/pod-1/node-2208/sys/lldp/inst/if-[eth1/4/3]/adj-1]/rec-12886869434",
        if info['interface_id'] is None:
            if 'sys/lldp/inst/if-' in info['dn']:
                info['interface_id'] = info['dn'].split('sys/lldp/inst/if-[')[1].split(']')[0]

        info['severityT'] = self.system_fault_severity_name[info['severity']]
        info['__Output']['severityT'] = self.system_fault_severity_color[info['severity']]

        return info

    def get_protocol_lldp_fault(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.lldp_fault:
            return self.lldp_fault[key]

        managed_objects = self.get_protocol_lldp_fault_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.lldp_fault[key] = []
        for managed_object in managed_objects:
            self.lldp_fault[key].append(
                self.get_protocol_lldp_fault_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'lldpInst.fault.info.%s' % (key),
            self.lldp_fault[key]
        )

        return self.lldp_fault[key]

    def get_protocol_lldp_fault_record(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.lldp_fault_record:
            return self.lldp_fault_record[key]

        managed_objects = self.get_protocol_lldp_fault_record_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.lldp_fault_record[key] = []
        for managed_object in managed_objects:
            self.lldp_fault_record[key].append(
                self.get_protocol_lldp_fault_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'lldpInst.faultRecord.info.%s' % (key),
            self.lldp_fault_record[key]
        )

        return self.lldp_fault_record[key]

    def get_protocol_lldp_adjacency_fault(self, pod_id, node_id, interface_id, fault_object, fault_filter=None):
        faults = []

        if fault_object == 'faultInst':
            all_faults = self.get_protocol_lldp_fault(
                pod_id,
                node_id
            )
            if all_faults is None:
                return faults

            fault_filter = self.remove_system_fault_timestamp_filter(
                fault_filter
            )

        if fault_object == 'faultRecord':
            all_faults = self.get_protocol_lldp_fault_record(
                pod_id,
                node_id
            )
            if all_faults is None:
                return faults

        for fault_info in all_faults:
            if fault_info['interface_id'] is not None:
                if fault_info['interface_id'] == interface_id:
                    if not self.match_system_fault(fault_info, fault_filter, exclude_cleared=False):
                        continue

                    faults.append(
                        fault_info
                    )

        return faults
