class ConfigApi():
    def __init__(self):
        self.config_mo = None

    def get_config_mo(self, cache_enabled=True):
        command = 'show running-config'

        if cache_enabled:
            if self.config_mo is not None:
                return self.config_mo

            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                return cached_mo

        if not self.connect():
            self.log.error(
                'get_config_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_config_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        self.set_command_cache(command, response)
        self.config_mo = [response]

        return self.config_mo
