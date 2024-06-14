import json


class ImcCliSel():
    def __init__(self):
        self.sel_mo = None

    def get_sel_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.sel_mo is not None:
                return self.sel_mo

            self.sel_mo = self.get_icm_cli_cache_entry(
                'sel'
            )
            if self.sel_mo is not None:
                return self.sel_mo

        # comp-7-p2b-eu-spdc-WMP24040061# show sel detail
        # SEL Information:
        #     No of Entries: 3008
        #     Max Entries: 3008
        #     Percent Used: 100
        #     Capacity: low

        self.sel_mo = self.show_dict(
            'show sel detail',
            start='SEL Information:'
        )

        if self.sel_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'sel',
            self.sel_mo
        )

        self.log.debug(
            'get_sel_mo',
            json.dumps(self.sel_mo, indent=4)
        )
        return self.sel_mo

    def get_sel_info(self, sel_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in sel_mo:
            info[key] = sel_mo[key]

        self.log.debug(
            'get_sel_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_sel(self, cache_enabled=True):
        sel_mo = self.get_sel_mo(cache_enabled=cache_enabled)
        if sel_mo is None:
            return None

        sel_info = self.get_sel_info(
            sel_mo
        )

        return sel_info
