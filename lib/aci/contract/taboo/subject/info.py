class ContractTabooSubjectInfo():
    def __init__(self):
        self.taboo_contract_subject = None

    def get_taboo_contract_subject_info(self, managed_object):
        keys = [
            'descr',
            'dn',
            'name'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['tenant'] = info['dn'].split('/')[1][3:]
        info['taboo'] = info['dn'].split('/')[2][6:]
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        info['vzFilterName'] = []
        for rule_mo in managed_object['vzRsDenyRule']:
            if rule_mo['tCl'] != 'vzFilter':
                self.log.error(
                    'get_taboo_contract_subject_info',
                    'Unsupported tCl: %s' % (rule_mo['tCl'])
                )
                continue

            info['vzFilterName'].append(
                rule_mo['tnVzFilterName']
            )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_taboo_contract_subjects_info(self):
        if self.taboo_contract_subject is None:
            self.taboo_contract_subject = []

            taboo_contract_subject = self.get_taboo_contract_subject_mo()
            if taboo_contract_subject is not None:
                for managed_object in taboo_contract_subject:
                    self.taboo_contract_subject.append(
                        self.get_taboo_contract_subject_info(
                            managed_object
                        )
                    )

        self.log.apic_mo(
            'vzTSubj',
            self.subjects_mo
        )

        return self.taboo_contract_subject

    def get_taboo_contract_subjects(self, tenant, contract_name):
        all_taboo_contract_subjects = self.get_taboo_contract_subjects_info()
        taboo_contract_subjects = []
        for taboo_contract_subject in all_taboo_contract_subjects:
            if taboo_contract_subject['tenant'] == tenant and taboo_contract_subject['taboo'] == contract_name:
                taboo_contract_subject.append(
                    taboo_contract_subject
                )
        return taboo_contract_subjects

    def get_taboo_contract_subject(self, tenant_name, subject_name):
        all_taboo_contract_subjects = self.get_taboo_contract_subjects_info()
        for taboo_contract_subject in all_taboo_contract_subjects:
            if taboo_contract_subject['tenant'] == tenant_name and taboo_contract_subject['name'] == subject_name:
                return taboo_contract_subject
        return None
