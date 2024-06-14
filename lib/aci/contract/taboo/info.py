from lib import filter_helper


class ContractTabooInfo():
    def __init__(self):
        self.taboo_contract = None

    def get_taboo_contract_count(self, tenant_name=None):
        taboo_filter = None
        if tenant_name is not None:
            taboo_filter = ['tenant:%s' % (tenant_name)]

        contracts = self.get_taboo_contracts(
            taboo_filter=taboo_filter
        )
        return len(contracts)

    def get_taboo_contract(self, tenant, name):
        taboo_filter = []
        taboo_filter.append(
            'tenant:%s' % (tenant)
        )
        taboo_filter.append(
            'name:%s' % (name)
        )

        taboos = self.get_taboo_contracts(
            taboo_filter=taboo_filter
        )

        if len(taboos) == 1:
            return taboos[0]

        return None

    def get_taboo_contract_filters_info(self, managed_object):
        info = []
        for item in managed_object['vzTSubj']:
            taboo_subject_name = item['name']
            taboo_subject_tenant = managed_object['dn'].split('/')[1][3:]
            taboo_subject_info = self.get_taboo_contract_subject(
                taboo_subject_tenant,
                taboo_subject_name
            )
            if taboo_subject_info is None:
                continue

            for taboo_filter_name in taboo_subject_info['vzFilterName']:
                filter_info = self.get_contract_filter(
                    taboo_subject_tenant,
                    taboo_filter_name
                )
                if filter_info is None:
                    self.log.error(
                        'get_taboo_contract_filters_info',
                        'Filter not found: %s/%s' % (
                            taboo_subject_tenant,
                            taboo_filter_name
                        )
                    )
                    continue

                filter_info['subjectName'] = taboo_subject_name
                filter_info['subjectTenant'] = taboo_subject_tenant
                filter_info['subjectNameTenant'] = '%s/%s' % (
                    taboo_subject_tenant,
                    taboo_subject_name
                )
                info.append(
                    filter_info
                )

        return info

    def get_taboo_taboo_info(self, managed_object):
        keys = [
            'descr',
            'dn',
            'name',
            'reevaluateAll',
            'scope',
            'status',
            'userdom'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['tenant'] = info['dn'].split('/')[1][3:]
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        info['vzFilter'] = self.get_taboo_contract_filters_info(
            managed_object
        )

        info['protectedEpg'] = []
        for item in managed_object['vzRtProtBy']:
            contract_epg_info = self.get_standard_contract_epg_info(
                item
            )
            if contract_epg_info is not None:
                info['protectedEpg'].append(
                    contract_epg_info
                )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_taboo_contracts_info(self):
        if self.taboo_contract is None:
            self.taboo_contract = []

            taboos = self.get_taboo_contract_mo()
            if taboos is not None:
                for managed_object in taboos:
                    self.taboo_contract.append(
                        self.get_taboo_taboo_info(
                            managed_object
                        )
                    )

        return self.taboo_contract

    def match_taboo_contract(self, taboo_info, taboo_filter):
        if taboo_filter is None or len(taboo_filter) == 0:
            return True

        for taboo_rule in taboo_filter:
            (key, value) = taboo_rule.split(':')
            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_tenant_name(value, taboo_info['nameTenant']):
                    return False

            if key == 'names':
                key_found = True
                found = False
                for name in value.split(','):
                    if filter_helper.match_tenant_name(name, taboo_info['nameTenant']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'tenant':
                key_found = True
                if not filter_helper.match_string(value, taboo_info['tenant']):
                    return False

            if key == 'filter':
                key_found = True
                found = False
                for filter_info in taboo_info['vzFilter']:
                    if filter_helper.match_tenant_name(value, filter_info['nameTenant']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'fault':
                key_found = True
                if value == 'any':
                    if not taboo_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_taboo_contract',
                        'Unsupported fault filtering value: %s' % (value)
                    )

            if not key_found:
                self.log.error(
                    'match_taboo_contract',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_taboo_contracts(
            self,
            taboo_filter=None,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_taboos = self.get_taboo_contracts_info()
        if all_taboos is None:
            return None

        taboos = []

        for taboo_info in all_taboos:
            if not self.match_taboo_contract(taboo_info, taboo_filter):
                continue

            if fault_info:
                taboo_info['faultInst'] = self.get_taboo_contract_id_fault(
                    taboo_info['tenant'],
                    taboo_info['name'],
                    'faultInst'
                )

            if hfault_info:
                taboo_info['faultRecord'] = self.get_taboo_contract_id_fault(
                    taboo_info['tenant'],
                    taboo_info['name'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                taboo_info['eventLog'] = self.get_taboo_contract_id_event(
                    taboo_info['tenant'],
                    taboo_info['name'],
                    event_filter=event_filter
                )

            if audit_info:
                taboo_info['auditLog'] = self.get_taboo_contract_id_audit(
                    taboo_info['tenant'],
                    taboo_info['name'],
                    audit_filter=audit_filter
                )

            taboos.append(taboo_info)

        taboos = sorted(
            taboos,
            key=lambda i: i['name'].lower()
        )

        self.log.apic_mo(
            'vzTaboo.info',
            taboos
        )

        return taboos
