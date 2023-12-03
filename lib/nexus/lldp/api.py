import time
import traceback


class LldpApi():
    def __init__(self):
        self.lldp_mo = None

    def get_lldp_mo(self, cache_enabled=True):
        command = 'show lldp neighbors'

        if cache_enabled:
            if self.lldp_mo is not None:
                return self.lldp_mo

            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                return cached_mo

        if not self.connect():
            self.log.error(
                'get_lldp_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_lldp_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        self.set_command_cache(command, response)
        self.lldp_mo = response

        return self.lldp_mo
