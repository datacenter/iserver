import json


class ImcCliChassis():
    def __init__(self):
        self.chassis_mo = None

    def get_chassis_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.chassis_mo is not None:
                return self.chassis_mo

            self.chassis_mo = self.get_icm_cli_cache_entry(
                'chassis'
            )
            if self.chassis_mo is not None:
                return self.chassis_mo

        # Chassis:
        #     Power: on
        #     Serial Number: WMP24040061
        #     Product Name: UCS C220 M5SX
        #     PID : UCSC-C220-M5SX
        #     UUID: B947D1F9-F0A0-4D6F-AF63-16A48DD0A96E
        #     Locator LED: off
        #     Description: comp-7-p2b-eu-spdc-WMP24040061
        #     Asset Tag: 022C32A
        #     Post Completion Status: Completed

        self.chassis_mo = self.show_dict(
            'show chassis detail',
            start='Chassis:'
        )

        if self.chassis_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'chassis',
            self.chassis_mo
        )

        self.log.debug(
            'get_chassis_mo',
            json.dumps(self.chassis_mo, indent=4)
        )
        return self.chassis_mo

    def get_chassis_info(self, chassis_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in chassis_mo:
            info[key] = chassis_mo[key]

        self.log.debug(
            'get_chassis_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_chassis(self, version_info=True, cache_enabled=True):
        chassis_mo = self.get_chassis_mo(cache_enabled=cache_enabled)
        if chassis_mo is None:
            return None

        chassis_info = self.get_chassis_info(
            chassis_mo
        )

        if version_info:
            version = self.get_version(
                cache_enabled=cache_enabled
            )
            if version is not None:
                chassis_info['Firmware Version'] = version['Firmware Version']

        return chassis_info

    def power_cycle(self):
        commands = []
        commands.append('top')
        commands.append('scope chassis')
        commands.append('power cycle')

        success, output = self.run_commands(
            commands,
            continue_prompt=True
        )

        return success
