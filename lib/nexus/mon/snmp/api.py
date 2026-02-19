class MonSnmpApi():
    def __init__(self):
        self.snmp_mo = None

    def get_snmp_mo(self, local_cache_enabled=True, cache_enabled=True):
        command = 'show snmp'

        if local_cache_enabled:
            if self.snmp_mo is not None:
                return self.snmp_mo

        if cache_enabled:
            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                self.log.debug(
                    'get_snmp_mo',
                    'Cache hit: %s' % (command)
                )
                return cached_mo

        if not self.connect():
            self.log.error(
                'get_snmp_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_snmp_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        if 'TABLE_snmp_neighbor_detail_info' not in response:
            self.log.error(
                'get_snmp_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if 'ROW_snmp_neighbor_detail_info' not in response['TABLE_snmp_neighbor_detail_info']:
            self.log.error(
                'get_snmp_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if isinstance(response['TABLE_snmp_neighbor_detail_info']['ROW_snmp_neighbor_detail_info'], dict):
            new_response = {}
            new_response['TABLE_snmp_neighbor_detail_info'] = {}
            new_response['TABLE_snmp_neighbor_detail_info']['ROW_snmp_neighbor_detail_info'] = []
            new_response['TABLE_snmp_neighbor_detail_info']['ROW_snmp_neighbor_detail_info'].append(
                response['TABLE_snmp_neighbor_detail_info']['ROW_snmp_neighbor_detail_info']
            )
            response = new_response

        self.set_command_cache(command, response)
        self.snmp_mo = response

        return self.snmp_mo
