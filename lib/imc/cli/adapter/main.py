import json


class ImcCliAdapter():
    def __init__(self):
        self.adapter_mo = None
        self.adapter_ext_mo = {}
        self.adapter_host_mo = {}
        self.adapter_fc_mo = {}

    def get_adapter_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.adapter_mo is not None:
                return self.adapter_mo

            self.adapter_mo = self.get_imc_cli_cache_entry(
                'adapter'
            )
            if self.adapter_mo is not None:
                return self.adapter_mo

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

    def get_adapter_ext_mo(self, adapter_id, cache_enabled=True):
        if cache_enabled:
            if adapter_id in self.adapter_ext_mo and self.adapter_ext_mo[adapter_id] is not None:
                return self.adapter_ext_mo[adapter_id]

            self.adapter_ext_mo[adapter_id] = self.get_imc_cli_cache_entry(
                'adapter_ext_%s' % (adapter_id)
            )
            if self.adapter_ext_mo[adapter_id] is not None:
                return self.adapter_ext_mo[adapter_id]

        self.adapter_ext_mo[adapter_id] = self.show_list(
            'show ext-eth-if detail',
            'Port',
            'Port',
            method='last word',
            scope='chassis,adapter %s' % (adapter_id)
        )

        if self.adapter_ext_mo[adapter_id] is None:
            return None

        self.set_imc_cli_cache_entry(
            'adapter_ext_%s' % (adapter_id),
            self.adapter_ext_mo[adapter_id]
        )

        self.log.debug(
            'get_adapter_ext_mo',
            json.dumps(self.adapter_ext_mo[adapter_id], indent=4)
        )
        return self.adapter_ext_mo[adapter_id]

    def get_adapter_ext_info(self, adapter_id, adapter_ext_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip
        info['Slot'] = adapter_id

        for key in adapter_ext_mo:
            info[key] = adapter_ext_mo[key]

        info['__Key'] = 'Port'
        info['__Value'] = info[info['__Key']]

        self.log.debug(
            'get_adapter_ext_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_adapter_host_mo(self, adapter_id, cache_enabled=True):
        if cache_enabled:
            if adapter_id in self.adapter_host_mo and self.adapter_host_mo[adapter_id] is not None:
                return self.adapter_host_mo[adapter_id]

            self.adapter_host_mo[adapter_id] = self.get_imc_cli_cache_entry(
                'adapter_host_%s' % (adapter_id)
            )
            if self.adapter_host_mo[adapter_id] is not None:
                return self.adapter_host_mo[adapter_id]

        self.adapter_host_mo[adapter_id] = self.show_list(
            'show host-eth-if detail',
            'Name',
            'Port',
            method='last word',
            scope='chassis,adapter %s' % (adapter_id)
        )

        if self.adapter_host_mo[adapter_id] is None:
            return None

        self.set_imc_cli_cache_entry(
            'adapter_host_%s' % (adapter_id),
            self.adapter_host_mo[adapter_id]
        )

        self.log.debug(
            'get_adapter_host_mo',
            json.dumps(self.adapter_host_mo[adapter_id], indent=4)
        )
        return self.adapter_host_mo[adapter_id]

    def get_adapter_host_info(self, adapter_id, adapter_host_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip
        info['Slot'] = adapter_id

        for key in adapter_host_mo:
            info[key] = adapter_host_mo[key]

        info['__Key'] = 'Port'
        info['__Value'] = info[info['__Key']]

        self.log.debug(
            'get_adapter_host_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_adapter_fc_mo(self, adapter_id, cache_enabled=True):
        if cache_enabled:
            if adapter_id in self.adapter_fc_mo and self.adapter_fc_mo[adapter_id] is not None:
                return self.adapter_fc_mo[adapter_id]

            self.adapter_fc_mo[adapter_id] = self.get_imc_cli_cache_entry(
                'adapter_fc_%s' % (adapter_id)
            )
            if self.adapter_fc_mo[adapter_id] is not None:
                return self.adapter_fc_mo[adapter_id]

        self.adapter_fc_mo[adapter_id] = self.show_list(
            'show host-fc-if detail',
            'Name',
            'Port',
            method='last word',
            scope='chassis,adapter %s' % (adapter_id)
        )

        if self.adapter_fc_mo[adapter_id] is None:
            return None

        self.set_imc_cli_cache_entry(
            'adapter_fc_%s' % (adapter_id),
            self.adapter_fc_mo[adapter_id]
        )

        self.log.debug(
            'get_adapter_fc_mo',
            json.dumps(self.adapter_fc_mo[adapter_id], indent=4)
        )
        return self.adapter_fc_mo[adapter_id]

    def get_adapter_fc_info(self, adapter_id, adapter_fc_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip
        info['Slot'] = adapter_id

        for key in adapter_fc_mo:
            info[key] = adapter_fc_mo[key]

        info['__Key'] = 'Port'
        info['__Value'] = info[info['__Key']]

        self.log.debug(
            'get_adapter_fc_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_adapter(self, ext_info=False, host_info=False, fc_info=False, cache_enabled=True):
        adapters_mo = self.get_adapter_mo(cache_enabled=cache_enabled)
        if adapters_mo is None:
            return None

        adapters_info = []

        for adapter_mo in adapters_mo:
            adapter_info = self.get_adapter_info(
                adapter_mo
            )

            if ext_info:
                adapter_info['ext'] = self.get_adapter_ext(
                    slot_id=adapter_info['Slot'],
                    cache_enabled=cache_enabled
                )

            if host_info:
                adapter_info['host'] = self.get_adapter_host(
                    slot_id=adapter_info['Slot'],
                    cache_enabled=cache_enabled
                )

            if fc_info:
                adapter_info['host'] = self.get_adapter_fc(
                    slot_id=adapter_info['Slot'],
                    cache_enabled=cache_enabled
                )

            adapters_info.append(
                adapter_info
            )

        return adapters_info

    def get_adapter_ext(self, slot_id=None, cache_enabled=True):
        if slot_id is None:
            slots = self.get_adapter_slots(cache_enabled=cache_enabled)
            if slots is None:
                return None
        else:
            slots = [slot_id]

        info = []

        for slot in slots:
            adapter_ext_mo = self.get_adapter_ext_mo(slot, cache_enabled=cache_enabled)
            if adapter_ext_mo is None:
                return None

            for item in adapter_ext_mo:
                info.append(
                    self.get_adapter_ext_info(
                        slot,
                        item
                    )
                )

        return info

    def get_adapter_host(self, slot_id=None, cache_enabled=True):
        if slot_id is None:
            slots = self.get_adapter_slots(cache_enabled=cache_enabled)
            if slots is None:
                return None
        else:
            slots = [slot_id]

        info = []

        for slot in slots:
            adapter_host_mo = self.get_adapter_host_mo(slot, cache_enabled=cache_enabled)
            if adapter_host_mo is None:
                return None

            for item in adapter_host_mo:
                info.append(
                    self.get_adapter_host_info(
                        slot,
                        item
                    )
                )

        return info

    def get_adapter_fc(self, slot_id=None, cache_enabled=True):
        if slot_id is None:
            slots = self.get_adapter_slots(cache_enabled=cache_enabled)
            if slots is None:
                return None
        else:
            slots = [slot_id]

        info = []

        for slot in slots:
            adapter_fc_mo = self.get_adapter_fc_mo(slot, cache_enabled=cache_enabled)
            if adapter_fc_mo is None:
                return None

            for item in adapter_fc_mo:
                info.append(
                    self.get_adapter_fc_info(
                        slot,
                        item
                    )
                )

        return info

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
