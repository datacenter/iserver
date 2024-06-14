import json
from lib import filter_helper


class ImcCliBios():
    def __init__(self):
        self.bios_mo = None
        self.bios_params_mo = None

    def get_bios_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.bios_mo is not None:
                return self.bios_mo

            self.bios_mo = self.get_icm_cli_cache_entry(
                'bios'
            )
            if self.bios_mo is not None:
                return self.bios_mo

        # BIOS:
        #     BIOS Version: C220M5.4.2.2b.0.0613220203
        #     Backup BIOS Version: C220M5.4.1.3i.0.0713210713
        #     Boot Order: HDD
        #     FW Update Status: None, OK
        #     UEFI Secure Boot: disabled
        #     Configured Boot Mode: Uefi
        #     Actual Boot Mode: Uefi
        #     Last Configured Boot Order Source: CIMC
        #     One time boot device: (none)

        self.bios_mo = self.show_dict(
            'show bios detail',
            start='BIOS:'
        )

        if self.bios_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'bios',
            self.bios_mo
        )

        self.log.debug(
            'get_bios_mo',
            json.dumps(self.bios_mo, indent=4)
        )

        return self.bios_mo

    def get_bios_params_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.bios_params_mo is not None:
                return self.bios_params_mo

            self.bios_params_mo = self.get_icm_cli_cache_entry(
                'bios_params'
            )
            if self.bios_params_mo is not None:
                return self.bios_params_mo

        # Set-up parameters:
        #     Intel VTD ATS support: Enabled
        #     All Onboard LOM Ports: Enabled
        #     Intel VTD Coherency Support: Disabled

        self.bios_params_mo = {}
        param_types = [
            'input-output',
            'memory',
            'power-or-performance',
            'processor',
            'security',
            'server-management'
        ]
        self.set_scope('bios')
        for param_type in param_types:
            self.bios_params_mo[param_type] = []
            bios_params = self.show_dict(
                'show %s detail' % (param_type),
                start='Set-up parameters:',
                top=False
            )
            if bios_params is not None:
                for bios_param in bios_params:
                    bios_param_mo = {}
                    bios_param_mo[bios_param] = bios_params[bios_param]
                    self.bios_params_mo[param_type].append(
                        bios_param_mo
                    )

        self.set_imc_cli_cache_entry(
            'bios_params',
            self.bios_params_mo
        )

        self.log.debug(
            'get_bios_mo',
            json.dumps(self.bios_params_mo, indent=4)
        )

        return self.bios_params_mo

    def get_bios_info(self, bios_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in bios_mo:
            info[key] = bios_mo[key]

        self.log.debug(
            'get_bios_info',
            json.dumps(info, indent=4)
        )

        return info

    def get_bios_params_info(self, bios_mo, key_filter=None, type_filter=None):
        info = {}

        for key in bios_mo:
            if type_filter is not None and len(type_filter) > 0:
                is_match = False
                for item in type_filter:
                    is_match = is_match or filter_helper.match_string('*%s*' % (item), key)

                if not is_match:
                    continue

            info[key] = {}
            info[key]['__Output'] = {}
            info[key]['__IP'] = self.endpoint_ip

            for item in bios_mo[key]:
                for ikey in item:
                    if key_filter is not None and len(key_filter) > 0:
                        is_match = False
                        for key_filter_item in key_filter:
                            is_match = is_match or filter_helper.match_string('*%s*' % (key_filter_item), ikey)

                        if not is_match:
                            continue

                    info[key][ikey] = item[ikey]

            if len(info[key]) == 2:
                del info[key]

        self.log.debug(
            'get_bios_param_info',
            json.dumps(info, indent=4)
        )

        return info

    def get_bios(self, key_filter=None, type_filter=None, state_info=True, params_info=True, cache_enabled=True):
        bios_info = {}

        if state_info:
            bios_mo = self.get_bios_mo(cache_enabled=cache_enabled)
            if bios_mo is None:
                return None

            bios_info['state'] = self.get_bios_info(
                bios_mo
            )

        if params_info:
            bios_params_mo = self.get_bios_params_mo(cache_enabled=cache_enabled)
            if bios_params_mo is None:
                return None

            bios_info['params'] = self.get_bios_params_info(
                bios_params_mo,
                key_filter=key_filter,
                type_filter=type_filter
            )

        return bios_info
