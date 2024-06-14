class ProtocolBgpFaultInfo():
    def __init__(self):
        self.proto_bgp_fault = {}
        self.proto_bgp_fault_record = {}

    def get_protocol_bgp_fault_info(self, managed_object):
        info = self.get_system_fault_info(
            managed_object
        )

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        # "dn": "topology/pod-1/node-2208/sys/bgp/inst/dom-vEPC_demo:ACC_VRF/peer-[<ip>/32]/ent-[<ip>]/fault-F0299"

        info['domainName'] = None
        info['nei'] = None

        if 'affected' in info:
            if 'sys/bgp/inst/dom-' in info['affected']:
                info['domainName'] = info['affected'].split('sys/bgp/inst/dom-')[1].split('/')[0]

            if '/peer-[' in info['affected']:
                info['nei'] = info['affected'].split('/peer-[')[1].split(']')[0]

        if info['domainName'] is None:
            if 'sys/bgp/inst/dom-' in info['dn']:
                info['domainName'] = info['dn'].split('sys/bgp/inst/dom-')[1].split('/')[0]

            if '/peer-[' in info['dn']:
                info['nei'] = info['dn'].split('/peer-[')[1].split(']')[0]

        info['domainNameT'] = info['domainName']
        if info['domainNameT'] is None:
            info['domainNameT'] = '--'

        info['neiT'] = info['nei']
        if info['neiT'] is None:
            info['neiT'] = '--'

        info['severityT'] = self.system_fault_severity_name[info['severity']]
        info['__Output']['severityT'] = self.system_fault_severity_color[info['severity']]

        return info

    def get_protocol_bgp_fault(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.proto_bgp_fault:
            return self.proto_bgp_fault[key]

        managed_objects = self.get_protocol_bgp_fault_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.proto_bgp_fault[key] = []
        for managed_object in managed_objects:
            self.proto_bgp_fault[key].append(
                self.get_protocol_bgp_fault_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'bgpDom.fault.info.%s' % (key),
            self.proto_bgp_fault[key]
        )

        return self.proto_bgp_fault[key]

    def get_protocol_bgp_fault_record(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.proto_bgp_fault_record:
            return self.proto_bgp_fault_record[key]

        managed_objects = self.get_protocol_bgp_fault_record_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.proto_bgp_fault_record[key] = []
        for managed_object in managed_objects:
            self.proto_bgp_fault_record[key].append(
                self.get_protocol_bgp_fault_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'bgpDom.faultRecord.info.%s' % (key),
            self.proto_bgp_fault_record[key]
        )

        return self.proto_bgp_fault_record[key]
