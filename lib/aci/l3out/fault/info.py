import time
from datetime import datetime

from lib import filter_helper


class L3OutFaultInfo():
    def __init__(self):
        self.l3out_fault = None
        self.l3out_fault_record = None

    def get_l3out_fault_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['tenantName'] = None
        info['l3outName'] = None

        if not managed_object['delegated']:
            if 'affected' in info:
                if 'uni/tn-' in info['affected']:
                    # uni/tn-k8s/l3out-bmk8s_3_BD
                    info['tenantName'] = info['affected'].split('uni/tn-')[1].split('/')[0]

                if '/l3out-' in info['affected']:
                    info['l3outName'] = info['affected'].split('/l3out-')[1].split('/')[0]

                if '/out-' in info['affected']:
                    info['l3outName'] = info['affected'].split('/out-')[1].split('/')[0]

        if info['tenantName'] is None:
            if 'uni/tn-' in info['dn']:
                # uni/tn-k8s/l3out-bmk8s_3_BD
                info['tenantName'] = info['dn'].split('uni/tn-')[1].split('/')[0]

            if '/l3out-' in info['dn']:
                info['l3outName'] = info['dn'].split('/l3out-')[1].split('/')[0]

            if '/out-' in info['dn']:
                info['l3outName'] = info['dn'].split('/out-')[1].split('/')[0]

        info['nameTenant'] = '--'
        if info['tenantName'] is not None and info['l3outName'] is not None:
            info['nameTenant'] = '%s/%s' % (
                info['tenantName'],
                info['l3outName']
            )

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

        # "3033-04-39T13:33:45.167+03:00"
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

    def get_l3out_fault(self):
        if self.l3out_fault is not None:
            return self.l3out_fault

        managed_objects = self.get_l3out_fault_mo()
        if managed_objects is None:
            return None

        self.l3out_fault = []

        for managed_object in managed_objects:
            fault_info = self.get_l3out_fault_info(
                managed_object
            )
            self.l3out_fault.append(
                fault_info
            )

        self.log.apic_mo(
            'l3extOut.fault.info',
            self.l3out_fault
        )

        return self.l3out_fault

    def get_l3out_fault_record(self, deduplicate=True):
        if self.l3out_fault_record is not None:
            return self.l3out_fault_record

        managed_objects = self.get_l3out_fault_record_mo()
        if managed_objects is None:
            return None

        self.l3out_fault_record = []
        fault_ids = []

        for managed_object in managed_objects:
            fault_info = self.get_l3out_fault_info(
                managed_object
            )
            if not deduplicate or fault_info['id'] not in fault_ids:
                self.l3out_fault_record.append(
                    fault_info
                )
                fault_ids.append(
                    fault_info['id']
                )

        self.log.apic_mo(
            'l3extOut.faultRecord.info',
            self.l3out_fault_record
        )

        return self.l3out_fault_record

    def get_l3out_id_fault(self, tenant_name, l3out_name, fault_object, fault_filter=None):
        faults = []

        if fault_object == 'faultInst':
            all_faults = self.get_l3out_fault()
            if all_faults is None:
                return faults

            fault_filter = self.remove_system_fault_timestamp_filter(
                fault_filter
            )

        if fault_object == 'faultRecord':
            all_faults = self.get_l3out_fault_record()
            if all_faults is None:
                return faults

        for fault_info in all_faults:
            if fault_info['tenantName'] is not None and fault_info['l3outName'] is not None:
                if fault_info['tenantName'] == tenant_name and fault_info['l3outName'] == l3out_name:
                    if not self.match_system_fault(fault_info, fault_filter, exclude_cleared=False):
                        continue

                    faults.append(
                        fault_info
                    )

        return faults
