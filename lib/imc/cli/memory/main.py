import json


class ImcCliMemory():
    def __init__(self):
        self.memory_mo = None

    def get_memory_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.memory_mo is not None:
                return self.memory_mo

            self.memory_mo = self.get_icm_cli_cache_entry(
                'memory'
            )
            if self.memory_mo is not None:
                return self.memory_mo

        # DIMM Summary:
        #     Memory Speed: 2933 MHz
        #     Total Memory: 393216 MB
        #     Effective Memory: 393216 MB
        #     Redundant Memory: 0 MB
        #     Failed Memory: 0 MB
        #     Ignored Memory: 0 MB
        #     Number of Ignored Dimms: 0
        #     Number of Failed Dimms: 0
        #     Memory RAS possible: MaximumPerformance Mirroring PartialMirror
        #     Memory Configuration: MaximumPerformance

        self.memory_mo = self.show_dict(
            'show dimm-summary',
            start='DIMM Summary:',
            scope='chassis'
        )

        if self.memory_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'memory',
            self.memory_mo
        )

        self.log.debug(
            'get_memory_mo',
            json.dumps(self.memory_mo, indent=4)
        )
        return self.memory_mo

    def get_memory_info(self, memory_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in memory_mo:
            info[key] = memory_mo[key]

        self.log.debug(
            'get_memory_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_memory(self, cache_enabled=True):
        memory_mo = self.get_memory_mo(cache_enabled=cache_enabled)
        if memory_mo is None:
            return None

        memory_info = self.get_memory_info(
            memory_mo
        )

        return memory_info
