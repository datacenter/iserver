import json


class ImcCliIp():
    def __init__(self):
        self.network_mo = None
        self.icmp_mo = None
        self.blocking_mo = None
        self.filtering_mo = None

    def get_network_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.network_mo is not None:
                return self.network_mo

            self.network_mo = self.get_icm_cli_cache_entry(
                'network'
            )
            if self.network_mo is not None:
                return self.network_mo

        # hostname /cimc # show network detail
        # Network Setting:
        #     IPv4 Enabled: yes
        #     IPv4 Address: <ip>
        #     IPv4 Netmask: <mask>

        if keep_scope:
            self.network_mo = self.show_dict(
                'show detail',
                start='Network Setting:',
                top=False
            )
        else:
            self.network_mo = self.show_dict(
                'show detail',
                start='Network Setting:',
                scope='cimc,network'
            )

        if self.network_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'network',
            self.network_mo
        )

        self.log.debug(
            'get_network_mo',
            json.dumps(self.network_mo, indent=4)
        )
        return self.network_mo

    def get_network_info(self, network_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in network_mo:
            info[key] = network_mo[key]

        self.log.debug(
            'get_network_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_icmp_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.icmp_mo is not None:
                return self.icmp_mo

            self.icmp_mo = self.get_icm_cli_cache_entry(
                'icmp'
            )
            if self.icmp_mo is not None:
                return self.icmp_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /cimc/network # show icmp-configuration detail
        # ICMP Settings:
        #     Destination Unreachable Enabled: no
        #     Redirect Enabled: no

        if keep_scope:
            self.icmp_mo = self.show_dict(
                'show icmp-configuration detail',
                start='ICMP Settings',
                top=False
            )
        else:
            self.icmp_mo = self.show_dict(
                'show icmp-configuration detail',
                start='ICMP Settings',
                scope='cimc,network'
            )

        if self.icmp_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'icmp',
            self.icmp_mo
        )

        self.log.debug(
            'get_icmp_mo',
            json.dumps(self.icmp_mo, indent=4)
        )
        return self.icmp_mo

    def get_icmp_info(self, icmp_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in icmp_mo:
            info[key] = icmp_mo[key]

        self.log.debug(
            'get_icmp_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_blocking_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.blocking_mo is not None:
                return self.blocking_mo

            self.blocking_mo = self.get_icm_cli_cache_entry(
                'blocking'
            )
            if self.blocking_mo is not None:
                return self.blocking_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /cimc/network # show ipblocking detail
        # IP Blocking Setting:
        #     Enabled: no
        #     Fail Count: 3
        #     Fail Window: 90
        #     Blocking Time: 300

        if keep_scope:
            self.blocking_mo = self.show_dict(
                'show ipblocking detail',
                start='IP Blocking Setting:',
                top=False
            )
        else:
            self.blocking_mo = self.show_dict(
                'show ipblocking detail',
                start='IP Blocking Setting:',
                scope='cimc,network'
            )

        if self.blocking_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'blocking',
            self.blocking_mo
        )

        self.log.debug(
            'get_blocking_mo',
            json.dumps(self.blocking_mo, indent=4)
        )
        return self.blocking_mo

    def get_blocking_info(self, blocking_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in blocking_mo:
            info[key] = blocking_mo[key]

        self.log.debug(
            'get_blocking_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_filtering_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.filtering_mo is not None:
                return self.filtering_mo

            self.filtering_mo = self.get_icm_cli_cache_entry(
                'filtering'
            )
            if self.filtering_mo is not None:
                return self.filtering_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /cimc/network # show ipfiltering detail
        # IP Filter Service Settings:
        #     Enabled: no
        #     Filter 1:
        #     Filter 2:
        #     Filter 3:
        #     Filter 4:

        if keep_scope:
            self.filtering_mo = self.show_dict(
                'show ipfiltering detail',
                start='IP Filter Service Settings:',
                top=False
            )
        else:
            self.filtering_mo = self.show_dict(
                'show ipfiltering detail',
                start='IP Filter Service Settings:',
                scope='cimc,network'
            )

        if self.filtering_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'filtering',
            self.filtering_mo
        )

        self.log.debug(
            'get_filtering_mo',
            json.dumps(self.filtering_mo, indent=4)
        )
        return self.filtering_mo

    def get_filtering_info(self, filtering_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in filtering_mo:
            info[key] = filtering_mo[key]

        self.log.debug(
            'get_filtering_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_ip(self, network_info=False, icmp_info=False, blocking_info=False, filtering_info=False, cache_enabled=True):
        ip_info = {}

        self.set_scope('cimc,network')

        if network_info:
            network_mo = self.get_network_mo(
                keep_scope=True,
                cache_enabled=cache_enabled
            )
            if network_mo is not None:
                ip_info['network'] = self.get_network_info(
                    network_mo
                )

        if icmp_info:
            icmp_mo = self.get_icmp_mo(
                keep_scope=True,
                cache_enabled=cache_enabled
            )
            if icmp_mo is not None:
                ip_info['icmp'] = self.get_icmp_info(
                    icmp_mo
                )

        if blocking_info:
            blocking_mo = self.get_blocking_mo(
                keep_scope=True,
                cache_enabled=cache_enabled
            )
            if blocking_mo is not None:
                ip_info['blocking'] = self.get_blocking_info(
                    blocking_mo
                )

        if filtering_info:
            filtering_mo = self.get_filtering_mo(
                keep_scope=True,
                cache_enabled=cache_enabled
            )
            if filtering_mo is not None:
                ip_info['filtering'] = self.get_filtering_info(
                    filtering_mo
                )

        return ip_info
