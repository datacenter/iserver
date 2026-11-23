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

        self.my_output.my_table_ng(
            info,
            [
                ['Path', 'pathT'],
                ['Boot', 'bootT'],
                ['Trim', 'trimT'],
                ['Maj:Min', 'maj:min'],
                ['Size', 'size'],
                ['HW', 'hwT'],
                ['FS', 'fstypeT'],
                ['Disk ID', 'disk-id'],
                ['Warning', 'warningT']
            ],
            remove_empty=['warningT']
        )