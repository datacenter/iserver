import time
import traceback


class LacpApi():
    def __init__(self):
        self.lacp_mo = None

    def get_lacp_mo(self, cache_enabled=True):
        command = 'show lacp neighbor'

        if cache_enabled:
            if self.lacp_mo is not None:
                return self.lacp_mo

            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                return cached_mo

        if not self.connect():
            self.log.error(
                'get_lacp_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_lacp_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        self.set_command_cache(command, response)
        self.lacp_mo = response

        return self.lacp_mo
