class InterfaceStateApi():
    def __init__(self):
        self.interface_mo = None

    def get_interface_mo(self, local_cache_enabled=True, cache_enabled=True):
        command = 'show interface'

        if local_cache_enabled:
            if self.interface_mo is not None:
                return self.interface_mo

        if cache_enabled:
            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                return cached_mo

        if not self.connect():
            self.log.error(
                'get_interface_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_interface_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        if 'TABLE_interface' not in response:
            self.log.error(
                'get_interface_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if 'ROW_interface' not in response['TABLE_interface']:
            self.log.error(
                'get_interface_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if isinstance(response['TABLE_interface']['ROW_interface'], dict):
            new_response = {}
            new_response['TABLE_interface'] = {}
            new_response['TABLE_interface']['ROW_interface'] = []
            new_response['TABLE_interface']['ROW_interface'].append(
                response['TABLE_interface']['ROW_interface']
            )
            response = new_response

        self.set_command_cache(command, response)
        self.interface_mo = response

        return self.interface_mo
