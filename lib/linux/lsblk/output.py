class LinuxLsblkOutput():
    def __init__(self):
        pass

    def print_linux_lsblk(self, info, title=False, server=None):
        if title:
            if server is None:
                self.my_output.default(
                    'Block Devices',
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Block Devices [%s]' % (server),
                    underline=True,
                    before_newline=True
                )

        order = [
            'path',
            'kname',
            'bootT',
            'maj:min',
            'size',
            'model',
            'serial',
            'group',
            'fstypeT'
        ]

        headers = [
            'Path',
            'KName',
            'Boot',
            'Maj:Min',
            'Size',
            'Model',
            'Serial',
            'Group',
            'FS Type'
        ]

        if len(info) > 0 and 'disk-path' in info[0]:
            order.append('diskId')
            headers.append('Disk ID')
            for item in info:
                item['diskId'] = []
                if item['disk-path'] is not None:
                    item['diskId'].append(
                        item['disk-path']
                    )
                if item['disk-wwn'] is not None:
                    item['diskId'].append(
                        item['disk-wwn']
                    )

                if len(item['diskId']) == 0:
                    item['diskId'].append('---')
                    
        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['diskId']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
