class VersionBotOutput():
    def __init__(self):
        pass

    def print_versions(self, info, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'HW/SW Version [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'nexus_name',
            'nxos_ver_str',
            'chassis_id',
            'uptime',
            'cpu_name',
            'memory_size'
        ]

        headers = [
            'Device',
            'SW',
            'HW',
            'Uptime',
            'CPU',
            'Memory'
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
            title='HW/SW Version'
        )

        html_output = self.my_output.get_output()

        return output, html_output
