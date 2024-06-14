class K8sRoleBindingOutput():
    def __init__(self):
        pass

    def print_role_bindings(self, info, title=False):
        if title:
            self.my_output.default(
                'Role Binding [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['namespace_nameT'] = []
            item['namespace_nameT'].append('Namespace: %s' % (item['namespace']))
            item['namespace_nameT'].append('Name: %s' % (item['name']))

            item['role_subjectT'] = []
            item['role_subjectT'].append(
                'Role: %s' % (item['role']['name'])
            )
            for subject in item['subject']:
                item['role_subjectT'].append(
                    'Subject: %s' % (subject['description'])
                )

        order = [
            'namespace_nameT',
            'role_subjectT',
            'age'
        ]

        headers = [
            'Namespace - Name',
            'Role - Subject',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['namespace_nameT', 'role_subjectT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
