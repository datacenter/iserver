class VrfApi():
    def __init__(self):
        self.vrf_mo = None

    def get_vrf_mo(self, local_cache_enabled=True, cache_enabled=True):
        command = 'show vrf detail'

        if local_cache_enabled:
            if self.vrf_mo is not None:
                return self.vrf_mo

        if cache_enabled:
            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                self.log.debug(
                    'get_vrf_mo',
                    'Cache hit: %s' % (command)
                )
                return cached_mo

        if not self.connect():
            self.log.error(
                'get_vrf_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_vrf_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        if 'TABLE_vrf' not in response:
            self.log.error(
                'get_vrf_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if 'ROW_vrf' not in response['TABLE_vrf']:
            self.log.error(
                'get_vrf_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if isinstance(response['TABLE_vrf']['ROW_vrf'], dict):
            new_response = {}
            new_response['TABLE_vrf'] = {}
            new_response['TABLE_vrf']['ROW_vrf'] = []
            new_response['TABLE_vrf']['ROW_vrf'].append(
                response['TABLE_vrf']['ROW_vrf']
            )
            response = new_response

        self.set_command_cache(command, response)
        self.vrf_mo = response

        return self.vrf_mo
