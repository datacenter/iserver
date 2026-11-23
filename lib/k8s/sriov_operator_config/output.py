class K8sSriovOperatorConfigOutput():
    def __init__(self):
        pass

    def print_sriov_operator_configs(self, info, title=False):
        if title:
            self.my_output.default(
                'SR-IOV Operator Configs [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name'
        ]

        headers = [
            'SR-IOV Operator Config'
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
