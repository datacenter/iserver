class K8sSandboxPolicyOutput():
    def __init__(self):
        pass

    def print_sandbox_policies(self, info, title=False):
        if title:
            self.my_output.default(
                'Sandbox Policy - State [#%s]' % (len(info)),
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
            'Sandbox Policy'
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
