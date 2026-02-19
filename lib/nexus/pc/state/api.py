class PcStateApi():
    def __init__(self):
        self.pc_state_mo = None

    def get_pc_state_mo(self, local_cache_enabled=True, cache_enabled=True):
        command = 'show port-channel summary'

        if local_cache_enabled:
            if self.pc_state_mo is not None:
                return self.pc_state_mo

        if cache_enabled:
            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                return cached_mo

        if not self.connect():
            self.log.error(
                'get_pc_state_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_pc_state_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        if 'TABLE_channel' in response and 'ROW_channel' in response['TABLE_channel']:
            if isinstance(response['TABLE_channel']['ROW_channel'], dict):
                new_response = {}
                new_response['TABLE_channel'] = {}
                new_response['TABLE_channel']['ROW_channel'] = []
                new_response['TABLE_channel']['ROW_channel'].append(
                    response['TABLE_channel']['ROW_channel']
                )
                response = new_response

        self.set_command_cache(command, response)
        self.pc_state_mo = response

        return self.pc_state_mo
