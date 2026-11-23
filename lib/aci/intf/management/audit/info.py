import time
from datetime import datetime

from lib import filter_helper


class InterfaceMgmtAuditInfo():
    def __init__(self):
        self.interface_management_audit = {}

    def get_interface_management_audit_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['interfaceId'] = None
        if '/mgmt-[' in info['affected']:
            info['interfaceId'] = info['affected'].split('/mgmt-[')[1].split(']')[0]

        info['descrT'] = filter_helper.get_string_chunks(
            filter_helper.sanitize_string(
                info['descr']
            ),
            80
        )

        info['changeSetT'] = filter_helper.get_string_chunks(
            filter_helper.sanitize_string(
                info['changeSet']
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

    def get_interface_management_audit(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_management_audit:
            return self.interface_management_audit[key]

        managed_objects = self.get_interface_management_audit_mo(
            pod_id,
            node_id
        )
        if managed_objects is None:
            return None

        self.interface_management_audit[key] = []
        for managed_object in managed_objects:
            audit_info = self.get_interface_management_audit_info(
                managed_object
            )
            self.interface_management_audit[key].append(
                audit_info
            )

        self.log.apic_mo(
            'mgmtMgmtIf.auditRecord.info.%s' % (key),
            self.interface_management_audit[key]
        )

        return self.interface_management_audit[key]

    def get_interface_management_id_audit(self, pod_id, node_id, interface_id, audit_filter=None):
        audits = []

        all_audits = self.get_interface_management_audit(
            pod_id,
            node_id
        )
        if all_audits is None:
            return audits

        for audit_info in all_audits:
            if audit_info['interfaceId'] is not None:
                if audit_info['interfaceId'] == interface_id:
                    if not self.match_system_fault(audit_info, audit_filter):
                        continue

                    audits.append(
                        audit_info
                    )

        return audits
