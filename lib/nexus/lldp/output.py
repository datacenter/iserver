class LldpOutput():
    def __init__(self):
        pass

    def print_lldps(self, info, title=False):
        if title:
            self.my_output.default(
                'LLDP [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

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
            table=True
        )
