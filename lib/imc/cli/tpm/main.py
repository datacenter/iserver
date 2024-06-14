import json


class ImcCliTpm():
    def __init__(self):
        self.tpm_mo = None

    def get_tpm_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.tpm_mo is not None:
                return self.tpm_mo

            self.tpm_mo = self.get_icm_cli_cache_entry(
                'tpm'
            )
            if self.tpm_mo is not None:
                return self.tpm_mo

        # Version NA:
        #     Presence: empty
        #     Enabled-Status: unknown
        #     Active-Status: unknown
        #     Ownership: unknown
        #     Revision: NA
        #     Model: NA
        #     Vendor: NA
        #     Serial: NA
        #     Firmare Version : NA

        self.tpm_mo = self.show_dict(
            'show tpm-inventory detail',
            start='Version ',
            scope='chassis'
        )

        if self.tpm_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'tpm',
            self.tpm_mo
        )

        self.log.debug(
            'get_tpm_mo',
            json.dumps(self.tpm_mo, indent=4)
        )
        return self.tpm_mo

    def get_tpm_info(self, tpm_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in tpm_mo:
            info[key] = tpm_mo[key]

        self.log.debug(
            'get_tpm_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_tpm(self, cache_enabled=True):
        tpm_mo = self.get_tpm_mo(cache_enabled=cache_enabled)
        if tpm_mo is None:
            return None

        tpm_info = self.get_tpm_info(
            tpm_mo
        )

        return tpm_info
