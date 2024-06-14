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

            self.snmp_mo = self.get_icm_cli_cache_entry(
                'snmp'
            )
            if self.snmp_mo is not None:
                return self.snmp_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /snmp # show detail
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
        #     SNMP Engine ID: 80 00 1F 88 80 F5 6B A8 01 5F 88 12 66
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

            self.snmp_destination_mo = self.get_icm_cli_cache_entry(
                'snmp_destination'
            )
            if self.snmp_destination_mo is not None:
                return self.snmp_destination_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /snmp # show trap-destinations detail
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

            self.snmp_user_mo = self.get_icm_cli_cache_entry(
                'snmp_user'
            )
            if self.snmp_user_mo is not None:
                return self.snmp_user_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /snmp # show v3users detail
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

        for key in snmp_mo:
            info[key] = snmp_mo[key]

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
                snmp_info['Server'].append(
                    self.get_snmp_destination_info(
                        server_mo
                    )
                )

        snmp_info['User'] = []
        snmp_user_mo = self.get_snmp_user_mo(keep_scope=True, cache_enabled=cache_enabled)
        if snmp_user_mo is not None:
            for user_mo in snmp_user_mo:
                snmp_info['User'].append(
                    self.get_snmp_user_info(
                        user_mo
                    )
                )

        self.log.debug(
            'get_snmp_info',
            json.dumps(snmp_info, indent=4)
        )

        return snmp_info
