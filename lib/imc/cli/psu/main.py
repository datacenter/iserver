import json


class ImcCliPsu():
    def __init__(self):
        self.psu_mo = None

    def get_psu_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.psu_mo is not None:
                return self.psu_mo

            self.psu_mo = self.get_icm_cli_cache_entry(
                'psu'
            )
            if self.psu_mo is not None:
                return self.psu_mo

        # Name PSU1:
        #     In. Power (Watts): 150
        #     Out. Power (Watts): 123
        #     Firmware : 10252046
        #     Status : Present
        #     Product ID : UCSC-PSU1-1050W
        # Name PSU2:
        #     In. Power (Watts): 146
        #     Out. Power (Watts): 122
        #     Firmware : 10252046
        #     Status : Present
        #     Product ID : UCSC-PSU1-1050W

        self.psu_mo = self.show_list(
            'show psu detail',
            'Name',
            'Name',
            method='last word',
            scope='chassis'
        )

        if self.psu_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'psu',
            self.psu_mo
        )

        self.log.debug(
            'get_psu_mo',
            json.dumps(self.psu_mo, indent=4)
        )
        return self.psu_mo

    def get_psu_info(self, psu_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in psu_mo:
            info[key] = psu_mo[key]

        if 'Status' in info:
            if info['Status'] == 'Present':
                info['__Output']['Status'] = 'Green'
            else:
                info['__Output']['Status'] = 'Red'

        info['__Key'] = 'Name'
        info['__Value'] = info[info['__Key']]

        self.log.debug(
            'get_psu_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_psu(self, cache_enabled=True):
        psus_mo = self.get_psu_mo(cache_enabled=cache_enabled)
        if psus_mo is None:
            return None

        psus_info = []

        for psu_mo in psus_mo:
            psus_info.append(
                self.get_psu_info(
                    psu_mo
                )
            )

        return psus_info
