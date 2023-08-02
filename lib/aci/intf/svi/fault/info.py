import time
from datetime import datetime

from lib import filter_helper


class InterfaceSviFaultInfo():
    def __init__(self):
        self.interface_svi_fault = {}
        self.interface_svi_fault_record = {}

    def get_interface_svi_fault_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        # "affected": "topology/pod-1/node-2208/sys/ctx-[vxlan-2228224]/bd-[vxlan-15597460]/svi-[vlan33]"
        info['interfaceId'] = None
        if not managed_object['delegated']:
            if 'affected' in info:
                if '/svi-[' in info['affected']:
                    info['interfaceId'] = info['affected'].split('/svi-[')[1].split(']')[0]

        # "dn": "topology/pod-1/node-2208/sys/ctx-[vxlan-2293761]/bd-[vxlan-15237056]/svi-[vlan30]/fault-F112128"
        if info['interfaceId'] is None:
            if '/svi-[' in info['dn']:
                info['interfaceId'] = info['dn'].split('/svi-[')[1].split(']')[0]

        info['descrT'] = filter_helper.get_string_chunks(
            filter_helper.sanitize_string(
                info['descr']
            ),
            80
        )

        info['dnT'] = filter_helper.get_string_chunks(
            info['dn'],
            40,
            separator='/'
        )

        # "2022-04-29T13:32:45.167+02:00"
        info['timestamp'] = int(
            time.mktime(
                datetime.strptime(
                    info['created'],
                    '%Y-%m-%dT%H:%M:%S.%f%z'
                ).timetuple()
            )
        )

        info['severityT'] = self.system_fault_severity_name[info['severity']]
        info['__Output']['severityT'] = self.system_fault_severity_color[info['severity']]

        return info

    def get_interface_svi_fault(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_svi_fault:
            return self.interface_svi_fault[key]

        managed_objects = self.get_interface_svi_fault_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.interface_svi_fault[key] = []
        for managed_object in managed_objects:
            fault_info = self.get_interface_svi_fault_info(
                managed_object
            )
            self.interface_svi_fault[key].append(
                fault_info
            )

        self.log.apic_mo(
            'svi.fault.info.%s' % (key),
            self.interface_svi_fault[key]
        )

        return self.interface_svi_fault[key]

    def get_interface_svi_fault_record(self, pod_id, node_id, deduplicate=True):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_svi_fault_record:
            return self.interface_svi_fault_record[key]

        managed_objects = self.get_interface_svi_fault_record_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        self.interface_svi_fault_record[key] = []
        fault_ids = []

        for managed_object in managed_objects:
            fault_info = self.get_interface_svi_fault_info(
                managed_object
            )
            if not deduplicate or fault_info['id'] not in fault_ids:
                self.interface_svi_fault_record[key].append(
                    fault_info
                )
                fault_ids.append(
                    fault_info['id']
                )

        self.log.apic_mo(
            'svi.faultRecord.info.%s' % (key),
            self.interface_svi_fault_record[key]
        )

        return self.interface_svi_fault_record[key]

    def get_interface_svi_vlan_fault(self, pod_id, node_id, interface_id, fault_object, fault_filter=None):
        faults = []

        if fault_object == 'faultInst':
            all_faults = self.get_interface_svi_fault(pod_id, node_id)
            if all_faults is None:
                return faults

            fault_filter = self.remove_system_fault_timestamp_filter(
                fault_filter
            )

        if fault_object == 'faultRecord':
            all_faults = self.get_interface_svi_fault_record(pod_id, node_id)
            if all_faults is None:
                return faults

        for fault_info in all_faults:
            if fault_info['interfaceId'] is not None:
                if fault_info['interfaceId'] == interface_id:
                    if not self.match_system_fault(fault_info, fault_filter, exclude_cleared=False):
                        continue

                    faults.append(
                        fault_info
                    )

        return faults
