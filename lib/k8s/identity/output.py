class K8sIdentityOutput():
    def __init__(self):
        pass

    def print_identities(self, info, title=False):
        if title:
            self.my_output.default(
                'Identity [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'providerName',
            'providerUserName'
        ]

        headers = [
            'Identity',
            'Provider Name',
            'provider User Name'
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
