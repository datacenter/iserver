class TabooSubjectInfo():
    def __init__(self):
        self.taboo_subjects = None

    def get_taboo_subject_info(self, managed_object):
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
                    'get_taboo_subject_info',
                    'Unsupported tCl: %s' % (rule_mo['tCl'])
                )
                continue

            info['vzFilterName'].append(
                rule_mo['tnVzFilterName']
            )

        return info

    def get_taboo_subjects_info(self):
        if self.taboo_subjects is None:
            self.taboo_subjects = []

            taboo_subjects = self.get_taboo_subjects_mo()
            if taboo_subjects is not None:
                for managed_object in taboo_subjects:
                    self.taboo_subjects.append(
                        self.get_taboo_subject_info(
                            managed_object
                        )
                    )

        self.log.apic_mo(
            'vzTSubj',
            self.subjects_mo
        )

        return self.taboo_subjects

    def get_taboo_subjects(self, tenant, contract_name):
        all_taboo_subjects = self.get_taboo_subjects_info()
        taboo_subjects = []
        for taboo_subject in all_taboo_subjects:
            if taboo_subject['tenant'] == tenant and taboo_subject['taboo'] == contract_name:
                taboo_subjects.append(
                    taboo_subject
                )

        return taboo_subjects

    def get_taboo_subject(self, tenant, name):
        all_taboo_subjects = self.get_taboo_subjects_info()
        for taboo_subject in all_taboo_subjects:
            if taboo_subject['tenant'] == tenant and taboo_subject['name'] == name:
                return taboo_subject
        return None
