class MonTelemetryApi():
    def __init__(self):
        self.telemetry_mo = None

    def get_telemetry_mo(self, local_cache_enabled=True, cache_enabled=True):
        command = 'show telemetry transport all'

        if local_cache_enabled:
            if self.telemetry_mo is not None:
                return self.telemetry_mo

        if cache_enabled:
            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                self.log.debug(
                    'get_telemetry_mo',
                    'Cache hit: %s' % (command)
                )
                return cached_mo

        if not self.connect():
            self.log.error(
                'get_telemetry_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_telemetry_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        if 'TABLE_telemetry_neighbor_detail_info' not in response:
            self.log.error(
                'get_telemetry_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if 'ROW_telemetry_neighbor_detail_info' not in response['TABLE_telemetry_neighbor_detail_info']:
            self.log.error(
                'get_telemetry_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if isinstance(response['TABLE_telemetry_neighbor_detail_info']['ROW_telemetry_neighbor_detail_info'], dict):
            new_response = {}
            new_response['TABLE_telemetry_neighbor_detail_info'] = {}
            new_response['TABLE_telemetry_neighbor_detail_info']['ROW_telemetry_neighbor_detail_info'] = []
            new_response['TABLE_telemetry_neighbor_detail_info']['ROW_telemetry_neighbor_detail_info'].append(
                response['TABLE_telemetry_neighbor_detail_info']['ROW_telemetry_neighbor_detail_info']
            )
            response = new_response

        self.set_command_cache(command, response)
        self.telemetry_mo = response

        return self.telemetry_mo
