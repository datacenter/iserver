class K8sServiceAccountOutput():
    def __init__(self):
        pass

    def print_service_accounts(self, info, title=False):
        if title:
            self.my_output.default(
                'Service Account [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        row_separator = False
        for item in info:
            if len(item['secret']) > 1:
                row_separator = True

        order = [
            'namespace',
            'name',
            'secret.name',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Secret',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['secret']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=row_separator,
            table=True
        )
