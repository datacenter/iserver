import json


class ImcCliBbu():
    def __init__(self):
        self.bbu_mo = None

    def get_bbu_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.bbu_mo is not None:
                return self.bbu_mo

            self.bbu_mo = self.get_icm_cli_cache_entry(
                'bbu'
            )
            if self.bbu_mo is not None:
                return self.bbu_mo

        # Controller MRAID:
        #     BBU Type: TMM-C SuperCap
        #     BBU Health: Good
        #     BBU Status: Optimal
        #     Learn Cycle Status: Successful
        #     Charging Status: N/A
        #     Learn Mode: Auto
        #     Battery Present: true
        #     Serial Number: 26487
        #     Temperature: 20 degrees C
        #     Temperature High: false
        #     Retention Time: N/A
        #     Relative State of Charge: N/A
        #     Absolute State of Charge: N/A
        #     Capacitance: 100 %
        #     Manufacturer: LSI
        #     Date of Manufacture: 2019-12-21
        #     Firmware Version: 05668-01
        #     Design Voltage: 9.800 V
        #     Voltage: 9.734 V
        #     Current: 0.000 A
        #     Design Capacity: 374 Joules
        #     Full Capacity: N/A
        #     Remaining Capacity: N/A
        #     Pack Energy: 334 Joules
        #     Expected Margin of Error: N/A
        #     Completed Charge Cycles: N/A
        #     Learn Cycle Requested: false
        #     Next Learn Cycle: 2024-06-23 03:33
        #     Learn Cycle Active: false
        #     Learn Cycle Failed: false
        #     Learn Cycle Timeout: false
        #     I2c Errors Detected: false

        slots = self.get_storage_adapter_slots()
        if slots is None:
            return None

        output = ''
        for slot in slots:
            commands = [
                'top',
                'scope chassis',
                'scope storageadapter %s' % (slot),
                'show bbu detail'
            ]

            success, slot_output = self.run_commands(
                commands
            )

            if not success:
                return None

            output = output + slot_output['show bbu detail']

        self.bbu_mo = self.parse_list(
            output,
            'Controller',
            'Controller',
            method='last word'
        )

        if self.bbu_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'bbu',
            self.bbu_mo
        )

        self.log.debug(
            'get_bbu_mo',
            json.dumps(self.bbu_mo, indent=4)
        )
        return self.bbu_mo

    def get_bbu_info(self, bbu_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in bbu_mo:
            info[key] = bbu_mo[key]

        if 'BBU Health' in info:
            if info['BBU Health'] == 'Good':
                info['__Output']['BBU Health'] = 'Green'
            else:
                info['__Output']['BBU Health'] = 'Red'

        if 'BBU Status' in info:
            if info['BBU Status'] == 'Optimal':
                info['__Output']['BBU Status'] = 'Green'
            else:
                info['__Output']['BBU Status'] = 'Red'

        info['__Key'] = 'Controller'
        info['__Value'] = info[info['__Key']]

        self.log.debug(
            'get_bbu_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_bbu(self, cache_enabled=True):
        bbus_mo = self.get_bbu_mo(cache_enabled=cache_enabled)
        if bbus_mo is None:
            return None

        bbus_info = []

        for bbu_mo in bbus_mo:
            bbus_info.append(
                self.get_bbu_info(
                    bbu_mo
                )
            )

        return bbus_info
