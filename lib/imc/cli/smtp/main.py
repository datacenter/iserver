import json


class ImcCliSmtp():
    def __init__(self):
        self.smtp_mo = None

    def get_smtp_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.smtp_mo is not None:
                return self.smtp_mo

            self.smtp_mo = self.get_icm_cli_cache_entry(
                'smtp'
            )
            if self.smtp_mo is not None:
                return self.smtp_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /smtp # show detail
        # SMTP Setting:
        #     Enabled: no
        #     Port Number: 25
        #     Server Address:
        #     From Address:
        #     Recipient1:
        #         Mail-ID  :
        #         Reachable: na
        #         Minimum Severity to Report: critical
        #     Recipient2:
        #         Mail-ID  :
        #         Reachable: na
        #         Minimum Severity to Report: critical
        #     Recipient3:
        #         Mail-ID  :
        #         Reachable: na
        #         Minimum Severity to Report: critical
        #     Recipient4:
        #         Mail-ID  :
        #         Reachable: na
        #         Minimum Severity to Report: critical

        commands = [
            'top',
            'scope smtp',
            'show detail'
        ]

        success, output = self.run_commands(
            commands
        )

        if not success:
            return None

        self.smtp_mo = self.parse_dict(
            output['show detail'],
            start='SMTP Setting:',
            ignore_start='Recipient'
        )

        if self.smtp_mo is None:
            return None

        self.smtp_mo['Recipient'] = self.parse_list(
            output['show detail'],
            'Recipient',
            'Recipient',
            method='all'
        )

        self.set_imc_cli_cache_entry(
            'smtp',
            self.smtp_mo
        )

        self.log.debug(
            'get_smtp_mo',
            json.dumps(self.smtp_mo, indent=4)
        )
        return self.smtp_mo

    def get_smtp_info(self, smtp_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in smtp_mo:
            info[key] = smtp_mo[key]

        self.log.debug(
            'get_smtp_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_smtp(self, cache_enabled=True):
        smtp_mo = self.get_smtp_mo(cache_enabled=cache_enabled)
        if smtp_mo is None:
            return None

        smtp_info = self.get_smtp_info(
            smtp_mo
        )

        return smtp_info
