import json


class ImcCliRedfish():
    def __init__(self):
        self.redfish_mo = None

    def get_redfish_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.redfish_mo is not None:
                return self.redfish_mo

            self.redfish_mo = self.get_icm_cli_cache_entry(
                'redfish'
            )
            if self.redfish_mo is not None:
                return self.redfish_mo

        # comp-7-p2b-eu-spdc-WMP24040061# show redfish detail
        # REDFISH Settings:
        #     Enabled: yes
        #     Active Sessions: 0
        #     Max Sessions: 4

        self.redfish_mo = self.show_dict(
            'show redfish detail',
            start='REDFISH Settings:'
        )

        if self.redfish_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'redfish',
            self.redfish_mo
        )

        self.log.debug(
            'get_redfish_mo',
            json.dumps(self.redfish_mo, indent=4)
        )
        return self.redfish_mo

    def get_redfish_info(self, redfish_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in redfish_mo:
            info[key] = redfish_mo[key]

        self.log.debug(
            'get_redfish_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_redfish(self, cache_enabled=True):
        redfish_mo = self.get_redfish_mo(cache_enabled=cache_enabled)
        if redfish_mo is None:
            return None

        redfish_info = self.get_redfish_info(
            redfish_mo
        )

        return redfish_info

    def enable_redfish(self):
        commands = [
            'scope redfish',
            'set enabled yes',
            'commit'
        ]

        success, output = self.run_commands(
            commands
        )

        return success

    def disable_redfish(self):
        commands = [
            'scope redfish',
            'set enabled no',
            'commit'
        ]

        success, output = self.run_commands(
            commands
        )

        return success