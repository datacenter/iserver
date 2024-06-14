import time
from datetime import datetime

from lib import filter_helper


class BridgeDomainFaultInfo():
    def __init__(self):
        self.bridge_domain_fault = None
        self.bridge_domain_fault_record = None

    def get_bridge_domain_fault_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['tenantName'] = None
        info['bdName'] = None

        if not managed_object['delegated']:
            if 'affected' in info:
                if 'uni/tn-' in info['affected']:
                    # uni/tn-k8s/BD-bmk8s_2_BD
                    info['tenantName'] = info['affected'].split('uni/tn-')[1].split('/')[0]

                if '/BD-' in info['affected']:
                    info['bdName'] = info['affected'].split('/BD-')[1].split('/')[0]

        if info['tenantName'] is None:
            if 'uni/tn-' in info['dn']:
                # uni/tn-k8s/BD-bmk8s_2_BD
                info['tenantName'] = info['dn'].split('uni/tn-')[1].split('/')[0]

            if '/BD-' in info['dn']:
                info['bdName'] = info['dn'].split('/BD-')[1].split('/')[0]

        info['nameTenant'] = '--'
        if info['tenantName'] is not None and info['bdName'] is not None:
            info['nameTenant'] = '%s/%s' % (
                info['tenantName'],
                info['bdName']
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

    def get_bridge_domain_fault(self):
        if self.bridge_domain_fault is not None:
            return self.bridge_domain_fault

        managed_objects = self.get_bridge_domain_fault_mo()
        if managed_objects is None:
            return None

        self.bridge_domain_fault = []

        for managed_object in managed_objects:
            fault_info = self.get_bridge_domain_fault_info(
                managed_object
            )
            self.bridge_domain_fault.append(
                fault_info
            )

        self.log.apic_mo(
            'fvBD.fault.info',
            self.bridge_domain_fault
        )

        return self.bridge_domain_fault

    def get_bridge_domain_fault_record(self, deduplicate=True):
        if self.bridge_domain_fault_record is not None:
            return self.bridge_domain_fault_record

        managed_objects = self.get_bridge_domain_fault_record_mo()
        if managed_objects is None:
            return None

        self.bridge_domain_fault_record = []
        fault_ids = []

        for managed_object in managed_objects:
            fault_info = self.get_bridge_domain_fault_info(
                managed_object
            )
            if not deduplicate or fault_info['id'] not in fault_ids:
                self.bridge_domain_fault_record.append(
                    fault_info
                )
                fault_ids.append(
                    fault_info['id']
                )

        self.log.apic_mo(
            'fvBD.faultRecord.info',
            self.bridge_domain_fault_record
        )

        return self.bridge_domain_fault_record

    def get_bridge_domain_id_fault(self, tenant_name, bd_name, fault_object, fault_filter=None):
        faults = []

        if fault_object == 'faultInst':
            all_faults = self.get_bridge_domain_fault()
            if all_faults is None:
                return faults

            fault_filter = self.remove_system_fault_timestamp_filter(
                fault_filter
            )

        if fault_object == 'faultRecord':
            all_faults = self.get_bridge_domain_fault_record()
            if all_faults is None:
                return faults

        for fault_info in all_faults:
            if fault_info['tenantName'] is not None and fault_info['bdName'] is not None:
                if fault_info['tenantName'] == tenant_name and fault_info['bdName'] == bd_name:
                    if not self.match_system_fault(fault_info, fault_filter, exclude_cleared=False):
                        continue

                    faults.append(
                        fault_info
                    )

        return faults
