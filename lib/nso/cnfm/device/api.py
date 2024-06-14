class NsoCnfmDeviceApi():
    def __init__(self):
        self.cnfm_device_mo = {}

    def get_cnfm_device_mo(self, device_name, cache_enabled=True):
        if cache_enabled:
            if device_name in self.cnfm_device_mo:
                return self.cnfm_device_mo[device_name]

        device_config = self.get_device_config_mo(
            device_name,
            cache_enabled=cache_enabled
        )
        if device_config is None:
            self.log.error(
                'nso.get_cnfm_device_mo',
                'Failed to get device config: %s' % (device_name)
            )
            return None

        self.cnfm_device_mo[device_name] = device_config
        return self.cnfm_device_mo[device_name]
