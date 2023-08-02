import time
from datetime import datetime

from lib import filter_helper


class PolicyGeneralAaeAuditInfo():
    def __init__(self):
        self.policy_global_aae_audit = None

    def get_policy_global_aae_audit_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        # uni/infra/attentp-HX1_AAEP/rsdomP-[uni/phys-HX1_PhysDom]
        info['policyName'] = None
        if 'uni/infra/attentp-' in info['affected']:
            info['policyName'] = info['affected'].split('uni/infra/attentp-')[1].split('/')[0]

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

    def get_policy_global_aae_audit(self):
        if self.policy_global_aae_audit is not None:
            return self.policy_global_aae_audit

        managed_objects = self.get_policy_global_aae_audit_mo()
        if managed_objects is None:
            return None

        self.policy_global_aae_audit = []
        for managed_object in managed_objects:
            audit_info = self.get_policy_global_aae_audit_info(
                managed_object
            )
            self.policy_global_aae_audit.append(
                audit_info
            )

        self.log.apic_mo(
            'infraAttEntityP.auditRecord.info',
            self.policy_global_aae_audit
        )

        return self.policy_global_aae_audit

    def get_policy_global_aae_id_audit(self, policy_name, audit_filter=None):
        audits = []

        all_audits = self.get_policy_global_aae_audit()
        if all_audits is None:
            return audits

        for audit_info in all_audits:
            if audit_info['policyName'] is not None:
                if audit_info['policyName'] == policy_name:
                    if not self.match_system_fault(audit_info, audit_filter, exclude_cleared=False):
                        continue

                    audits.append(
                        audit_info
                    )

        return audits
