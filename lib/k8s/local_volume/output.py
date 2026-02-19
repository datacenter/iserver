class K8sLocalVolumeOutput():
    def __init__(self):
        pass

    def print_local_volumes(self, info, title=False):
        if title:
            self.my_output.default(
                'Local Volume [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'node',
            'device.path',
            'device.sc',
            'device.mode'
        ]

        headers = [
            'Local Volume',
            'Node',
            'Device',
            'Storage Class',
            'Mode'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['node', 'device']
            ),
            order=order,
            headers=headers,
            row_separator=False,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
