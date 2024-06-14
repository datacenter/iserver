import time
from datetime import datetime

from lib import filter_helper


class SystemFaultInfo():
    def __init__(self):
        self.system_fault = None

        self.system_fault_type = {}
        self.system_fault_type['environmental'] = 'Environmental'
        self.system_fault_type['communications'] = 'Communications'
        self.system_fault_type['config'] = 'Config'
        self.system_fault_type['operational'] = 'Operational'
        self.system_fault_type['total'] = 'Total'

        self.system_fault_domain = {}
        self.system_fault_domain['access'] = 'Access'
        self.system_fault_domain['apps'] = 'Apps'
        self.system_fault_domain['external'] = 'External'
        self.system_fault_domain['framework'] = 'Framework'
        self.system_fault_domain['infra'] = 'Infra'
        self.system_fault_domain['management'] = 'Management'
        self.system_fault_domain['security'] = 'Security'
        self.system_fault_domain['tenant'] = 'Tenant'
        self.system_fault_domain['total'] = 'Total'

        self.system_fault_severity_name = {}
        self.system_fault_severity_name['critical'] = 'Crit'
        self.system_fault_severity_name['major'] = 'Maj'
        self.system_fault_severity_name['minor'] = 'Min'
        self.system_fault_severity_name['warning'] = 'Warn'
        self.system_fault_severity_name['info'] = 'Info'
        self.system_fault_severity_name['cleared'] = '--'

        self.system_fault_severity_color = {}
        self.system_fault_severity_color['critical'] = 'Red'
        self.system_fault_severity_color['major'] = 'Magenta'
        self.system_fault_severity_color['minor'] = 'Yellow'
        self.system_fault_severity_color['warning'] = 'Green'
        self.system_fault_severity_color['cleared'] = 'Blue'
        self.system_fault_severity_color['info'] = 'Blue'

    def get_system_faults_max_severity(self, faults):
        if faults is None or len(faults) == 0:
            return None

        severity = None
        for fault in faults:
            if severity is None:
                severity = fault['severity']
                continue

            if severity == 'warning':
                severity = fault['severity']
                continue

            if severity == 'minor':
                if fault['severity'] == 'major':
                    severity = fault['severity']
                    continue

        return severity

    def get_system_fault_scope_tenant_epg_dn(self, managed_object):
        scope = {}

        if 'uni/epp/br-[' in managed_object['dn']:
            scope['epgDn'] = managed_object['dn'].split('uni/epp/br-[')[1].split(']')[0]
            scope['epgType'] = 'l2out'
            if len(scope['epgDn'].split('/')) != 3:
                scope['reason'] = 'Unexpected l2out dn structure'
                return scope

            # "dn": "uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg"
            scope['tenant'] = scope['epgDn'].split('/')[1][3:]
            scope['l2outName'] = scope['epgDn'].split('/')[2][6:]
            scope['epgName'] = scope['epgDn'].split('/')[3][6:]
            scope['resolved'] = True
            return scope

        if 'uni/epp/fv-[' in managed_object['dn']:
            scope['epgDn'] = managed_object['dn'].split('uni/epp/fv-[')[1].split(']')[0]
            scope['epgType'] = 'aepg'
            if len(scope['epgDn'].split('/')) != 4:
                scope['reason'] = 'Unexpected l2out dn structure'
                return scope

            # "dn": "uni/epp/fv-[uni/tn-common/ap-privIP_TEST/epg-privIP_TEST]/node-301/polDelSt/fault-F1298"
            scope['tenant'] = scope['epgDn'].split('/')[1][3:]
            scope['application_profile'] = scope['epgDn'].split('/')[2][3:]
            scope['name'] = scope['epgDn'].split('/')[3][4:]
            scope['nameApTenant'] = '%s/%s/%s' % (
                scope['tenant'],
                scope['application_profile'],
                scope['name']
            )
            scope['resolved'] = True
            return scope

        scope['reason'] = 'Unsupported epg dn'
        return scope

    def get_system_fault_scope_tenant_epg(self, managed_object):
        scope = {}
        scope['domain'] = managed_object['domain']
        scope['subject'] = managed_object['subject']
        scope['resolved'] = False
        scope['reason'] = ''
        scope.update(
            self.get_system_fault_scope_tenant_epg_dn(
                managed_object
            )
        )
        return scope

    def get_system_fault_scope_tenant_management(self, managed_object):
        scope = {}
        scope['domain'] = managed_object['domain']
        scope['subject'] = managed_object['subject']
        scope['resolved'] = False
        scope['reason'] = ''
        scope.update(
            self.get_system_fault_scope_tenant_epg_dn(
                managed_object
            )
        )

        return scope

    def get_system_fault_scope_tenant(self, managed_object):
        if managed_object['subject'] == 'epg':
            scope = self.get_system_fault_scope_tenant_epg(managed_object)
            return scope

        if managed_object['subject'] == 'management':
            scope = self.get_system_fault_scope_tenant_management(managed_object)
            return scope

        scope = {}
        scope['domain'] = managed_object['domain']
        scope['subject'] = managed_object['subject']
        scope['resolved'] = False
        scope['reason'] = 'Unsupported tenant subject: %s' % (managed_object['subject'])

        return scope

    def get_system_fault_scope_external(self, managed_object):
        scope = {}
        scope['resolved'] = False
        scope['reason'] = 'Not implemented'
        scope['domain'] = managed_object['domain']
        return scope

    def get_system_fault_scope_infra(self, managed_object):
        scope = {}
        scope['resolved'] = False
        scope['reason'] = 'Not implemented'
        scope['domain'] = managed_object['domain']
        return scope

    def get_system_fault_scope_framework(self, managed_object):
        scope = {}
        scope['resolved'] = False
        scope['reason'] = 'Not implemented'
        scope['domain'] = managed_object['domain']
        return scope

    def get_system_fault_scope_access(self, managed_object):
        scope = {}
        scope['resolved'] = False
        scope['reason'] = 'Not implemented'
        scope['domain'] = managed_object['domain']
        return scope

    def get_system_fault_scope(self, managed_object):
        if managed_object['domain'] == 'tenant':
            scope = self.get_system_fault_scope_tenant(managed_object)
            return scope

        if managed_object['domain'] == 'infra':
            scope = self.get_system_fault_scope_infra(managed_object)
            return scope

        if managed_object['domain'] == 'access':
            scope = self.get_system_fault_scope_access(managed_object)
            return scope

        if managed_object['domain'] == 'framework':
            scope = self.get_system_fault_scope_framework(managed_object)
            return scope

        if managed_object['domain'] == 'external':
            scope = self.get_system_fault_scope_external(managed_object)
            return scope

        scope = {}
        scope['resolved'] = False
        scope['reason'] = 'Unsupported domain: %s' % (managed_object['domain'])
        scope['domain'] = managed_object['domain']

        return scope

    def get_system_fault_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['codeInt'] = int(info['code'][1:])
        info['codeT'] = info['code']
        if info['code'] in self.system_fault_code:
            info['codeT'] = self.system_fault_code[info['code']]

        info['count'] = int(info['occur'])

        info['severityT'] = self.system_fault_severity_name[info['severity']]
        info['__Output']['severityT'] = self.system_fault_severity_color[info['severity']]

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

        # info['scope'] = self.get_system_fault_scope(
        #     managed_object
        # )

        # "2022-04-29T13:32:45.167+02:00"
        info['timestamp'] = int(
            time.mktime(
                datetime.strptime(
                    info['created'],
                    '%Y-%m-%dT%H:%M:%S.%f%z'
                ).timetuple()
            )
        )

        return info

    def get_system_faults_info(self):
        if self.system_fault is not None:
            return self.system_fault

        managed_objects = self.get_system_fault_mo()
        if managed_objects is None:
            return None

        self.system_fault = []
        for managed_object in managed_objects:
            self.system_fault.append(
                self.get_system_fault_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'faultInst.info',
            self.system_fault
        )

        return self.system_fault

    def remove_system_fault_timestamp_filter(self, system_fault_filter):
        if system_fault_filter is None:
            return None

        new_filter = []
        for rule in system_fault_filter:
            (key, value) = rule.split(':')
            if key == 'timestamp':
                continue
            new_filter.append(
                rule
            )

        return new_filter

    def match_system_fault(self, system_fault_info, system_fault_filter, exclude_cleared=True):
        if exclude_cleared:
            if system_fault_info['severity'] == 'cleared':
                return False

        if system_fault_filter is None or len(system_fault_filter) == 0:
            return True

        for aepg_rule in system_fault_filter:
            (key, value) = aepg_rule.split(':')
            found = False

            if key == 'epg':
                found = True
                if not system_fault_info['scope']['resolved']:
                    return False

                if system_fault_info['scope']['domain'] != 'tenant':
                    return False

                if system_fault_info['scope']['subject'] != 'epg':
                    return False

                if system_fault_info['scope']['epgType'] != 'aepg':
                    return False

                if not filter_helper.match_tenant_ap_name(value, system_fault_info['scope']['nameApTenant']):
                    return False

            if key == 'severity':
                found = True
                if not filter_helper.match_string(value, system_fault_info['severity']):
                    return False

            if key == 'domain':
                found = True
                if not filter_helper.match_string(value, system_fault_info['domain']):
                    return False

            if key == 'type':
                found = True
                if not filter_helper.match_string(value, system_fault_info['type']):
                    return False

            if key == 'code':
                found = True
                matched = False

                if value.startswith('gt'):
                    if not filter_helper.match_integer(value, system_fault_info['codeInt']):
                        return False
                    matched = True

                if value.startswith('ge'):
                    if not filter_helper.match_integer(value, system_fault_info['codeInt']):
                        return False
                    matched = True

                if value.startswith('lt'):
                    if not filter_helper.match_integer(value, system_fault_info['codeInt']):
                        return False
                    matched = True

                if value.startswith('le'):
                    if not filter_helper.match_integer(value, system_fault_info['codeInt']):
                        return False
                    matched = True

                if '-' in value:
                    if not filter_helper.match_integer(value, system_fault_info['codeInt']):
                        return False
                    matched = True

                if not matched:
                    if not filter_helper.match_string(value, system_fault_info['code']):
                        return False

            if key == 'timestamp':
                found = True
                if not filter_helper.match_timestamp(value, system_fault_info['timestamp']):
                    return False

            if key == 'dn':
                found = True
                if not filter_helper.match_string(value, system_fault_info['dn']):
                    return False

            if key == 'cause':
                found = True
                if not filter_helper.match_string(value, system_fault_info['cause']):
                    return False

            if key == 'description':
                found = True
                if not filter_helper.match_string(value, system_fault_info['descr']):
                    return False

            if not found:
                if key in system_fault_info:
                    found = True
                    if not filter_helper.match_string(value, system_fault_info[key]):
                        return False

            if not found:
                self.log.error(
                    'match_system_fault',
                    'Unsupported filtering key: %s' % (key)
                )

        return True

    def get_system_faults(self, system_fault_filter=None):
        all_system_faults = self.get_system_faults_info()
        if all_system_faults is None:
            return None

        system_faults = []

        for system_fault_info in all_system_faults:
            if not self.match_system_fault(system_fault_info, system_fault_filter):
                continue

            system_faults.append(
                system_fault_info
            )

        system_faults = sorted(
            system_faults,
            key=lambda i: i['severity'].lower()
        )

        return system_faults

    def get_system_faults_summary(self, system_fault_filter=None):
        all_system_faults = self.get_system_faults_info()
        if all_system_faults is None:
            return None

        system_faults = []

        for system_fault_info in all_system_faults:
            if not self.match_system_fault(system_fault_info, system_fault_filter):
                continue

            found = False
            for system_fault in system_faults:
                if system_fault['code'] == system_fault_info['code']:
                    system_fault['count'] = system_fault['count'] + system_fault_info['count']
                    found = True
                    break

            if found:
                continue

            system_faults.append(
                system_fault_info
            )

        system_faults = sorted(
            system_faults,
            key=lambda i: i['severity'].lower()
        )

        return system_faults

    def get_system_faults_domain_count(self, system_fault_filter=None):
        all_system_faults = self.get_system_faults_info()
        if all_system_faults is None:
            return None

        info = {}
        for fault_domain in self.system_fault_domain:
            info[fault_domain] = {}
            for fault_severity in self.system_fault_severity_name:
                info[fault_domain][fault_severity] = 0

        info['total'] = {}
        for fault_severity in self.system_fault_severity_name:
            info['total'][fault_severity] = 0

        for system_fault_info in all_system_faults:
            if not self.match_system_fault(system_fault_info, system_fault_filter):
                continue

            info[system_fault_info['domain']][system_fault_info['severity']] = info[system_fault_info['domain']][system_fault_info['severity']] + 1
            info['total'][system_fault_info['severity']] = info['total'][system_fault_info['severity']] + 1

        system_faults = []
        for item in info:
            entry = info[item]
            entry['domain'] = item
            entry['domainT'] = self.system_fault_domain[item]
            system_faults.append(
                entry
            )

        return system_faults

    def get_system_faults_type_count(self, system_fault_filter=None):
        all_system_faults = self.get_system_faults_info()
        if all_system_faults is None:
            return None

        info = {}
        for fault_type in self.system_fault_type:
            info[fault_type] = {}
            for fault_severity in self.system_fault_severity_name:
                info[fault_type][fault_severity] = 0

        info['total'] = {}
        for fault_severity in self.system_fault_severity_name:
            info['total'][fault_severity] = 0

        for system_fault_info in all_system_faults:
            if not self.match_system_fault(system_fault_info, system_fault_filter):
                continue

            info[system_fault_info['type']][system_fault_info['severity']] = info[system_fault_info['type']][system_fault_info['severity']] + 1
            info['total'][system_fault_info['severity']] = info['total'][system_fault_info['severity']] + 1

        system_faults = []
        for item in info:
            entry = info[item]
            entry['type'] = item
            entry['typeT'] = self.system_fault_type[item]
            system_faults.append(
                entry
            )

        return system_faults
