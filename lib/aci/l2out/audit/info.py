import time
from datetime import datetime

from lib import filter_helper


class L2OutAuditInfo():
    def __init__(self):
        self.l2out_audit = None

    def get_l2out_audit_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['tenantName'] = None
        info['l2outName'] = None

        if 'uni/tn-' in info['affected']:
            # uni/tn-k8s/l2out-Test
            info['tenantName'] = info['affected'].split('uni/tn-')[1].split('/')[0]

        if '/l2out-' in info['affected']:
            info['l2outName'] = info['affected'].split('/l2out-')[1].split('/')[0]

        info['nameTenant'] = '--'
        if info['tenantName'] is not None and info['l2outName'] is not None:
            info['nameTenant'] = '%s/%s' % (
                info['tenantName'],
                info['l2outName']
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

    def get_l2out_audit(self):
        if self.l2out_audit is not None:
            return self.l2out_audit

        managed_objects = self.get_l2out_audit_mo()
        if managed_objects is None:
            return None

        self.l2out_audit = []
        for managed_object in managed_objects:
            audit_info = self.get_l2out_audit_info(
                managed_object
            )
            self.l2out_audit.append(
                audit_info
            )

        self.log.apic_mo(
            'l2extOut.auditRecord.info',
            self.l2out_audit
        )

        return self.l2out_audit

    def get_l2out_id_audit(self, tenant_name, l2out_name, audit_filter=None):
        audits = []

        all_audits = self.get_l2out_audit()
        if all_audits is None:
            return audits

        for audit_info in all_audits:
            if audit_info['tenantName'] is not None and audit_info['l2outName'] is not None:
                if audit_info['tenantName'] == tenant_name and audit_info['l2outName'] == l2out_name:
                    if not self.match_system_fault(audit_info, audit_filter, exclude_cleared=False):
                        continue

                    audits.append(
                        audit_info
                    )

        return audits
