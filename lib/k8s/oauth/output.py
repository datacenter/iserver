class K8sOAuthOutput():
    def __init__(self):
        pass

    def print_oauths(self, info, title=False):
        if title:
            self.my_output.default(
                'OAuth [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name'
        ]

        headers = [
            'OAuth'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_oauths_htpasswd(self, info, title=False):
        if title:
            self.my_output.default(
                'OAuth HTPasswd [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'oauth',
            'name',
            'secret',
            'isSecret',
            'usersT'
        ]

        headers = [
            'OAuth',
            'Provider',
            'Secret',
            'Is Secret',
            'User'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['usersT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
