import json


class ImcCliPci():
    def __init__(self):
        self.pci_mo = None
        self.pci_pid_mo = None

    def get_pci_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.pci_mo is not None:
                return self.pci_mo

            self.pci_mo = self.get_icm_cli_cache_entry(
                'pci'
            )
            if self.pci_mo is not None:
                return self.pci_mo

        # Slot 1:
        #     Vendor ID: 0x8086
        #     Device ID: 0x158b
        #     SubVendor ID: 0x1137
        #     SubDevice ID: 0x0225
        #     Firmware Version: 0x8000B900-1.826.0
        #     Product Name: Cisco(R) Ethernet Converged NIC XXV710-DA2
        #     Option ROM Status : Not-Loaded

        self.pci_mo = self.show_list(
            'show pci-adapter detail',
            'Slot',
            'Slot',
            method='last word',
            scope='chassis'
        )

        if self.pci_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'pci',
            self.pci_mo
        )

        self.log.debug(
            'get_pci_mo',
            json.dumps(self.pci_mo, indent=4)
        )
        return self.pci_mo

    def get_pci_pid_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.pci_pid_mo is not None:
                return self.pci_pid_mo

            self.pci_pid_mo = self.get_icm_cli_cache_entry(
                'pci_pid'
            )
            if self.pci_pid_mo is not None:
                return self.pci_pid_mo

        # Slot 1:
        #     Description: Cisco(R) Ethernet Converged NIC XXV710-DA2
        #     Product ID: UCSC-PCIE-ID25GF
        #     Vendor ID: 0x8086
        #     Device ID: 0x158b
        #     SubVendor ID: 0x1137
        #     SubDevice ID: 0x0225

        self.pci_pid_mo = self.show_list(
            'show pciadapter-pid detail',
            'Slot',
            'Slot',
            method='last word',
            scope='chassis'
        )

        if self.pci_pid_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'pci_pid',
            self.pci_pid_mo
        )

        self.log.debug(
            'get_pci_pid_mo',
            json.dumps(self.pci_pid_mo, indent=4)
        )
        return self.pci_pid_mo

    def get_pci_info(self, pci_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in pci_mo:
            info[key] = pci_mo[key]

        info['__Key'] = 'Slot'
        info['__Value'] = info[info['__Key']]

        return info

    def get_pci_pid_info(self, pci_mo):
        info = {}
        for key in pci_mo:
            info[key] = pci_mo[key]
        return info

    def get_pci(self, cache_enabled=True):
        pcis_mo = self.get_pci_mo(cache_enabled=cache_enabled)
        if pcis_mo is None:
            return None

        pcis_pid_mo = self.get_pci_pid_mo(cache_enabled=cache_enabled)
        if pcis_pid_mo is None:
            return None

        pcis_info = []

        for pci_mo in pcis_mo:
            pcis_info.append(
                self.get_pci_info(
                    pci_mo
                )
            )

        keys = [
            'Description',
            'Product ID'
        ]
        for pci_info in pcis_info:
            for key in keys:
                pci_info[key] = ''

        for pci_pid_mo in pcis_pid_mo:
            pci_pid_info = self.get_pci_pid_info(
                pci_pid_mo
            )
            for pci_info in pcis_info:
                if pci_info['Slot'] == pci_pid_info['Slot']:
                    for key in keys:
                        pci_info[key] = pci_pid_info[key]

        self.log.debug(
            'get_pci_info',
            json.dumps(pcis_info, indent=4)
        )
        return pcis_info
