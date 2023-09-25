from lib import filter_helper


class ContractFilterInfo():
    def __init__(self):
        self.contract_filter = None

    def get_contract_filter_count(self, tenant_name=None):
        filter_filter = None
        if tenant_name is not None:
            filter_filter = ['tenant:%s' % (tenant_name)]

        filters = self.get_contract_filters(
            filter_filter=filter_filter
        )
        return len(filters)

    def get_contract_filter(self, tenant, name):
        filter_filter = []
        filter_filter.append(
            'tenant:%s' % (tenant)
        )
        filter_filter.append(
            'name:%s' % (name)
        )

        filters = self.get_contract_filters(
            filter_filter=filter_filter
        )

        if len(filters) == 1:
            return filters[0]

        return None

    def get_contract_filter_entry_info(self, managed_object):
        keys = [
            'applyToFrag',
            'arpOpc',
            'dFromPort',
            'dToPort',
            'descr',
            'etherT',
            'icmpv4T',
            'icmpv6T',
            'matchDscp',
            'name',
            'prot',
            'sFromPort',
            'sToPort',
            'stateful',
            'status',
            'tcpRules'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['source'] = ''
        if info['sFromPort'] != 'unspecified' and info['sToPort'] != 'unspecified':
            info['source'] = '%s - %s' % (
                info['sFromPort'],
                info['sToPort']
            )

        info['destination'] = ''
        if info['dFromPort'] != 'unspecified' and info['dToPort'] != 'unspecified':
            info['destination'] = '%s - %s' % (
                info['dFromPort'],
                info['dToPort']
            )

        for key in ['etherT', 'arpOpc', 'prot']:
            if info[key] == 'unspecified':
                info[key] = ''

        return info

    def get_contract_filter_info(self, managed_object):
        keys = [
            'descr',
            'dn',
            'name',
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

        info['vzEntry'] = []
        for entry_mo in managed_object['vzEntry']:
            info['vzEntry'].append(
                self.get_contract_filter_entry_info(
                    entry_mo
                )
            )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_contract_filters_info(self):
        if self.contract_filter is None:
            self.contract_filter = []

            filters = self.get_contract_filters_mo()
            if filters is not None:
                for managed_object in filters:
                    self.contract_filter.append(
                        self.get_contract_filter_info(
                            managed_object
                        )
                    )

        return self.contract_filter

    def match_contract_filter(self, filter_info, filter_filter):
        if filter_filter is None or len(filter_filter) == 0:
            return True

        for filter_rule in filter_filter:
            (key, value) = filter_rule.split(':')
            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_tenant_name(value, filter_info['nameTenant']):
                    return False

            if key == 'tenant':
                key_found = True
                if not filter_helper.match_string(value, filter_info['tenant']):
                    return False

            if key == 'fault':
                key_found = True
                if value == 'any':
                    if not filter_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_contract_filter',
                        'Unsupported fault filtering value: %s' % (value)
                    )

            if not key_found:
                self.log.error(
                    'match_contract_filter',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_contract_filter_usage_info(self, filter_info):
        filter_filter = ['filter:%s' % (filter_info['nameTenant'])]

        filter_info['taboo'] = []

        contracts = self.get_contract_filters(
            filter_filter=filter_filter
        )
        if contracts is not None:
            for contract in contracts:
                filter_info['taboo'].append(
                    contract['nameTenant']
                )

        filter_info['contract'] = []

        contracts = self.get_standard_contracts(
            contract_filter=filter_filter
        )
        if contracts is not None:
            for contract in contracts:
                filter_info['contract'].append(
                    contract['nameTenant']
                )

        return filter_info

    def get_contract_filters(
            self,
            filter_filter=None,
            usage_info=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_filters = self.get_contract_filters_info()
        if all_filters is None:
            return None

        filters = []

        for filter_info in all_filters:
            if not self.match_contract_filter(filter_info, filter_filter):
                continue

            if usage_info:
                filter_info = self.get_contract_filter_usage_info(filter_info)

            if fault_info:
                filter_info['faultInst'] = self.get_filter_contract_id_fault(
                    filter_info['tenant'],
                    filter_info['name'],
                    'faultInst'
                )

            if hfault_info:
                filter_info['faultRecord'] = self.get_filter_contract_id_fault(
                    filter_info['tenant'],
                    filter_info['name'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                filter_info['eventLog'] = self.get_filter_contract_id_event(
                    filter_info['tenant'],
                    filter_info['name'],
                    event_filter=event_filter
                )

            if audit_info:
                filter_info['auditLog'] = self.get_filter_contract_id_audit(
                    filter_info['tenant'],
                    filter_info['name'],
                    audit_filter=audit_filter
                )

            filters.append(filter_info)

        filters = sorted(
            filters,
            key=lambda i: i['name'].lower()
        )

        self.log.apic_mo(
            'vzFilter.info',
            filters
        )

        return filters
