import json


class K8sLogicalVolumeOutput():
    def __init__(self):
        pass

    def print_logical_volumes(self, info, title=False):
        if title:
            self.my_output.default(
                'Logical Volume [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if info is None or len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'info.node_name',
            'info.device_class',
            'info.requested_size',
            'info.current_size',
            'info.volume_id'
        ]

        headers = [
            'Logical Volume',
            'Node',
            'Device Class',
            'Req Size',
            'Curr Size',
            'Volume'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=False,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
