class ConfigInfo():
    def __init__(self):
        self.config = None

    def set_configuration_cache(self, config_mo):
        self.config = self.get_config_info(config_mo)

    def get_config_info(self, config_mo):
        if config_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name
        info['configuration'] = config_mo

        return info

    def get_config(self, cache_enabled=True):
        if cache_enabled and self.config is not None:
            return self.config

        config_mo = self.get_config_mo(cache_enabled=cache_enabled)
        if config_mo is None:
            self.log.error(
                'get_config',
                'Failed to get config: %s' % (self.nexus_name)
            )
            return None

        self.config = self.get_config_info(config_mo)
        return self.config
