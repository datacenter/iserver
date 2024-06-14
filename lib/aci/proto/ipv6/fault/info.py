class ProtocolIpv6FaultInfo():
    def __init__(self):
        self.proto_ipv6_fault = {}
        self.proto_ipv6_fault_record = {}

    def get_protocol_ipv6_fault_info(self, managed_object):
        info = self.get_system_fault_info(
            managed_object
        )

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        # topology/pod-1/node-2208/sys/ipv6/inst/dom-common:Infra_privIP_VRF/if-[vlan50]/addr-[<ip>/24]
        info['domainName'] = None
        if 'affected' in info:
            if 'sys/ipv6/inst/dom-' in info['affected']:
                info['domainName'] = info['affected'].split('sys/ipv6/inst/dom-')[1].split('/')[0]
        info['domainNameT'] = info['domainName']
        if info['domainNameT'] is None:
            info['domainNameT'] = '--'

        info['interfaceId'] = None
        if 'affected' in info:
            if '/if-[' in info['affected']:
                info['interfaceId'] = info['affected'].split('/if-[')[1].split(']')[0]
        info['interfaceIdT'] = info['interfaceId']
        if info['interfaceIdT'] is None:
            info['interfaceIdT'] = '--'

        info['address'] = None
        if 'affected' in info:
            if '/addr-[' in info['affected']:
                info['address'] = info['affected'].split('/addr-[')[1].split(']')[0]
        info['addressT'] = info['address']
        if info['addressT'] is None:
            info['addressT'] = '--'

        info['severityT'] = self.system_fault_severity_name[info['severity']]
        info['__Output']['severityT'] = self.system_fault_severity_color[info['severity']]

        return info

    def get_protocol_ipv6_fault(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.proto_ipv6_fault:
            return self.proto_ipv6_fault[key]

        managed_objects = self.get_protocol_ipv6_fault_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.proto_ipv6_fault[key] = []
        for managed_object in managed_objects:
            self.proto_ipv6_fault[key].append(
                self.get_protocol_ipv6_fault_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'ipv6Dom.fault.info.%s' % (key),
            self.proto_ipv6_fault[key]
        )

        return self.proto_ipv6_fault[key]

    def get_protocol_ipv6_fault_record(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.proto_ipv6_fault_record:
            return self.proto_ipv6_fault_record[key]

        managed_objects = self.get_protocol_ipv6_fault_record_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.proto_ipv6_fault_record[key] = []
        for managed_object in managed_objects:
            self.proto_ipv6_fault_record[key].append(
                self.get_protocol_ipv6_fault_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'ipv6Dom.faultRecord.info.%s' % (key),
            self.proto_ipv6_fault_record[key]
        )

        return self.proto_ipv6_fault_record[key]
