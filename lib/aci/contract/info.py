import time

from lib import filter_helper


class ContractInfo():
    def __init__(self):
        self.contracts = None

    def get_contract_count(self, tenant_name=None):
        contract_filter = None
        if tenant_name is not None:
            contract_filter = ['tenant:%s' % (tenant_name)]

        contracts = self.get_contracts(
            contract_filter=contract_filter
        )
        return len(contracts)

    def get_contract(self, tenant, name):
        contract_filter = []
        contract_filter.append(
            'tenant:%s' % (tenant)
        )
        contract_filter.append(
            'name:%s' % (name)
        )

        contracts = self.get_contracts(
            contract_filter=contract_filter
        )

        if len(contracts) == 1:
            return contracts[0]

        return None

    def get_contract_epg_info(self, managed_object):
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

    def get_contract_filters_info(self, managed_object):
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
                filter_info = self.get_filter(
                    filter_item['tenant'],
                    filter_item['name']
                )
                if filter_info is None:
                    # self.log.error(
                    #     'get_contract_filters_info',
                    #     'Filter not found: %s/%s' % (
                    #         filter_item['tenant'],
                    #         filter_item['name']
                    #     )
                    # )
                    # self.log.error(
                    #     'get_contract_filters_info',
                    #     subject_info
                    # )
                    # self.log.error(
                    #     'get_contract_filters_info',
                    #     managed_object
                    # )
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

    def get_contract_info(self, managed_object):
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

        info['vzFilter'] = self.get_contract_filters_info(
            managed_object
        )

        info['consumerEpg'] = []
        for item in managed_object['vzRtCons']:
            contract_epg_info = self.get_contract_epg_info(
                item
            )
            if contract_epg_info is not None:
                info['consumerEpg'].append(
                    contract_epg_info
                )

        info['providerEpg'] = []
        for item in managed_object['vzRtProv']:
            contract_epg_info = self.get_contract_epg_info(
                item
            )
            if contract_epg_info is not None:
                info['providerEpg'].append(
                    contract_epg_info
                )

        return info

    def get_contracts_info(self):
        if self.contracts is None:
            self.contracts = []

            contracts = self.get_contracts_mo()
            if contracts is not None:
                for managed_object in contracts:
                    self.contracts.append(
                        self.get_contract_info(
                            managed_object
                        )
                    )

        return self.contracts

    def match_contract(self, contract_info, contract_filter):
        if contract_filter is None or len(contract_filter) == 0:
            return True

        for contract_rule in contract_filter:
            (key, value) = contract_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, contract_info['name']):
                    return False

            if key == 'names':
                found = False
                for name in value.split(','):
                    if '/' in name:
                        if filter_helper.match_string(name, contract_info['nameTenant']):
                            found = True
                            break
                    else:
                        if not filter_helper.match_string(name, contract_info['name']):
                            return False

                if not found:
                    return False

            if key == 'tenant':
                if not filter_helper.match_string(value, contract_info['tenant']):
                    return False

            if key == 'filter':
                found = False
                for filter_info in contract_info['vzFilter']:
                    if filter_helper.match_string(value, filter_info['nameTenant']):
                        found = True
                        break

                if not found:
                    return False

        return True

    def get_contracts(self, contract_filter=None):
        start_time = int(time.time() * 1000)

        all_contracts = self.get_contracts_info()
        if all_contracts is None:
            return None

        contracts = []

        for contract_info in all_contracts:
            if not self.match_contract(contract_info, contract_filter):
                continue

            contracts.append(contract_info)

        contracts = sorted(
            contracts,
            key=lambda i: i['nameTenant'].lower()
        )

        self.log.apic_mo(
            'vzBrCP.info',
            contracts
        )

        self.log.trace(
            'get_contracts',
            start_time
        )

        return contracts
