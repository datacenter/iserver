import time
from datetime import datetime

from lib import filter_helper


class DomainVmmFaultInfo():
    def __init__(self):
        self.domain_vmm_fault = None
        self.domain_vmm_fault_record = None

    def get_domain_vmm_fault_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['domainName'] = None
        info['controllerName'] = None

        if not managed_object['delegated']:
            # "uni/vmmp-VMware/dom-EU-SPDC-CDC-22/ctrlr-EU-SPDC-CDC-22"
            if 'affected' in info:
                if 'uni/vmmp-VMware/dom-' in info['affected']:
                    info['domainName'] = info['affected'].split('uni/vmmp-VMware/dom-')[1].split('/')[0]
                    if len(info['affected'].split('/')) == 4:
                        info['controllerName'] = info['affected'].split('uni/vmmp-VMware/dom-')[1].split('/')[1][6:]

        # "dn": "uni/vmmp-VMware/dom-EU-SPDC-CDC-22/ctrlr-EU-SPDC-CDC-22/fd-[comp/prov-VMware/ctrlr-[EU-SPDC-CDC-22]-EU-SPDC-CDC-22/hv-host-3381]-fault-F2840"
        if info['domainName'] is None:
            if 'uni/vmmp-VMware/dom-' in info['dn']:
                info['domainName'] = info['dn'].split('uni/vmmp-VMware/dom-')[1].split('/')[0]
                info['controllerName'] = info['dn'].split('uni/vmmp-VMware/dom-')[1].split('/')[1][6:]

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

    def get_domain_vmm_fault(self):
        if self.domain_vmm_fault is not None:
            return self.domain_vmm_fault

        managed_objects = self.get_domain_vmm_fault_mo()
        if managed_objects is None:
            return None

        self.domain_vmm_fault = []
        for managed_object in managed_objects:
            fault_info = self.get_domain_vmm_fault_info(
                managed_object
            )
            self.domain_vmm_fault.append(
                fault_info
            )

        self.log.apic_mo(
            'vmmDomP.fault.info',
            self.domain_vmm_fault
        )

        return self.domain_vmm_fault

    def get_domain_vmm_fault_record(self, deduplicate=True):
        if self.domain_vmm_fault_record is not None:
            return self.domain_vmm_fault_record

        managed_objects = self.get_domain_vmm_fault_record_mo()
        if managed_objects is None:
            return None

        self.domain_vmm_fault_record = []
        fault_ids = []

        for managed_object in managed_objects:
            fault_info = self.get_domain_vmm_fault_info(
                managed_object
            )
            if not deduplicate or fault_info['id'] not in fault_ids:
                self.domain_vmm_fault_record.append(
                    fault_info
                )
                fault_ids.append(
                    fault_info['id']
                )

        self.log.apic_mo(
            'vmmDomP.faultRecord.info',
            self.domain_vmm_fault_record
        )

        return self.domain_vmm_fault_record

    def get_domain_vmm_id_fault(self, domain_name, fault_object, fault_filter=None):
        faults = []

        if fault_object == 'faultInst':
            all_faults = self.get_domain_vmm_fault()
            if all_faults is None:
                return faults

            fault_filter = self.remove_system_fault_timestamp_filter(
                fault_filter
            )

        if fault_object == 'faultRecord':
            all_faults = self.get_domain_vmm_fault_record()
            if all_faults is None:
                return faults

        for fault_info in all_faults:
            if fault_info['domainName'] is not None:
                if fault_info['domainName'] == domain_name:
                    if not self.match_system_fault(fault_info, fault_filter, exclude_cleared=False):
                        continue

                    faults.append(
                        fault_info
                    )

        return faults
