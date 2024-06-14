import json


class ImcCliNtp():
    def __init__(self):
        self.ntp_mo = None

    def get_ntp_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.ntp_mo is not None:
                return self.ntp_mo

            self.ntp_mo = self.get_icm_cli_cache_entry(
                'ntp'
            )
            if self.ntp_mo is not None:
                return self.ntp_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /cimc/network # show ntp detail
        # NTP Service Settings:
        #     Enabled: yes
        #     Server 1: <fqdn>
        #     Server 2:
        #     Server 3:
        #     Server 4:
        #     Status: ok

        self.ntp_mo = self.show_dict(
            'show ntp detail',
            start='NTP Service Settings:',
            scope='cimc,network'
        )

        if self.ntp_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'ntp',
            self.ntp_mo
        )


        self.log.debug(
            'get_ntp_mo',
            json.dumps(self.ntp_mo, indent=4)
        )
        return self.ntp_mo

    def get_ntp_info(self, ntp_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in ntp_mo:
            info[key] = ntp_mo[key]

        self.log.debug(
            'get_ntp_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_ntp(self, cache_enabled=True):
        ntp_mo = self.get_ntp_mo(cache_enabled=cache_enabled)
        if ntp_mo is None:
            return None

        ntp_info = self.get_ntp_info(
            ntp_mo
        )

        return ntp_info
