class K8sUserOutput():
    def __init__(self):
        pass

    def print_users(self, info, title=False):
        if title:
            self.my_output.default(
                'User [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'identities'
        ]

        headers = [
            'User',
            'Identity'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['identities']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
