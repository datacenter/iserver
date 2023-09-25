class K8sOperatorGroupOutput():
    def __init__(self):
        pass

    def print_operator_groups(self, info, title=False):
        if title:
            self.my_output.default(
                'Operator Group - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace',
            'name',
            'nsCount',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Target Namespaces',
            'Age'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_operator_groups_ns(self, info, title=False):
        if title:
            self.my_output.default(
                'Operator Group - Target Namespace [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace',
            'name',
            'ns.name',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Target Namespace',
            'Age'
        ]

        for item in info:
            if len(item['ns']) == 0:
                item['ns'].append(dict(name='--'))

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['ns']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
