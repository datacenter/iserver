import time
from datetime import datetime

from lib import filter_helper


class EpgAuditInfo():
    def __init__(self):
        self.epg_audit = None

    def get_epg_audit_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['tenantName'] = None
        info['apName'] = None
        info['epgName'] = None

        if 'uni/tn-' in info['affected']:
            # uni/tn-k8s/ap-k8s_ANP/epg-bmk8s_prov
            info['tenantName'] = info['affected'].split('uni/tn-')[1].split('/')[0]

        if '/ap-' in info['affected']:
            info['apName'] = info['affected'].split('/ap-')[1].split('/')[0]

        if '/epg-' in info['affected']:
            info['epgName'] = info['affected'].split('/epg-')[1].split('/')[0]

        info['nameApTenant'] = '--'
        if info['tenantName'] is not None and info['apName'] is not None and info['epgName'] is not None:
            info['nameApTenant'] = '%s/%s/%s' % (
                info['tenantName'],
                info['apName'],
                info['epgName']
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

    def get_epg_audit(self):
        if self.epg_audit is not None:
            return self.epg_audit

        managed_objects = self.get_epg_audit_mo()
        if managed_objects is None:
            return None

        self.epg_audit = []
        for managed_object in managed_objects:
            audit_info = self.get_epg_audit_info(
                managed_object
            )
            self.epg_audit.append(
                audit_info
            )

        self.log.apic_mo(
            'fvAEPg.auditRecord.info',
            self.epg_audit
        )

        return self.epg_audit

    def get_epg_id_audit(self, tenant_name, ap_name, epg_name, audit_filter=None):
        audits = []

        all_audits = self.get_epg_audit()
        if all_audits is None:
            return audits

        for audit_info in all_audits:
            if audit_info['tenantName'] is not None and audit_info['apName'] is not None and audit_info['epgName'] is not None:
                if audit_info['tenantName'] == tenant_name and audit_info['apName'] == ap_name and audit_info['epgName'] == epg_name:
                    if not self.match_system_fault(audit_info, audit_filter, exclude_cleared=False):
                        continue

                    audits.append(
                        audit_info
                    )

        return audits
