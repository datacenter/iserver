import json


class ImcCliFlex():
    def __init__(self):
        self.flex_mo = None

    def get_flex_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.flex_mo is not None:
                return self.flex_mo

            self.flex_mo = self.get_icm_cli_cache_entry(
                'flex'
            )
            if self.flex_mo is not None:
                return self.flex_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /chassis # show flexutil detail
        # Controller Flexutil:
        #     Product Name: Cisco Flexutil
        #     Internal State: Failed
        #     Controller Status: Card is Absent
        #     Physical Drive Count: 0
        #     Virtual Drive Count: 0

        self.flex_mo = self.show_dict(
            'show flexutil detail',
            start='Controller Flexutil:',
            scope='chassis'
        )

        if self.flex_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'flex',
            self.flex_mo
        )

        self.log.debug(
            'get_flex_mo',
            json.dumps(self.flex_mo, indent=4)
        )
        return self.flex_mo

    def get_flex_info(self, flex_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in flex_mo:
            info[key] = flex_mo[key]

        self.log.debug(
            'get_flex_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_flex(self, cache_enabled=True):
        flex_mo = self.get_flex_mo(cache_enabled=cache_enabled)
        if flex_mo is None:
            return None

        flex_info = self.get_flex_info(
            flex_mo
        )

        return flex_info
