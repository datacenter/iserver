import time
from datetime import datetime

from lib import filter_helper


class ContractFilterAuditInfo():
    def __init__(self):
        self.filter_contract_audit = None

    def get_filter_contract_audit_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['tenantName'] = None
        info['filterName'] = None

        if 'uni/tn-' in info['affected']:
            # uni/tn-k8s/filter-BT-Demo
            info['tenantName'] = info['affected'].split('uni/tn-')[1].split('/')[0]

        if '/flt-' in info['affected']:
            info['filterName'] = info['affected'].split('/flt-')[1].split('/')[0]

        info['nameTenant'] = '--'
        if info['tenantName'] is not None and info['filterName'] is not None:
            info['nameTenant'] = '%s/%s' % (
                info['tenantName'],
                info['filterName']
            )

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

    def get_filter_contract_audit(self):
        if self.filter_contract_audit is not None:
            return self.filter_contract_audit

        managed_objects = self.get_filter_contract_audit_mo()
        if managed_objects is None:
            return None

        self.filter_contract_audit = []
        for managed_object in managed_objects:
            audit_info = self.get_filter_contract_audit_info(
                managed_object
            )
            self.filter_contract_audit.append(
                audit_info
            )

        self.log.apic_mo(
            'vzFilter.auditRecord.info',
            self.filter_contract_audit
        )

        return self.filter_contract_audit

    def get_filter_contract_id_audit(self, tenant_name, filter_name, audit_filter=None):
        audits = []

        all_audits = self.get_filter_contract_audit()
        if all_audits is None:
            return audits

        for audit_info in all_audits:
            if audit_info['tenantName'] is not None and audit_info['filterName'] is not None:
                if audit_info['tenantName'] == tenant_name and audit_info['filterName'] == filter_name:
                    if not self.match_system_fault(audit_info, audit_filter, exclude_cleared=False):
                        continue

                    audits.append(
                        audit_info
                    )

        return audits
