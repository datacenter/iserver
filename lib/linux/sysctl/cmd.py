import re


class LinuxSysctlCmd():
    def __init__(self):
        self.sysctl_cmd = None

    def get_sysctl_cmd(self):
        command = 'sudo sysctl -a'
        if self.sysctl_cmd is not None:
            return self.sysctl_cmd

        cache = self.get_cmd_cache(
            'sysctl'
        )
        if cache is not None:
            self.sysctl_cmd = cache
            return self.sysctl_cmd

        outputs = self.run_commands([command])
        if outputs is None:
            self.log.error(
                'get_sysctl_cmd',
                'Commands output collection failed'
            )
            return None

        self.sysctl_cmd = outputs[command]

        self.set_cmd_cache(
            'sysctl',
            self.sysctl_cmd
        )

        return self.sysctl_cmd
