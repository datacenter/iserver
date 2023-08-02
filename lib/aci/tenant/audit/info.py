import time
from datetime import datetime

from lib import filter_helper


class TenantAuditInfo():
    def __init__(self):
        self.tenant_audit = None

    def get_tenant_audit_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['tenantName'] = None

        if 'uni/tn-' in info['affected']:
            info['tenantName'] = info['affected'].split('uni/tn-')[1].split('/')[0]

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

    def get_tenant_audit(self):
        if self.tenant_audit is not None:
            return self.tenant_audit

        managed_objects = self.get_tenant_audit_mo()
        if managed_objects is None:
            return None

        self.tenant_audit = []
        for managed_object in managed_objects:
            audit_info = self.get_tenant_audit_info(
                managed_object
            )
            self.tenant_audit.append(
                audit_info
            )

        self.log.apic_mo(
            'fvTenant.auditRecord.info',
            self.tenant_audit
        )

        return self.tenant_audit

    def get_tenant_id_audit(self, tenant_name, audit_filter=None):
        audits = []

        all_audits = self.get_tenant_audit()
        if all_audits is None:
            return audits

        for audit_info in all_audits:
            if audit_info['tenantName'] is not None:
                if audit_info['tenantName'] == tenant_name:
                    if not self.match_system_fault(audit_info, audit_filter, exclude_cleared=False):
                        continue

                    audits.append(
                        audit_info
                    )

        return audits
