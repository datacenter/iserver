import json


class ImcCliDimm():
    def __init__(self):
        self.dimm_mo = None
        self.dimm_pid_mo = None

    def get_dimm_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.dimm_mo is not None:
                return self.dimm_mo

            self.dimm_mo = self.get_icm_cli_cache_entry(
                'dimm'
            )
            if self.dimm_mo is not None:
                return self.dimm_mo

        # Name DIMM_L1:
        #     Capacity: 32768 MB
        #     Channel Speed (MHz): 2933
        #     Channel Type: DDR4
        #     Memory Type Detail: Synchronous Registered (Buffered)
        #     Bank Locator: NODE 1 CHANNEL 4 DIMM 0
        #     Visibility: Yes
        #     Operability: Operable
        #     Manufacturer: 0x2C00
        #     Part Number: 36ASF4G72PZ-2G9E2
        #     Serial Number: F0F73494
        #     Asset Tag: 252006 (Mfg Location:0x25, Mfg Year:20, Mfg Week:06)
        #     Data Width: 64 bits

        self.dimm_mo = self.show_list(
            'show dimm detail',
            'Name',
            'Name',
            method='last word',
            scope='chassis'
        )

        if self.dimm_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'dimm',
            self.dimm_mo
        )

        self.log.debug(
            'get_dimm_mo',
            json.dumps(self.dimm_mo, indent=4)
        )
        return self.dimm_mo

    def get_dimm_pid_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.dimm_pid_mo is not None:
                return self.dimm_pid_mo

            self.dimm_pid_mo = self.get_icm_cli_cache_entry(
                'dimm_pid'
            )
            if self.dimm_pid_mo is not None:
                return self.dimm_pid_mo

        # Name DIMM_M1:
        #     Description: 32GB DDR4-2933-MHz RDIMM/2Rx4/1.2v
        #     Product ID: UCS-MR-X32G2RT-H
        #     Vendor ID: 0xCE00
        #     Vendor Name: Samsung
        #     Model: M393A4K40CB2-CVF
        #     SerialNumber: 120AD606
        #     Operability: Operable
        #     Capacity: 32768 MB
        #     Speed: 2933
        #     Data Width: 64 bits

        self.dimm_pid_mo = self.show_list(
            'show dimm-pid detail',
            'Name',
            'Name',
            method='last word',
            scope='chassis'
        )

        if self.dimm_pid_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'dimm_pid',
            self.dimm_pid_mo
        )
        self.log.debug(
            'get_dimm_pid_mo',
            json.dumps(self.dimm_pid_mo, indent=4)
        )
        return self.dimm_pid_mo

    def get_dimm_info(self, dimm_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in dimm_mo:
            info[key] = dimm_mo[key]

        if 'Operability' in info:
            if info['Operability'] == 'Operable':
                info['__Output']['Operability'] = 'Green'
            else:
                info['__Output']['Operability'] = 'Red'

        info['__Key'] = 'Name'
        info['__Value'] = info[info['__Key']]

        return info

    def get_dimm_pid_info(self, dimm_mo):
        info = {}
        for key in dimm_mo:
            info[key] = dimm_mo[key]
        return info

    def get_dimm(self, cache_enabled=True):
        dimms_mo = self.get_dimm_mo(cache_enabled=cache_enabled)
        if dimms_mo is None:
            return None

        dimms_pid_mo = self.get_dimm_pid_mo(cache_enabled=cache_enabled)
        if dimms_pid_mo is None:
            return None

        dimms_info = []

        for dimm_mo in dimms_mo:
            dimms_info.append(
                self.get_dimm_info(
                    dimm_mo
                )
            )

        keys = [
            'Description',
            'Product ID',
            'Vendor ID',
            'Vendor Name',
            'Model'
        ]
        for dimm_info in dimms_info:
            for key in keys:
                dimm_info[key] = 'NA'

        for dimm_pid_mo in dimms_pid_mo:
            dimm_pid_info = self.get_dimm_pid_info(
                dimm_pid_mo
            )
            for dimm_info in dimms_info:
                if dimm_info['Name'] == dimm_pid_info['Name']:
                    for key in keys:
                        dimm_info[key] = dimm_pid_info[key]

        self.log.debug(
            'get_dimm_info',
            json.dumps(dimms_info, indent=4)
        )

        return dimms_info
