import json


class ImcCliFw():
    def __init__(self):
        self.fw_mo = None

    def get_fw_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.fw_mo is not None:
                return self.fw_mo

            self.fw_mo = self.get_icm_cli_cache_entry(
                'fw'
            )
            if self.fw_mo is not None:
                return self.fw_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /cimc # show firmware detail
        # Firmware Image Information:
        #     Update Stage: NONE
        #     Update Progress: 0
        #     Current FW Version: 4.2(2a)
        #     FW Image 1 Version: 4.2(2a)
        #     FW Image 1 State: RUNNING ACTIVATED
        #     FW Image 2 Version: 4.1(3d)
        #     FW Image 2 State: BACKUP INACTIVATED
        #     Boot-loader Version: 4.2(2a)
        #     Secure Boot: ENABLED

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
