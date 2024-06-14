class NodeBotOutput():
    def __init__(self):
        pass

    def print_nodes(self, info, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'Node [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'full_name',
            'id',
            'address',
            'adSt',
            'fabricSt',
            'roleUi',
            'model',
            'serial',
            'version'
        ]

        headers = [
            'Node Name',
            'ID',
            'VTEP IP',
            'Admin',
            'Fabric',
            'Role',
            'Model',
            'Serial',
            'Version'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Node'
        )

        html_output = self.my_output.get_output()

        return output, html_output