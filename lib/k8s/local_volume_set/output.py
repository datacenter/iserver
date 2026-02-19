class K8sLocalVolumeSetOutput():
    def __init__(self):
        pass

    def print_local_volume_sets(self, info, title=False):
        if title:
            self.my_output.default(
                'LocalVolumeSet [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'storage_class',
            'volume_mode',
            'availableT',
            'dm_availableT',
            'device_count'
        ]

        headers = [
            'LocalVolumeSet',
            'Storage Class',
            'Volume Mode',
            'Available',
            'Disk Maker',
            'Devices'
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
