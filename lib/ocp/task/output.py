
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

        for item in info:
            (key_type, key_pub, hostname) = item['key'].split(' ')
            if len(key_pub) > 68:
                item['key'] = '%s %s... %s' % (
                    key_type,
                    key_pub[:69],
                    hostname
                )

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
