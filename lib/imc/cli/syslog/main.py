import json


class ImcCliSyslog():
    def __init__(self):
        self.syslog_mo = None
        self.syslog_server_mo = None

    def get_syslog_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.syslog_mo is not None:
                return self.syslog_mo

            self.syslog_mo = self.get_icm_cli_cache_entry(
                'syslog'
            )
            if self.syslog_mo is not None:
                return self.syslog_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /cimc/log # show detail
        # LOG:
        #     Local Syslog Severity: debug
        #     Remote Syslog Severity: warning
        #     Log User Name on Failed Login: disabled

        self.syslog_mo = self.show_dict(
            'show detail',
            start='LOG:',
            scope='cimc,log'
        )

        if self.syslog_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'syslog',
            self.syslog_mo
        )

        self.log.debug(
            'get_syslog_mo',
            json.dumps(self.syslog_mo, indent=4)
        )
        return self.syslog_mo

    def get_syslog_server_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.syslog_server_mo is not None:
                return self.syslog_server_mo

            self.syslog_server_mo = self.get_icm_cli_cache_entry(
                'syslog_server'
            )
            if self.syslog_server_mo is not None:
                return self.syslog_server_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /cimc/log # show server detail
        # Syslog Server 1:
        #     Syslog Server Address: <ip>
        #     Syslog Server Port: 5140
        #     Enabled: yes
        #     Syslog Server protocol: udp
        #     Secure Remote Syslog Enabled: no
        #     Certificate Exists: no
        # Syslog Server 2:
        #     Syslog Server Address: <ip>
        #     Syslog Server Port: 514
        #     Enabled: no
        #     Syslog Server protocol: udp
        #     Secure Remote Syslog Enabled: no
        #     Certificate Exists: no

        if keep_scope:
            self.syslog_server_mo = self.show_list(
                'show server detail',
                'Syslog Server __INDEX__:',
                None,
                method='last word',
                top=False
            )
        else:
            self.syslog_server_mo = self.show_list(
                'show server detail',
                'Syslog Server __INDEX__:',
                None,
                method='last word',
                scope='cimc,log'
            )

        if self.syslog_server_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'syslog_server',
            self.syslog_server_mo
        )

        self.log.debug(
            'get_syslog_server_mo',
            json.dumps(self.syslog_server_mo, indent=4)
        )
        return self.syslog_server_mo

    def get_syslog_info(self, syslog_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in syslog_mo:
            info[key] = syslog_mo[key]

        return info

    def get_syslog_server_info(self, syslog_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in syslog_mo:
            info[key] = syslog_mo[key]

        return info

    def get_syslog(self, cache_enabled=True):
        syslog_mo = self.get_syslog_mo(cache_enabled=cache_enabled)
        if syslog_mo is None:
            return None

        syslog_info = self.get_syslog_info(
            syslog_mo
        )
        syslog_info['Server'] = []

        syslog_server_mo = self.get_syslog_server_mo(keep_scope=True, cache_enabled=cache_enabled)
        if syslog_server_mo is not None:
            for server_mo in syslog_server_mo:
                syslog_info['Server'].append(
                    self.get_syslog_server_info(
                        server_mo
                    )
                )

        self.log.debug(
            'get_syslog_info',
            json.dumps(syslog_info, indent=4)
        )

        return syslog_info
