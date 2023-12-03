class NsoCnfmClusterApi():
    def __init__(self):
        self.cnfm_cluster_mo = {}

    def get_cnfm_cluster_mo(self, device_name, cache_enabled=True):
        if cache_enabled:
            if device_name in self.cnfm_cluster_mo:
                return self.cnfm_cluster_mo[device_name]

        device_config = self.get_device_config_mo(
            device_name,
            cache_enabled=cache_enabled
        )
        if device_config is None:
            self.log.error(
                'nso.get_cnfm_cluster_mo',
                'Failed to get device config: %s' % (device_name)
            )
            return None

        self.cnfm_cluster_mo[device_name] = device_config['k8s-cnfm:clusters']['cluster']
        return self.cnfm_cluster_mo[device_name]
