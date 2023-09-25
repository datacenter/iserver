class K8sEndpointOutput():
    def __init__(self):
        pass

    def print_endpoints(self, info, title=False):
        if title:
            self.my_output.default(
                'Endpoint - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace',
            'name',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Age'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
