class ProtocolBfdFaultInfo():
    def __init__(self):
        self.bfd_fault = {}
        self.bfd_fault_record = {}

    def get_protocol_bfd_fault_info(self, managed_object):
        info = self.get_system_fault_info(
            managed_object
        )

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        # "affected": "topology/pod-1/node-2208/sys/bfd/inst/session-1090519092"
        info['session_id'] = None

        if not managed_object['delegated']:
            if 'affected' in info:
                if len(info['affected'].split('/')) == 7:
                    if info['affected'].split('/')[6].startswith('session-'):
                        info['session_id'] = info['affected'].split('/')[6].split('-')[1]

        if info['session_id'] is None:
            if info['dn'].split('/')[6].startswith('session-'):
                info['session_id'] = info['dn'].split('/')[6].split('-')[1]

        info['severityT'] = self.system_fault_severity_name[info['severity']]
        info['__Output']['severityT'] = self.system_fault_severity_color[info['severity']]

        return info

    def get_protocol_bfd_fault(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bfd_fault:
            return self.bfd_fault[key]

        managed_objects = self.get_protocol_bfd_fault_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.bfd_fault[key] = []
        for managed_object in managed_objects:
            self.bfd_fault[key].append(
                self.get_protocol_bfd_fault_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'bfdInst.fault.info.%s' % (key),
            self.bfd_fault[key]
        )

        return self.bfd_fault[key]

    def get_protocol_bfd_fault_record(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bfd_fault_record:
            return self.bfd_fault_record[key]

        managed_objects = self.get_protocol_bfd_fault_record_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.bfd_fault_record[key] = []
        for managed_object in managed_objects:
            self.bfd_fault_record[key].append(
                self.get_protocol_bfd_fault_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'bfdInst.faultRecord.info.%s' % (key),
            self.bfd_fault_record[key]
        )

        return self.bfd_fault_record[key]

    def get_protocol_bfd_session_fault(self, pod_id, node_id, session_id, fault_object, fault_filter=None):
        faults = []

        if fault_object == 'faultInst':
            all_faults = self.get_protocol_bfd_fault(pod_id, node_id)
            if all_faults is None:
                return faults

            fault_filter = self.remove_system_fault_timestamp_filter(
                fault_filter
            )

        if fault_object == 'faultRecord':
            all_faults = self.get_protocol_bfd_fault_record(pod_id, node_id)
            if all_faults is None:
                return faults

        for fault_info in all_faults:
            if fault_info['session_id'] is not None:
                if fault_info['session_id'] == session_id:
                    if not self.match_system_fault(fault_info, fault_filter, exclude_cleared=False):
                        continue

                    faults.append(
                        fault_info
                    )

        return faults
