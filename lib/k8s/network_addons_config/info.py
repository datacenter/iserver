from lib import filter_helper


class K8sNetworkAddonsConfigInfo():
    def __init__(self):
        self.network_addons_config = None

    def get_network_addons_config_info(self, network_addons_config_mo):
        if network_addons_config_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            network_addons_config_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(network_addons_config_mo, 'spec')
        info['status'] = self.get(network_addons_config_mo, 'status')

        info['ready'] = False
        info['readyTick'] = '\u2717'
        info['__Output']['readyTick'] = 'Red'

        info['error'] = []
        conditions_mo = self.get(network_addons_config_mo, 'status:conditions')
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                condition_type = self.get(condition_mo, 'type')
                if condition_type is not None:
                    if condition_type == 'Available':
                        if self.get(condition_mo, 'status') == 'True':
                            info['ready'] = True
                            info['readyTick'] = '\u2713'
                            info['__Output']['readyTick'] = 'Green'

        return info

    def get_network_addons_configs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.network_addons_config is not None:
                return self.network_addons_config

        managed_objects = self.get_network_addons_config_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.network_addons_config = []
        for managed_object in managed_objects:
            network_addons_config_info = {}
            network_addons_config_info['info'] = self.get_network_addons_config_info(
                managed_object
            )
            network_addons_config_info['mo'] = managed_object
            self.network_addons_config.append(
                network_addons_config_info
            )

        return self.network_addons_config

    def match_network_addons_config(self, network_addons_config_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, network_addons_config_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_network_addons_config',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_network_addons_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_network_addons_configs = self.get_network_addons_configs_info(cache_enabled=cache_enabled)
        if all_network_addons_configs is None:
            return None

        network_addons_configs = []

        for network_addons_config_info in all_network_addons_configs:
            if not self.match_network_addons_config(network_addons_config_info['info'], object_filter):
                continue

            if return_mo:
                network_addons_configs.append(
                    network_addons_config_info['mo']
                )
                continue

            network_addons_configs.append(
                network_addons_config_info['info']
            )

        return network_addons_configs

    def is_network_addons_config(self, name, cache_enabled=True):
        if self.get_network_addons_config(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_network_addons_config(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        network_addons_configs = self.get_network_addons_configs(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if network_addons_configs is None:
            return None

        if len(network_addons_configs) == 1:
            return network_addons_configs[0]

        return None
