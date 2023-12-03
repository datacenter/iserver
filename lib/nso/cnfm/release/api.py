class NsoCnfmReleaseApi():
    def __init__(self):
        self.cnfm_release_mo = {}

    def get_cnfm_release_mo(self, device_name, cache_enabled=True):
        if cache_enabled:
            if device_name in self.cnfm_release_mo:
                return self.cnfm_release_mo[device_name]

        device_config = self.get_device_config_mo(
            device_name,
            cache_enabled=cache_enabled
        )
        if device_config is None:
            self.log.error(
                'nso.get_cnfm_release_mo',
                'Failed to get device config: %s' % (device_name)
            )
            return None

        self.cnfm_release_mo[device_name] = device_config['k8s-cnfm:cnf']['release']
        return self.cnfm_release_mo[device_name]
