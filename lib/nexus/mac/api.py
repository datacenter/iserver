class MacApi():
    def __init__(self):
        self.mac_mo = None

    def get_mac_mo(self, local_cache_enabled=True, cache_enabled=True):
        command = 'show mac address-table'

        if local_cache_enabled:
            if self.mac_mo is not None:
                return self.mac_mo

        if cache_enabled:
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

        if 'TABLE_mac_address' not in response:
            self.log.error(
                'get_mac_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if 'ROW_mac_address' not in response['TABLE_mac_address']:
            self.log.error(
                'get_mac_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if isinstance(response['TABLE_mac_address']['ROW_mac_address'], dict):
            new_response = {}
            new_response['TABLE_mac_address'] = {}
            new_response['TABLE_mac_address']['ROW_mac_address'] = []
            new_response['TABLE_mac_address']['ROW_mac_address'].append(
                response['TABLE_mac_address']['ROW_mac_address']
            )
            response = new_response

        self.set_command_cache(command, response)
        self.mac_mo = response

        return self.mac_mo
