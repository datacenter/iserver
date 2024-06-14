import json


class ImcCliAdapter():
    def __init__(self):
        self.adapter_mo = None

    def get_adapter_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.adapter_mo is not None:
                return self.adapter_mo

            self.adapter_mo = self.get_icm_cli_cache_entry(
                'adapter'
            )
            if self.adapter_mo is not None:
                return self.adapter_mo

        # PCI Slot MLOM:
        #     Product Name: UCS VIC 1457
        #     Serial Number: FCH24157D1V
        #     Product ID: UCSC-MLOM-C25Q-04
        #     Adapter Hardware Revision: 5
        #     Current FW Version: 5.2(2b)
        #     VNTAG: Disabled
        #     FIP: Disabled
        #     LLDP: Disabled
        #     PORT CHANNEL: Disabled
        #     Physical NIC Mode (Experimental): Disabled
        #     Configuration Pending: no
        #     Cisco IMC Management Enabled: no
        #     VID: V05
        #     Vendor: Cisco Systems Inc
        #     Description:
        #     Bootloader Version: 5.0(2a)
        #     FW Image 1 Version: 5.2(2b)
        #     FW Image 1 State: RUNNING ACTIVATED
        #     FW Image 2 Version: 5.1(3d)
        #     FW Image 2 State: BACKUP INACTIVATED
        #     FW Update Status: Fwupdate never issued
        #     FW Update Error: No error
        #     FW Update Stage: No operation (0%)
        #     FW Update Overall Progress: 0%

        self.adapter_mo = self.show_list(
            'show adapter detail',
            'PCI Slot',
            'Slot',
            method='last word',
            scope='chassis'
        )

        if self.adapter_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'adapter',
            self.adapter_mo
        )

        self.log.debug(
            'get_adapter_mo',
            json.dumps(self.adapter_mo, indent=4)
        )
        return self.adapter_mo

    def get_adapter_info(self, adapter_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in adapter_mo:
            info[key] = adapter_mo[key]

        info['__Key'] = 'Slot'
        info['__Value'] = info[info['__Key']]

        self.log.debug(
            'get_adapter_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_adapter(self, cache_enabled=True):
        adapters_mo = self.get_adapter_mo(cache_enabled=cache_enabled)
        if adapters_mo is None:
            return None

        adapters_info = []

        for adapter_mo in adapters_mo:
            adapters_info.append(
                self.get_adapter_info(
                    adapter_mo
                )
            )

        return adapters_info

    def get_adapter_slots(self, cache_enabled=True):
        adapters = self.get_adapter(
            cache_enabled=cache_enabled
        )
        if adapters is None:
            return None

        slots = []
        for adapter in adapters:
            slots.append(
                adapter['Slot']
            )

        return slots
