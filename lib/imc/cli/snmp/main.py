import json


class ImcCliSnmp():
    def __init__(self):
        self.snmp_mo = None
        self.snmp_destination_mo = None
        self.snmp_user_mo = None

    def get_snmp_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.snmp_mo is not None:
                return self.snmp_mo

            self.snmp_mo = self.get_imc_cli_cache_entry(
                'snmp'
            )
            if self.snmp_mo is not None:
                return self.snmp_mo

        # com /snmp # show detail
        # SNMP Settings:
        #     Enabled: yes
        #     SNMP Port: 161
        #     System Contact: who@where
        #     System Location: unknown
        #     SNMP v2 Enabled: yes
        #     Access Community String: cimcpublic
        #     Trap Community String: public
        #     SNMP Community access: full
        #     SNMP v3 Enabled: no
        #     User Input EngineID:
        #     SNMP Engine ID: 11 11 11
        #     Serial Number Enabled: no

        self.snmp_mo = self.show_dict(
            'show detail',
            start='SNMP Settings:',
            scope='snmp'
        )

        if self.snmp_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'snmp',
            self.snmp_mo
        )

        self.log.debug(
            'get_snmp_mo',
            json.dumps(self.snmp_mo, indent=4)
        )
        return self.snmp_mo

    def get_snmp_destination_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.snmp_destination_mo is not None:
                return self.snmp_destination_mo

            self.snmp_destination_mo = self.get_imc_cli_cache_entry(
                'snmp_destination'
            )
            if self.snmp_destination_mo is not None:
                return self.snmp_destination_mo

        # com /snmp # show trap-destinations detail
        # Trap Destination 1:
        #     Enabled: yes
        #     SNMP version: 2
        #     Trap type: trap
        #     SNMP user:
        #     Trap Address(IPv4/IPv6/FQDN): <ip>
        #     Trap Port: 7162
        #     Delete Trap: no
        #     Trap Community String: public

        if keep_scope:
            self.snmp_destination_mo = self.show_list(
                'show trap-destinations detail',
                'Trap Destination __INDEX__:',
                None,
                method='last word',
                top=False
            )
        else:
            self.snmp_destination_mo = self.show_list(
                'show trap-destinations detail',
                'Trap Destination __INDEX__:',
                None,
                method='last word',
                scope='snmp'
            )

        if self.snmp_destination_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'snmp_destination',
            self.snmp_destination_mo
        )

        self.log.debug(
            'get_snmp_destination_mo',
            json.dumps(self.snmp_destination_mo, indent=4)
        )
        return self.snmp_destination_mo

    def get_snmp_user_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.snmp_user_mo is not None:
                return self.snmp_user_mo

            self.snmp_user_mo = self.get_imc_cli_cache_entry(
                'snmp_user'
            )
            if self.snmp_user_mo is not None:
                return self.snmp_user_mo

        # com /snmp # show v3users detail
        # User 1:
        #     Add User: no
        #     Security Name: (n/a)
        #     Security Level: (n/a)
        #     Auth Type: (n/a)
        #     Auth Key: ******
        #     Encryption: (n/a)
        #     Private Key: ******

        if keep_scope:
            self.snmp_user_mo = self.show_list(
                'show v3users detail',
                'User __INDEX__:',
                None,
                method='last word',
                top=False
            )
        else:
            self.snmp_user_mo = self.show_list(
                'show v3users detail',
                'User __INDEX__:',
                None,
                method='last word',
                scope='snmp'
            )

        if self.snmp_user_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'snmp_user',
            self.snmp_user_mo
        )

        self.log.debug(
            'get_snmp_user_mo',
            json.dumps(self.snmp_user_mo, indent=4)
        )
        return self.snmp_user_mo

    def get_snmp_info(self, snmp_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        info['Enabled'] = snmp_mo['Enabled']
        if info['Enabled'] == 'yes':
            info['__Output']['Enabled'] = 'Green'
        else:
            info['__Output']['Enabled'] = 'Red'

        info['Port'] = snmp_mo['SNMP Port']
        info['Contact'] = snmp_mo['System Contact']
        info['Location'] = snmp_mo['System Location']
        info['SNMPv2'] = snmp_mo['SNMP v2 Enabled']
        if info['SNMPv2'] == 'yes':
            info['__Output']['SNMPv2'] = 'Green'
        else:
            info['__Output']['SNMPv2'] = 'Red'

        info['Access Community'] = snmp_mo['Access Community String']
        info['Access Level'] = snmp_mo['SNMP Community access']
        info['Trap Community'] = snmp_mo['Trap Community String']
        info['SNMPv3'] = snmp_mo['SNMP v3 Enabled']
        if info['SNMPv3'] == 'yes':
            info['__Output']['SNMPv3'] = 'Green'
        else:
            info['__Output']['SNMPv3'] = 'Red'

        info['SNMP EngineID'] = snmp_mo['SNMP Engine ID']
        info['User EngineID'] = snmp_mo['User Input EngineID']
        info['EngineID'] = info['SNMP EngineID']
        if len(info['User EngineID']) > 0:
            info['EngineID'] = '%s (user)' % (info['User EngineID'])

        return info

    def get_snmp_destination_info(self, snmp_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in snmp_mo:
            info[key] = snmp_mo[key]

        return info

    def get_snmp_user_info(self, snmp_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in snmp_mo:
            info[key] = snmp_mo[key]

        info['Enabled'] = 'no'
        if info['Security Name'] != '(n/a)':
            info['Enabled'] = 'yes'

        return info

    def get_snmp(self, cache_enabled=True):
        snmp_mo = self.get_snmp_mo(cache_enabled=cache_enabled)
        if snmp_mo is None:
            return None

        snmp_info = self.get_snmp_info(
            snmp_mo
        )

        snmp_info['Server'] = []
        snmp_destination_mo = self.get_snmp_destination_mo(keep_scope=True, cache_enabled=cache_enabled)
        if snmp_destination_mo is not None:
            for server_mo in snmp_destination_mo:
                server_info = self.get_snmp_destination_info(
                    server_mo
                )
                if server_info['Enabled'] == 'yes':
                    snmp_info['Server'].append(
                        server_info
                    )

        snmp_info['Servers'] = len(snmp_info['Server'])

        snmp_info['User'] = []
        snmp_user_mo = self.get_snmp_user_mo(keep_scope=True, cache_enabled=cache_enabled)
        if snmp_user_mo is not None:
            for user_mo in snmp_user_mo:
                user_info = self.get_snmp_user_info(
                    user_mo
                )
                if user_info['Enabled'] == 'yes':
                    snmp_info['User'].append(
                        user_info
                    )

        snmp_info['Users'] = len(snmp_info['User'])

        self.log.debug(
            'get_snmp_info',
            json.dumps(snmp_info, indent=4)
        )

        return snmp_info
