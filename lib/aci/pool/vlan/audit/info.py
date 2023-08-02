import time
from datetime import datetime

from lib import filter_helper


class PoolVlanAuditInfo():
    def __init__(self):
        self.pool_vlan_audit = None

    def get_pool_vlan_audit_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['poolName'] = None

        if 'uni/infra/vlanns-[' in info['affected']:
            info['poolName'] = info['affected'].split('uni/infra/vlanns-[')[1].split(']')[0]

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

    def get_pool_vlan_audit(self):
        if self.pool_vlan_audit is not None:
            return self.pool_vlan_audit

        managed_objects = self.get_pool_vlan_audit_mo()
        if managed_objects is None:
            return None

        self.pool_vlan_audit = []
        for managed_object in managed_objects:
            audit_info = self.get_pool_vlan_audit_info(
                managed_object
            )
            self.pool_vlan_audit.append(
                audit_info
            )

        self.log.apic_mo(
            'fvnsVlanInstP.auditRecord.info',
            self.pool_vlan_audit
        )

        return self.pool_vlan_audit

    def get_pool_vlan_id_audit(self, pool_name, audit_filter=None):
        audits = []

        all_audits = self.get_pool_vlan_audit()
        if all_audits is None:
            return audits

        for audit_info in all_audits:
            if audit_info['poolName'] is not None:
                if audit_info['poolName'] == pool_name:
                    if not self.match_system_fault(audit_info, audit_filter, exclude_cleared=False):
                        continue

                    audits.append(
                        audit_info
                    )

        return audits
