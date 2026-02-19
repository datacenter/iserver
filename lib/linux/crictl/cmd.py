class LinuxCrictlCmd():
    def __init__(self):
        self.crictl_ps_cmd = None

    def get_critctl_ps_cmd(self, cache_enabled=True):
        command = 'sudo crictl ps -a -o json'

        if cache_enabled and self.crictl_ps_cmd is not None:
            return self.crictl_ps_cmd

        if cache_enabled:
            cache = self.get_cmd_cache(
                'crictl_ps'
            )
            if cache is not None:
                self.crictl_ps_cmd = cache
                return self.crictl_ps_cmd
        
        outputs = self.run_commands([command])
        if outputs is None:
            self.log.error(
                'get_crictl_ps_cmd',
                'Commands output collection failed'
            )
            return None

        self.crictl_ps_cmd = outputs[command]

        self.set_cmd_cache(
            'crictl_ps',
            self.crictl_ps_cmd
        )

        return self.crictl_ps_cmd
