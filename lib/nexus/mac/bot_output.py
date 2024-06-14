class MacBotOutput():
    def __init__(self):
        pass

    def print_macs(self, info, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'MAC [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'nexus_name',
            'vlan',
            'mac_addr',
            'type',
            'age',
            'is_secure',
            'is_ntfy',
            'port'
        ]

        headers = [
            'Device',
            'VLAN',
            'MAC',
            'Type',
            'Age',
            'Sec',
            'Ntfy',
            'Port'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='MAC Address Table'
        )

        html_output = self.my_output.get_output()

        return output, html_output
