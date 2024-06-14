class ContractSubjectInfo():
    def __init__(self):
        self.subjects = None

    def get_subject_info(self, managed_object):
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
        contract_dn = info['dn'].split('/')[2]
        if contract_dn.split('-')[0] == 'brc':
            info['contract'] = contract_dn[4:]
        if contract_dn.split('-')[0] == 'oobbrc':
            info['contract'] = contract_dn[7:]

        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        info['vzFilter'] = []
        for rule_mo in managed_object['vzRsSubjFiltAtt']:
            if rule_mo['tCl'] != 'vzFilter':
                self.log.error(
                    'get_subject_info',
                    'Unsupported tCl: %s' % (rule_mo['tCl'])
                )
                continue

            filter_info = {}
            filter_info['name'] = rule_mo['tnVzFilterName']
            try:
                filter_info['tenant'] = rule_mo['tDn'].split('/')[1][3:]
            except BaseException:
                filter_info['tenant'] = ''

            info['vzFilter'].append(
                filter_info
            )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_subjects_info(self):
        if self.subjects is None:
            self.subjects = []

            subjects = self.get_subjects_mo()
            if subjects is not None:
                for managed_object in subjects:
                    self.subjects.append(
                        self.get_subject_info(
                            managed_object
                        )
                    )

        self.log.apic_mo(
            'vzSubj.info',
            self.subjects
        )

        return self.subjects

    def get_subjects(self, tenant, contract_name):
        all_subjects = self.get_subjects_info()
        subjects = []
        for subject in all_subjects:
            if subject['tenant'] == tenant and subject['contract'] == contract_name:
                subjects.append(
                    subject
                )

        return subjects

    def get_subject(self, tenant, name):
        all_subjects = self.get_subjects_info()
        for subject in all_subjects:
            if subject['tenant'] == tenant and subject['name'] == name:
                return subject

        return None
