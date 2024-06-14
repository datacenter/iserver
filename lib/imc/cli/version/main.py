import json


class ImcCliVersion():
    def __init__(self):
        self.version_mo = None

    def get_version_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.version_mo is not None:
                return self.version_mo

            self.version_mo = self.get_icm_cli_cache_entry(
                'version'
            )
            if self.version_mo is not None:
                return self.version_mo

        # Firmware Version
        # --------------------
        # 4.2(2a)

        commands = [
            'show version'
        ]

        success, output = self.run_commands(
            commands
        )

        if not success:
            return None

        self.version_mo = output['show version'].split('\n')[-1]

        self.set_imc_cli_cache_entry(
            'version',
            self.version_mo
        )

        self.log.debug(
            'get_version_mo',
            json.dumps(self.version_mo, indent=4)
        )
        return self.version_mo

    def get_version_info(self, version_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip
        info['Firmware Version'] = version_mo

        self.log.debug(
            'get_version_mo',
            json.dumps(info, indent=4)
        )
        return info

    def get_version(self, cache_enabled=True):
        version_mo = self.get_version_mo(cache_enabled=cache_enabled)
        if version_mo is None:
            return None

        version_info = self.get_version_info(
            version_mo
        )

        return version_info
