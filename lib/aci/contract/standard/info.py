from lib import filter_helper


class ContractStandardInfo():
    def __init__(self):
        self.standard_contract = None

    def get_standard_contract_count(self, tenant_name=None):
        contract_filter = None
        if tenant_name is not None:
            contract_filter = ['tenant:%s' % (tenant_name)]

        contracts = self.get_standard_contracts(
            contract_filter=contract_filter
        )
        return len(contracts)

    def get_standard_contract(self, tenant, name):
        contract_filter = []
        contract_filter.append(
            'tenant:%s' % (tenant)
        )
        contract_filter.append(
            'name:%s' % (name)
        )

        contracts = self.get_standard_contracts(
            contract_filter=contract_filter
        )

        if len(contracts) == 1:
            return contracts[0]

        return None

    def get_standard_contract_epg_info(self, managed_object):
        if managed_object['tCl'] not in ['fvAEPg', 'l2extInstP', 'l3extInstP', 'mgmtInB']:
            self.log.error(
                'get_contract_epg_info',
                'Unsupported object class: %s' % (managed_object)
            )
            return None

        if managed_object['tCl'] == 'fvAEPg':
            # "tDn": "uni/tn-mgmt/ap-EU-SPDC_ANP/epg-EU-SPDC-MGMT"
            info = {}
            info['class'] = 'fvAEPg'
            info['tenant'] = managed_object['tDn'].split('/')[1][3:]
            info['application_profile'] = managed_object['tDn'].split('/')[2][3:]
            info['name'] = managed_object['tDn'].split('/')[3][4:]
            info['nameTenant'] = '%s/%s' % (
                info['tenant'],
                info['name']
            )
            info['nameLong'] = '%s/%s/%s' % (
                info['tenant'],
                info['application_profile'],
                info['name']
            )

        if managed_object['tCl'] == 'l3extInstP':
            # "tDn": "uni/tn-common/out-Infra_privIP_L3out/instP-Infra_privIP_ExtEPG"
            info = {}
            info['class'] = 'l3extInstP'
            info['tenant'] = managed_object['tDn'].split('/')[1][3:]
            info['l3out'] = managed_object['tDn'].split('/')[2][4:]
            info['name'] = managed_object['tDn'].split('/')[3][6:]
            info['nameTenant'] = '%s/%s' % (
                info['tenant'],
                info['name']
            )
            info['nameLong'] = '%s/%s/%s' % (
                info['tenant'],
                info['l3out'],
                info['name']
            )

        if managed_object['tCl'] == 'l2extInstP':
            # "tDn": "uni/tn-common/l2out-VNF-mgmt_L2out/instP-VNF-mgmt_L2ext"
            info = {}
            info['class'] = 'l2extInstP'
            info['tenant'] = managed_object['tDn'].split('/')[1][3:]
            info['l3out'] = managed_object['tDn'].split('/')[2][4:]
            info['name'] = managed_object['tDn'].split('/')[3][6:]
            info['nameTenant'] = '%s/%s' % (
                info['tenant'],
                info['name']
            )
            info['nameLong'] = '%s/%s/%s' % (
                info['tenant'],
                info['l3out'],
                info['name']
            )

        if managed_object['tCl'] == 'mgmtInB':
            # "tDn": "uni/tn-mgmt/mgmtp-default/inb-default"
            info = {}
            info['class'] = 'mgmtInB'
            info['tenant'] = managed_object['tDn'].split('/')[1][3:]
            info['mgmt'] = managed_object['tDn'].split('/')[2][6:]
            info['name'] = managed_object['tDn'].split('/')[3][4:]
            info['nameTenant'] = '%s/%s' % (
                info['tenant'],
                info['name']
            )
            info['nameLong'] = '%s/%s/%s' % (
                info['tenant'],
                info['mgmt'],
                info['name']
            )

        return info

    def get_standard_contract_filters_info(self, managed_object):
        info = []
        for item in managed_object['vzSubj']:
            subject_name = item['name']
            subject_tenant = managed_object['dn'].split('/')[1][3:]
            subject_info = self.get_subject(
                subject_tenant,
                subject_name
            )
            if subject_info is None:
                continue

            for filter_item in subject_info['vzFilter']:
                filter_tenant = filter_item['tenant']
                if len(filter_tenant) == 0:
                    filter_tenant = subject_tenant

                filter_info = self.get_contract_filter(
                    filter_tenant,
                    filter_item['name']
                )
                if filter_info is None:
                    self.log.error(
                        'get_standard_contract_filters_info',
                        'Filter not found: %s/%s' % (
                            filter_tenant,
                            filter_item['name']
                        )
                    )
                    self.log.error(
                        'get_standard_contract_filters_info',
                        subject_info
                    )
                    self.log.error(
                        'get_standard_contract_filters_info',
                        managed_object
                    )
                    continue

                filter_info['subjectName'] = subject_name
                filter_info['subjectTenant'] = subject_tenant
                filter_info['subjectNameTenant'] = '%s/%s' % (
                    subject_tenant,
                    subject_name
                )
                info.append(
                    filter_info
                )

        return info

    def get_standard_contract_info(self, managed_object):
        keys = [
            'descr',
            'dn',
            'intent',
            'name',
            'scope',
            'targetDscp',
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

        info['vzFilter'] = self.get_standard_contract_filters_info(
            managed_object
        )

        info['consumerEpg'] = []
        for item in managed_object['vzRtCons']:
            contract_epg_info = self.get_standard_contract_epg_info(
                item
            )
            if contract_epg_info is not None:
                info['consumerEpg'].append(
                    contract_epg_info
                )

        info['providerEpg'] = []
        for item in managed_object['vzRtProv']:
            contract_epg_info = self.get_standard_contract_epg_info(
                item
            )
            if contract_epg_info is not None:
                info['providerEpg'].append(
                    contract_epg_info
                )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_standard_contracts_info(self):
        if self.standard_contract is None:
            self.standard_contract = []

            contracts = self.get_standard_contract_mo()
            if contracts is not None:
                for managed_object in contracts:
                    self.standard_contract.append(
                        self.get_standard_contract_info(
                            managed_object
                        )
                    )

        return self.standard_contract

    def match_standard_contract(self, contract_info, contract_filter):
        if contract_filter is None or len(contract_filter) == 0:
            return True

        for contract_rule in contract_filter:
            (key, value) = contract_rule.split(':')
            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_tenant_name(value, contract_info['nameTenant']):
                    return False

            if key == 'names':
                key_found = True
                found = False
                for name in value.split(','):
                    if filter_helper.match_tenant_name(name, contract_info['nameTenant']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'tenant':
                key_found = True
                if not filter_helper.match_string(value, contract_info['tenant']):
                    return False

            if key == 'filter':
                key_found = True
                found = False
                for filter_info in contract_info['vzFilter']:
                    if filter_helper.match_tenant_name(value, filter_info['nameTenant']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'fault':
                key_found = True
                if value == 'any':
                    if not contract_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_standard_contract',
                        'Unsupported fault filtering value: %s' % (value)
                    )

            if not key_found:
                self.log.error(
                    'match_standard_contract',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_standard_contracts(
            self,
            contract_filter=None,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_contracts = self.get_standard_contracts_info()
        if all_contracts is None:
            return None

        contracts = []

        for contract_info in all_contracts:
            if not self.match_standard_contract(contract_info, contract_filter):
                continue

            if fault_info:
                contract_info['faultInst'] = self.get_standard_contract_id_fault(
                    contract_info['tenant'],
                    contract_info['name'],
                    'faultInst'
                )

            if hfault_info:
                contract_info['faultRecord'] = self.get_standard_contract_id_fault(
                    contract_info['tenant'],
                    contract_info['name'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                contract_info['eventLog'] = self.get_standard_contract_id_event(
                    contract_info['tenant'],
                    contract_info['name'],
                    event_filter=event_filter
                )

            if audit_info:
                contract_info['auditLog'] = self.get_standard_contract_id_audit(
                    contract_info['tenant'],
                    contract_info['name'],
                    audit_filter=audit_filter
                )

            contracts.append(contract_info)

        contracts = sorted(
            contracts,
            key=lambda i: i['nameTenant'].lower()
        )

        self.log.apic_mo(
            'vzBrCP.info',
            contracts
        )

        return contracts
