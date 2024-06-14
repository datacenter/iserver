class VersionApi():
    def __init__(self):
        self.version_mo = None

    def get_version_mo(self, local_cache_enabled=True, cache_enabled=True):
        command = 'show version'

        if local_cache_enabled:
            if self.version_mo is not None:
                return self.version_mo

        if cache_enabled:
            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                return [cached_mo]

        if not self.connect():
            self.log.error(
                'get_version_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_version_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        self.set_command_cache(command, response)
        self.version_mo = [response]

        return self.version_mo
