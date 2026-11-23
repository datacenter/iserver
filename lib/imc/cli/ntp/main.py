import json


class ImcCliNtp():
    def __init__(self):
        self.ntp_mo = None

    def get_ntp_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.ntp_mo is not None:
                return self.ntp_mo

            self.ntp_mo = self.get_imc_cli_cache_entry(
                'ntp'
            )
            if self.ntp_mo is not None:
                return self.ntp_mo

        # com /cimc/network # show ntp detail
        # NTP Service Settings:
        #     Enabled: yes
        #     Server 1: <fqdn>
        #     Server 2:
        #     Server 3:
        #     Server 4:
        #     Status: ok

        self.ntp_mo = self.show_dict(
            'show ntp detail',
            start='NTP Service Settings:',
            scope='cimc,network'
        )

        if self.ntp_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'ntp',
            self.ntp_mo
        )


        self.log.debug(
            'get_ntp_mo',
            json.dumps(self.ntp_mo, indent=4)
        )
        return self.ntp_mo

    def get_ntp_info(self, ntp_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        info['Enabled'] = ntp_mo['Enabled']
        if info['Enabled'] == 'yes':
            info['__Output']['Enabled'] = 'Green'
        else:
            info['__Output']['Enabled'] = 'Red'

        info['Server'] = []
        for index in range(1, 5):
            server_id = 'Server %s' % (index)
            if server_id in ntp_mo and len(ntp_mo[server_id]) > 0:
                info['Server'].append(
                    ntp_mo[server_id]
                )

        info['Status'] = ntp_mo['Status']
        if info['Status'] == 'ok':
            info['__Output']['Status'] = 'Green'
        else:
            info['__Output']['Status'] = 'Red'

        self.log.debug(
            'get_ntp_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_ntp(self, cache_enabled=True):
        ntp_mo = self.get_ntp_mo(cache_enabled=cache_enabled)
        if ntp_mo is None:
            return None

        ntp_info = self.get_ntp_info(
            ntp_mo
        )

        return ntp_info
