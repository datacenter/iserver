class PcDatabaseApi():
    def __init__(self):
        self.pc_database_mo = None

    def get_pc_database_mo(self, local_cache_enabled=True, cache_enabled=True):
        command = 'show port-channel database'

        if local_cache_enabled:
            if self.pc_database_mo is not None:
                return self.pc_database_mo

        if cache_enabled:
            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                return cached_mo

        if not self.connect():
            self.log.error(
                'get_pc_database_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_pc_database_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        if len(response) == 0:
            response = {}
            response['TABLE_interface'] = {}
            response['TABLE_interface']['ROW_interface'] = []

        if 'TABLE_interface' not in response:
            self.log.error(
                'get_pc_database_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if 'ROW_interface' not in response['TABLE_interface']:
            self.log.error(
                'get_pc_database_mo',
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
        self.pc_database_mo = response

        return self.pc_database_mo
