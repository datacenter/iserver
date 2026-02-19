class OcpTaskHelmOutput():
    def __init__(self):
        pass

    def print_ocp_helm(self, info, title=False):
        if title:
            self.my_output.default(
                'Helm',
                underline=True,
                before_newline=True
            )

        if info is None:
            self.my_output.default('None')
            return
        
        order = [
            'namespace',
            'name',
            'revision',
            'status',
            'chart',
            'app_version'
        ]

        headers = [
            'Namespace',
            'Name',
            'Revision',
            'Status',
            'Chart',
            'Version'
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