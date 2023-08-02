import time
from datetime import datetime

from lib import filter_helper


class PolicyGroupAccessInterfaceVpcFaultInfo():
    def __init__(self):
        self.policy_group_access_interface_vpc_fault = None
        self.policy_group_access_interface_vpc_fault_record = None

    def get_policy_group_access_interface_vpc_fault_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        # "affected": "uni/infra/funcprof/accbundle-ESX-R7DC_PolGrp/rsqosDppIfPol"
        info['pgName'] = None
        if not managed_object['delegated']:
            if 'uni/infra/funcprof/accbundle-' in info['affected']:
                info['pgName'] = info['affected'].split('uni/infra/funcprof/accbundle-')[1].split('/')[0]

        if info['pgName'] is None:
            if 'uni/infra/funcprof/accbundle-' in info['dn']:
                info['pgName'] = info['dn'].split('uni/infra/funcprof/accbundle-')[1].split('/')[0]

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

    def get_policy_group_access_interface_vpc_fault(self):
        if self.policy_group_access_interface_vpc_fault is not None:
            return self.policy_group_access_interface_vpc_fault

        managed_objects = self.get_policy_group_access_interface_vpc_fault_mo()
        if managed_objects is None:
            return None

        self.policy_group_access_interface_vpc_fault = []
        fault_ids = []

        for managed_object in managed_objects:
            fault_info = self.get_policy_group_access_interface_vpc_fault_info(
                managed_object
            )
            self.policy_group_access_interface_vpc_fault.append(
                fault_info
            )

        self.log.apic_mo(
            'infraAccBndlGrp.fault.info',
            self.policy_group_access_interface_vpc_fault
        )

        return self.policy_group_access_interface_vpc_fault

    def get_policy_group_access_interface_vpc_fault_record(self, deduplicate=True):
        if self.policy_group_access_interface_vpc_fault_record is not None:
            return self.policy_group_access_interface_vpc_fault_record

        managed_objects = self.get_policy_group_access_interface_vpc_fault_record_mo()
        if managed_objects is None:
            return None

        self.policy_group_access_interface_vpc_fault_record = []
        fault_ids = []

        for managed_object in managed_objects:
            fault_info = self.get_policy_group_access_interface_vpc_fault_info(
                managed_object
            )
            if not deduplicate or fault_info['id'] not in fault_ids:
                self.policy_group_access_interface_vpc_fault_record.append(
                    fault_info
                )
                fault_ids.append(
                    fault_info['id']
                )

        self.log.apic_mo(
            'infraAccBndlGrp.faultRecord.info',
            self.policy_group_access_interface_vpc_fault_record
        )

        return self.policy_group_access_interface_vpc_fault_record

    def get_policy_group_access_interface_vpc_id_fault(self, pg_name, fault_object, fault_filter=None):
        faults = []

        if fault_object == 'faultInst':
            all_faults = self.get_policy_group_access_interface_vpc_fault()
            if all_faults is None:
                return faults

            fault_filter = self.remove_system_fault_timestamp_filter(
                fault_filter
            )

        if fault_object == 'faultRecord':
            all_faults = self.get_policy_group_access_interface_vpc_fault_record()
            if all_faults is None:
                return faults

        for fault_info in all_faults:
            if fault_info['pgName'] is not None:
                if fault_info['pgName'] == pg_name:
                    if not self.match_system_fault(fault_info, fault_filter, exclude_cleared=False):
                        continue

                    faults.append(
                        fault_info
                    )

        return faults
