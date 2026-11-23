class LinuxBootCmd():
    def __init__(self):
        self.boot_cmd = None

    def get_boot_cmd(self):
        if self.boot_cmd is not None:
            return self.boot_cmd

        cache = self.get_cmd_cache(
            'boot'
        )
        if cache is not None:
            self.boot_cmd = cache
            return self.boot_cmd

        self.boot_cmd = self.ssh_handler.get_file(
            '/proc/cmdline'
        )

        self.set_cmd_cache(
            'boot',
            self.boot_cmd
        )

        return self.boot_cmd
