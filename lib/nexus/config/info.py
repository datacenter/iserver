from lib import filter_helper
from lib import ip_helper


class ConfigInfo():
    def __init__(self):
        self.config = None

    def get_config_info(self, config_mo):
        if config_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        return info

    def get_configs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.config is not None:
                return self.config

        managed_objects = self.get_config_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            self.log.error(
                'get_configs_info',
                'No config managed objects: %s' % (self.nexus_name)
            )
            return None

        self.config = []
        for managed_object in managed_objects:
            self.config.append(
                self.get_config_info(
                    managed_object
                )
            )

        return self.config

    def get_configs(self, cache_enabled=True):
        all_configs = self.get_configs_info(cache_enabled=cache_enabled)
        if all_configs is None:
            self.log.error(
                'get_configs',
                'Failed to get config: %s' % (self.nexus_name)
            )
            return None

        configs = []

        for config_info in all_configs:
            configs.append(
                config_info
            )

        return configs
