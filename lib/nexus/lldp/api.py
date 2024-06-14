class LldpApi():
    def __init__(self):
        self.lldp_mo = None

    def get_lldp_mo(self, local_cache_enabled=True, cache_enabled=True):
        command = 'show lldp neighbors'

        if local_cache_enabled:
            if self.lldp_mo is not None:
                return self.lldp_mo

        if cache_enabled:
            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                self.log.debug(
                    'get_lldp_mo',
                    'Cache hit: %s' % (command)
                )
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

        if 'TABLE_nbor' not in response:
            self.log.error(
                'get_lldp_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if 'ROW_nbor' not in response['TABLE_nbor']:
            self.log.error(
                'get_lldp_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if isinstance(response['TABLE_nbor']['ROW_nbor'], dict):
            new_response = {}
            new_response['TABLE_nbor'] = {}
            new_response['TABLE_nbor']['ROW_nbor'] = []
            new_response['TABLE_nbor']['ROW_nbor'].append(
                response['TABLE_nbor']['ROW_nbor']
            )
            response = new_response

        self.set_command_cache(command, response)
        self.lldp_mo = response

        return self.lldp_mo
