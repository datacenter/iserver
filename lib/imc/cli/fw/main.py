import json


class ImcCliFw():
    def __init__(self):
        self.fw_mo = None

    def get_fw_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.fw_mo is not None:
                return self.fw_mo

            self.fw_mo = self.get_imc_cli_cache_entry(
                'fw'
            )
            if self.fw_mo is not None:
                return self.fw_mo

        self.fw_mo = self.show_dict(
            'show firmware detail',
            start='Firmware Image Information:',
            scope='cimc'
        )

        if self.fw_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'fw',
            self.fw_mo
        )

        self.log.debug(
            'get_fw_mo',
            json.dumps(self.fw_mo, indent=4)
        )
        return self.fw_mo

    def get_fw_info(self, fw_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in fw_mo:
            info[key] = fw_mo[key]

        self.log.debug(
            'get_fw_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_fw(self, cache_enabled=True):
        fw_mo = self.get_fw_mo(cache_enabled=cache_enabled)
        if fw_mo is None:
            return None

        fw_info = self.get_fw_info(
            fw_mo
        )

        return fw_info
