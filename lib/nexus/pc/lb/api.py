class PcLbApi():
    def __init__(self):
        self.pc_lb_mo = None

    def get_pc_lb_mo(self, local_cache_enabled=True, cache_enabled=True):
        command = 'show port-channel load-balance'

        if local_cache_enabled:
            if self.pc_lb_mo is not None:
                return self.pc_lb_mo

        if cache_enabled:
            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                return cached_mo

        if not self.connect():
            self.log.error(
                'get_pc_lb_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_pc_lb_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        self.set_command_cache(command, response)
        self.pc_lb_mo = response

        return self.pc_lb_mo
