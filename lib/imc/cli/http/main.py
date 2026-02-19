import json


class ImcCliHttp():
    def __init__(self):
        self.http_mo = None

    def get_http_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.http_mo is not None:
                return self.http_mo

            self.http_mo = self.get_imc_cli_cache_entry(
                'http'
            )
            if self.http_mo is not None:
                return self.http_mo

        self.http_mo = self.show_dict(
            'show http detail',
            start='HTTP Settings:'
        )

        if self.http_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'http',
            self.http_mo
        )

        self.log.debug(
            'get_http_mo',
            json.dumps(self.http_mo, indent=4)
        )
        return self.http_mo

    def get_http_info(self, http_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in http_mo:
            info[key] = http_mo[key]

        if info['HTTP Enabled'] == 'yes':
            info['__Output']['HTTP Enabled'] = 'Green'
        else:
            info['__Output']['HTTP Enabled'] = 'Red'

        if info['HTTP Redirected'] == 'yes':
            info['__Output']['HTTP Redirected'] = 'Green'
        else:
            info['__Output']['HTTP Redirected'] = 'Red'

        if info['HTTPS Enabled'] == 'yes':
            info['__Output']['HTTPS Enabled'] = 'Green'
        else:
            info['__Output']['HTTPS Enabled'] = 'Red'

        self.log.debug(
            'get_http_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_http(self, cache_enabled=True):
        http_mo = self.get_http_mo(cache_enabled=cache_enabled)
        if http_mo is None:
            return None

        http_info = self.get_http_info(
            http_mo
        )

        return http_info
