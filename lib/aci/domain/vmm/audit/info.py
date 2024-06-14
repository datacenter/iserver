import time
from datetime import datetime

from lib import filter_helper


class DomainVmmAuditInfo():
    def __init__(self):
        self.domain_vmm_audit = None

    def get_domain_vmm_audit_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['domainName'] = None
        if 'uni/vmmp-VMware/dom-' in info['affected']:
            info['domainName'] = info['affected'].split('uni/vmmp-VMware/dom-')[1].split('/')[0]

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

    def get_domain_vmm_audit(self):
        if self.domain_vmm_audit is not None:
            return self.domain_vmm_audit

        managed_objects = self.get_domain_vmm_audit_mo()
        if managed_objects is None:
            return None

        self.domain_vmm_audit = []
        for managed_object in managed_objects:
            audit_info = self.get_domain_vmm_audit_info(
                managed_object
            )
            self.domain_vmm_audit.append(
                audit_info
            )

        self.log.apic_mo(
            'vmmDomP.auditRecord.info',
            self.domain_vmm_audit
        )

        return self.domain_vmm_audit

    def get_domain_vmm_id_audit(self, domain_name, audit_filter=None):
        audits = []

        all_audits = self.get_domain_vmm_audit()
        if all_audits is None:
            return audits

        for audit_info in all_audits:
            if audit_info['domainName'] is not None:
                if audit_info['domainName'] == domain_name:
                    if not self.match_system_fault(audit_info, audit_filter, exclude_cleared=False):
                        continue

                    audits.append(
                        audit_info
                    )

        return audits
