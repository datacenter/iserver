import json


class ImcCliStorageAdapter():
    def __init__(self):
        self.storage_adapter_mo = None

    def get_storage_adapter_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_adapter_mo is not None:
                return self.storage_adapter_mo

            self.storage_adapter_mo = self.get_imc_cli_cache_entry(
                'storage_adapter'
            )
            if self.storage_adapter_mo is not None:
                return self.storage_adapter_mo

        self.storage_adapter_mo = self.show_list(
            'show storageadapter detail',
            'PCI Slot',
            'Slot',
            method='last word',
            scope='chassis'
        )

        if self.storage_adapter_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'storage_adapter',
            self.storage_adapter_mo
        )

        self.log.debug(
            'get_storage_adapter_mo',
            json.dumps(self.storage_adapter_mo, indent=4)
        )
        return self.storage_adapter_mo

    def get_storage_adapter_info(self, storage_adapter_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in storage_adapter_mo:
            info[key] = storage_adapter_mo[key]

        if 'Health' in info:
            if info['Health'] == 'Good':
                info['__Output']['Health'] = 'Green'
            else:
                info['__Output']['Health'] = 'Red'

        if 'Controller Status' in info:
            if info['Controller Status'] == 'Optimal':
                info['__Output']['Controller Status'] = 'Green'
            else:
                info['__Output']['Controller Status'] = 'Red'

        info['__Key'] = 'Slot'
        info['__Value'] = info[info['__Key']]

        self.log.debug(
            'get_storage_adapter_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_storage_adapter(self, cache_enabled=True):
        storage_adapters_mo = self.get_storage_adapter_mo(cache_enabled=cache_enabled)
        if storage_adapters_mo is None:
            return None

        storage_adapters_info = []

        for storage_adapter_mo in storage_adapters_mo:
            storage_adapters_info.append(
                self.get_storage_adapter_info(
                    storage_adapter_mo
                )
            )

        return storage_adapters_info

    def get_storage_adapter_slots(self, cache_enabled=True):
        storage_adapters = self.get_storage_adapter(
            cache_enabled=cache_enabled
        )
        if storage_adapters is None:
            return None

        slots = []
        for storage_adapter in storage_adapters:
            slots.append(
                storage_adapter['Slot']
            )

        return slots
