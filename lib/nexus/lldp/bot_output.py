class LldpBotOutput():
    def __init__(self):
        pass

    def print_lldps(self, info, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'LLDP [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        for item in info:
            if item['system_capability'] is None:
                item['system_capability'] = '--'

        order = [
            'nexus_name',
            'l_port_id',
            'chassis_id',
            'port_id',
            'hold_time',
            'system_capability'
        ]

        headers = [
            'Device',
            'Local Interface',
            'Device ID',
            'Port ID',
            'Hold Time',
            'Capability'
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
            title='LLDP'
        )

        html_output = self.my_output.get_output()

        return output, html_output
