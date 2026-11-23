class LinuxChronyOutput():
    def __init__(self):
        pass

    def print_linux_chrony_config(self, info, title=False):
        if title:
            self.my_output.default(
                'Chrony Configuration',
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for line in info['config']:
            self.my_output.default(line)
