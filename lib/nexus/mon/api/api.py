class MonApiApi():
    def __init__(self):
        self.api_mo = None

    def get_api_mo(self, local_cache_enabled=True, cache_enabled=True):
        command = 'show nxapi'

        if local_cache_enabled:
            if self.api_mo is not None:
                return self.api_mo

        if cache_enabled:
            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                self.log.debug(
                    'get_api_mo',
                    'Cache hit: %s' % (command)
                )
                return cached_mo

        if not self.connect():
            self.log.error(
                'get_api_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_api_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        if 'TABLE_api_neighbor_detail_info' not in response:
            self.log.error(
                'get_api_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if 'ROW_api_neighbor_detail_info' not in response['TABLE_api_neighbor_detail_info']:
            self.log.error(
                'get_api_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if isinstance(response['TABLE_api_neighbor_detail_info']['ROW_api_neighbor_detail_info'], dict):
            new_response = {}
            new_response['TABLE_api_neighbor_detail_info'] = {}
            new_response['TABLE_api_neighbor_detail_info']['ROW_api_neighbor_detail_info'] = []
            new_response['TABLE_api_neighbor_detail_info']['ROW_api_neighbor_detail_info'].append(
                response['TABLE_api_neighbor_detail_info']['ROW_api_neighbor_detail_info']
            )
            response = new_response

        self.set_command_cache(command, response)
        self.api_mo = response

        return self.api_mo
