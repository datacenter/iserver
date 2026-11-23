class LinuxBootInfo():
    def __init__(self):
        self.boot = None

    def get_boot_info(self):
        if self.boot is not None:
            return self.boot

        boot = self.get_boot_cmd()
        self.boot = boot.split(' ')
        return self.boot

    def get_boot(self):
        return self.get_boot_info()
