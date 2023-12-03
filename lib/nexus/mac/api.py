import time
import traceback


class MacApi():
    def __init__(self):
        self.mac_mo = None

    def get_mac_mo(self, cache_enabled=True):
        command = 'show mac address-table'

        if cache_enabled:
            if self.mac_mo is not None:
                return self.mac_mo

            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                return cached_mo

        if not self.connect():
            self.log.error(
                'get_mac_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_mac_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        self.set_command_cache(command, response)
        self.mac_mo = response

        return self.mac_mo
