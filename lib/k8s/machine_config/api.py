class K8sMachineConfigApi():
    def __init__(self):
        self.machine_config_mo = None

    def get_machine_config_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.machine_config_mo
        )
        if cache_hit:
            return response

        response, self.machine_config_mo = self.get_resources(
            'MachineConfig', 
            'machineconfiguration.openshift.io/v1', 
            self.machine_config_mo,
            name=name
        )

        return response