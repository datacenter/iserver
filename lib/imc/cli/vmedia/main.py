import json


class ImcCliVmedia():
    def __init__(self):
        self.vmedia_mo = None

    def get_vmedia_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.vmedia_mo is not None:
                return self.vmedia_mo

            self.vmedia_mo = self.get_icm_cli_cache_entry(
                'vmedia'
            )
            if self.vmedia_mo is not None:
                return self.vmedia_mo

        # comp-7-p2b-eu-spdc-WMP24040061# show vmedia detail
        # vMedia Settings:
        #     Enabled: yes
        #     Max Sessions: 1
        #     Active Sessions: 0
        #     Low Power USB Enabled: yes

        self.vmedia_mo = self.show_dict(
            'show vmedia detail',
            start='vMedia Settings:'
        )

        if self.vmedia_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'vmedia',
            self.vmedia_mo
        )

        self.log.debug(
            'get_vmedia_mo',
            json.dumps(self.vmedia_mo, indent=4)
        )
        return self.vmedia_mo

    def get_vmedia_info(self, vmedia_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in vmedia_mo:
            info[key] = vmedia_mo[key]

        self.log.debug(
            'get_vmedia_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_vmedia(self, cache_enabled=True):
        vmedia_mo = self.get_vmedia_mo(cache_enabled=cache_enabled)
        if vmedia_mo is None:
            return None

        vmedia_info = self.get_vmedia_info(
            vmedia_mo
        )

        return vmedia_info
