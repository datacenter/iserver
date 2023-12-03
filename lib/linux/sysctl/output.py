class LinuxSysctlOutput():
    def __init__(self):
        pass

    def print_linux_sysctl(self, info, diff_servers, diff_sysctl, title=False):
        if title:
            self.my_output.default(
                'Sysctl [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'key',
            'value'
        ]

        headers = [
            'Key',
            'Value'
        ]

        if len(diff_servers) > 0:
            for diff_server in diff_servers:
                order.append(diff_server)
                headers.append('Server: %s' % (diff_server))

                for item in info:
                    for diff_item in diff_sysctl[diff_server]:
                        if item['key'] == diff_item['key']:
                            item[diff_server] = diff_item['value']

            for item in info:
                item['__Output'] = {}
                for diff_server in diff_servers:
                    if item['value'] != item[diff_server]:
                        item['__Output']['key'] = 'Red'
                        item['__Output']['value'] = 'Red'
                        item['__Output'][diff_server] = 'Red'

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=False,
            underline=True,
            table=True
        )
