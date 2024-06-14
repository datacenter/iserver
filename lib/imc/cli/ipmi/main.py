import json


class ImcCliIpmi():
    def __init__(self):
        self.ipmi_mo = None

    def get_ipmi_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.ipmi_mo is not None:
                return self.ipmi_mo

            self.ipmi_mo = self.get_icm_cli_cache_entry(
                'ipmi'
            )
            if self.ipmi_mo is not None:
                return self.ipmi_mo

        # comp-7-p2b-eu-spdc-WMP24040061# show ipmi detail
        # IPMI over LAN Settings:
        #     Enabled: no
        #     Encryption Key: 0000000000000000000000000000000000000000
        #     Privilege Level Limit: admin

        self.ipmi_mo = self.show_dict(
            'show ipmi detail',
            start='IPMI over LAN Settings:'
        )

        if self.ipmi_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'ipmi',
            self.ipmi_mo
        )

        self.log.debug(
            'get_ipmi_mo',
            json.dumps(self.ipmi_mo, indent=4)
        )
        return self.ipmi_mo

    def get_ipmi_info(self, ipmi_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in ipmi_mo:
            info[key] = ipmi_mo[key]

        self.log.debug(
            'get_ipmi_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_ipmi(self, cache_enabled=True):
        ipmi_mo = self.get_ipmi_mo(cache_enabled=cache_enabled)
        if ipmi_mo is None:
            return None

        ipmi_info = self.get_ipmi_info(
            ipmi_mo
        )

        return ipmi_info
