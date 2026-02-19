class HardwareInfo():
    def __init__(self):
        self.hardware = None

    def get_hardware_info(self, hardware_mo):
        if hardware_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        excludeded_keys = [
            'TABLE_slot'
        ]
        for key in hardware_mo:
            if key not in excludeded_keys:
                info[key] = hardware_mo[key]

        info['chassis'] = {}
        info['modules'] = []
        info['ps'] = []
        info['fan'] = []

        try:
            for item in hardware_mo['TABLE_slot']['ROW_slot']['TABLE_slot_info']['ROW_slot_info']:
                if 'status_ok_empty' not in item and 'Chassis' in item['type']:
                    info['chassis'] = item

                if 'status_ok_empty' in item:
                    if item['status_ok_empty'].startswith('Module'):
                        info['modules'].append(
                            item
                        )

                    if item['status_ok_empty'].startswith('PS'):
                        info['ps'].append(
                            item
                        )

                    if item['status_ok_empty'].startswith('Fan'):
                        info['fan'].append(
                            item
                        )

        except BaseException:
            pass

        return info

    def get_hardware(self, cache_enabled=True):
        hardware_mo = self.get_hardware_mo(cache_enabled=cache_enabled)
        if hardware_mo is None:
            self.log.error(
                'get_hardware',
                'Failed to get hardware: %s' % (self.nexus_name)
            )
            return None

        return self.get_hardware_info(hardware_mo)
