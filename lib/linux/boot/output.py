class LinuxBootOutput():
    def __init__(self):
        pass

    def print_linux_boot(self, info):

        self.my_output.default(
            'Boot parameters',
            underline=True,
            before_newline=True
        )

        for item in info:
            self.my_output.default(item)
