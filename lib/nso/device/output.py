class NsoDeviceOutput():
    def __init__(self):
        pass

    def print_devices(self, info, title=False):
        if title:
            self.my_output.default(
                'Device [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'address_port',
            'authgroup',
            'device_type',
            'ned',
            'state'
        ]

        headers = [
            'Name',
            'Address',
            'AuthGroup',
            'Type',
            'NED',
            'State'
        ]

        updated = False
        for item in info:
            if 'sync' in item:
                if not updated:
                    updated = True
                    order.append('syncTick')
                    headers.append('In-Sync')

            for key in order:
                if item[key] is None:
                    item[key] = '--'

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
