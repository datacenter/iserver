class VlanApi():
    def __init__(self):
        self.vlan_mo = None

    def get_vlan_mo(self, local_cache_enabled=True, cache_enabled=True):
        command = 'show vlan'

        if local_cache_enabled:
            if self.vlan_mo is not None:
                return self.vlan_mo

        if cache_enabled:
            cached_mo = self.get_command_cache(command)
            if cached_mo is not None:
                self.log.debug(
                    'get_vlan_mo',
                    'Cache hit: %s' % (command)
                )
                return cached_mo

        if not self.connect():
            self.log.error(
                'get_vlan_mo',
                'API connection failed: %s' % (self.nexus_name)
            )
            return None

        response = self.run_show_command(command)
        if response is None:
            self.log.error(
                'get_vlan_mo',
                'Command failed on %s: %s' % (
                    self.nexus_name,
                    command
                )
            )
            return None

        if 'TABLE_vlanbrief' not in response:
            self.log.error(
                'get_vlan_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if 'ROW_vlanbrief' not in response['TABLE_vlanbrief']:
            self.log.error(
                'get_vlan_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if 'TABLE_mtuinfo' not in response:
            self.log.error(
                'get_vlan_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        if 'ROW_mtuinfo' not in response['TABLE_mtuinfo']:
            self.log.error(
                'get_vlan_mo',
                'Unexpected rest response %s: %s' % (
                    self.nexus_name,
                    response
                )
            )
            return None

        new_response = {}

        if isinstance(response['TABLE_vlanbrief']['ROW_vlanbrief'], dict):
            new_response['TABLE_vlanbrief'] = {}
            new_response['TABLE_vlanbrief']['ROW_vlanbrief'] = []
            new_response['TABLE_vlanbrief']['ROW_vlanbrief'].append(
                response['TABLE_vlanbrief']['ROW_vlanbrief']
            )
        else:
            new_response['TABLE_vlanbrief'] = response['TABLE_vlanbrief']

        if isinstance(response['TABLE_mtuinfo']['ROW_mtuinfo'], dict):
            new_response['TABLE_mtuinfo'] = {}
            new_response['TABLE_mtuinfo']['ROW_mtuinfo'] = []
            new_response['TABLE_mtuinfo']['ROW_mtuinfo'].append(
                response['TABLE_mtuinfo']['ROW_mtuinfo']
            )
        else:
            new_response['TABLE_mtuinfo'] = response['TABLE_mtuinfo']

        self.set_command_cache(command, new_response)
        self.vlan_mo = new_response

        return self.vlan_mo
