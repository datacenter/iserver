
class OcpTaskOutput():
    def __init__(self):
        pass

    def print_ocp_ssh_authorized_keys(self, info):
        order = [
            'node',
            'username',
            'key',
            'mc'
        ]

        headers = [
            'Node',
            'Username',
            'Key',
            'Machine Config'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['node']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
