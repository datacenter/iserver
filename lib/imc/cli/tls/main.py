import json

from lib import filter_helper


class ImcCliTls():
    def __init__(self):
        self.tls_mo = None

    def get_tls_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.tls_mo is not None:
                return self.tls_mo

            self.tls_mo = self.get_imc_cli_cache_entry(
                'tls'
            )
            if self.tls_mo is not None:
                return self.tls_mo

        # comp /cimc # show tls-config detail
        # TLS Configuration:
        #     TLS Static Cipher Enabled: NA
        #     Configured TLS Version: TLSv1.2, TLSv1.3
        #     TLS Version 1.2 Enabled: yes
        #     TLS Version 1.2 Cipher Mode: High
        #     TLS Version 1.2 Cipher List: ALL:!DH:!EDH:!ADH:!EXP:!EXPORT40:!EXPORT56:!LOW:!MEDIUM:!RC4:!3DES:!SSLv2:!eNULL:!aNULL:!PSK:!SRP:!RSA:+HIGH
        #     TLS Version 1.2 Custom Status: NA
        #     TLS Version 1.3 Cipher Suite: TLS_AES_256_GCM_SHA384:TLS_AES_128_GCM_SHA256

        self.tls_mo = self.show_dict(
            'show tls-config detail',
            start='TLS Configuration:',
            scope='cimc'
        )

        if self.tls_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'tls',
            self.tls_mo
        )

        self.log.debug(
            'get_tls_mo',
            json.dumps(self.tls_mo, indent=4)
        )
        return self.tls_mo

    def get_tls_info(self, tls_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in tls_mo:
            info[key] = tls_mo[key]

        info['TLS 1.2 Cipher List'] = filter_helper.get_string_chunks(
            tls_mo['TLS Version 1.2 Cipher List'].strip(),
            40,
            extra_separator=':'
        )

        info['TLS 1.3 Cipher Suite'] = filter_helper.get_string_chunks(
            tls_mo['TLS Version 1.3 Cipher Suite'].strip(),
            40,
            extra_separator=':'
        )

        if info['TLS Version 1.2 Enabled'] == 'yes':
            info['__Output']['TLS Version 1.2 Enabled'] = 'Green'
        else:
            info['__Output']['TLS Version 1.2 Enabled'] = 'Red'

        self.log.debug(
            'get_tls_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_tls(self, cache_enabled=True):
        tls_mo = self.get_tls_mo(cache_enabled=cache_enabled)
        if tls_mo is None:
            return None

        tls_info = self.get_tls_info(
            tls_mo
        )

        return tls_info
