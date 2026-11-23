class HardwareOutput():
    def __init__(self):
        pass

    def print_hardwares(self, info, title=False):
        if title:
            self.my_output.default(
                'Hardware [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'chassis.model_num',
            'chassis.hw_ver',
            'chassis.part_num',
            'chassis.part_revision',
            'chassis.serial_num'
        ]

        headers = [
            'Device',
            'Chassis',
            'HW Ver',
            'PN',
            'PN Rev',
            'SN'
        ]

        self.my_output.my_table(
            info,
            order=order,
            allow_order_subkeys=True,
            headers=headers,
            underline=True,
            table=True
        )

        order = [
            'nexus_name',
            'ps.status_ok_empty',
            'ps.type',
            'ps.model_num',
            'ps.hw_ver',
            'ps.part_num',
            'ps.part_revision',
            'ps.serial_num'
        ]

        headers = [
            'Device',
            'PS State',
            'Type',
            'Model',
            'HW Ver',
            'PN',
            'PN Rev',
            'SN'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['ps']
            ),
            order=order,
            allow_order_subkeys=True,
            headers=headers,
            underline=True,
            table=True
        )

        order = [
            'nexus_name',
            'fan.status_ok_empty'
        ]

        headers = [
            'Device',
            'Fan State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['fan']
            ),
            order=order,
            allow_order_subkeys=True,
            headers=headers,
            underline=True,
            table=True
        )
