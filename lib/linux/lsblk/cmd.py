class LinuxLsblkCmd():
    def __init__(self):
        self.lsblk_cmd = None

    def get_lsblk_cmd(self, cache_enabled=True):
        command = 'sudo lsblk -O --json'

        if cache_enabled and self.lsblk_cmd is not None:
            return self.lsblk_cmd

        if cache_enabled:
            cache = self.get_cmd_cache(
                'lsblk'
            )
            if cache is not None:
                self.lsblk_cmd = cache
                return self.lsblk_cmd
        
        outputs = self.run_commands([command])
        if outputs is None:
            self.log.error(
                'get_lsblk_cmd',
                'Commands output collection failed'
            )
            return None

        self.lsblk_cmd = outputs[command]

        self.set_cmd_cache(
            'lsblk',
            self.lsblk_cmd
        )

        return self.lsblk_cmd
