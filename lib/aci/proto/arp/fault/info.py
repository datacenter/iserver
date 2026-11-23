class ProtocolArpFaultInfo():
    def __init__(self):
        self.proto_arp_fault = {}
        self.proto_arp_fault_record = {}

    def get_protocol_arp_fault_info(self, managed_object):
        info = self.get_system_fault_info(
            managed_object
        )

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        info['severityT'] = self.system_fault_severity_name[info['severity']]
        info['__Output']['severityT'] = self.system_fault_severity_color[info['severity']]

        return info

    def get_protocol_arp_fault(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.proto_arp_fault:
            return self.proto_arp_fault[key]

        managed_objects = self.get_protocol_arp_fault_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.proto_arp_fault[key] = []
        for managed_object in managed_objects:
            self.proto_arp_fault[key].append(
                self.get_protocol_arp_fault_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'arpDom.fault.info.%s' % (key),
            self.proto_arp_fault[key]
        )

        return self.proto_arp_fault[key]

    def get_protocol_arp_fault_record(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.proto_arp_fault_record:
            return self.proto_arp_fault_record[key]

        managed_objects = self.get_protocol_arp_fault_record_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.proto_arp_fault_record[key] = []
        for managed_object in managed_objects:
            self.proto_arp_fault_record[key].append(
                self.get_protocol_arp_fault_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'arpDom.faultRecord.info.%s' % (key),
            self.proto_arp_fault_record[key]
        )

        return self.proto_arp_fault_record[key]
