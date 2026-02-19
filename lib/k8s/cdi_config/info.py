from lib import filter_helper


class K8sCdiConfigInfo():
    def __init__(self):
        self.cdi_config = None

    def get_cdi_config_info(self, cdi_config_mo):
        if cdi_config_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            cdi_config_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(cdi_config_mo, 'spec')
        info['status'] = self.get(cdi_config_mo, 'status')
        return info

    def get_cdi_configs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cdi_config is not None:
                return self.cdi_config

        managed_objects = self.get_cdi_config_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cdi_config = []
        for managed_object in managed_objects:
            cdi_config_info = {}
            cdi_config_info['info'] = self.get_cdi_config_info(
                managed_object
            )
            cdi_config_info['mo'] = managed_object
            self.cdi_config.append(
                cdi_config_info
            )

        return self.cdi_config

    def match_cdi_config(self, cdi_config_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cdi_config_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cdi_config',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cdi_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_cdi_configs = self.get_cdi_configs_info(cache_enabled=cache_enabled)
        if all_cdi_configs is None:
            return None

        cdi_configs = []

        for cdi_config_info in all_cdi_configs:
            if not self.match_cdi_config(cdi_config_info['info'], object_filter):
                continue

            if return_mo:
                cdi_configs.append(
                    cdi_config_info['mo']
                )
                continue

            cdi_configs.append(
                cdi_config_info['info']
            )

        return cdi_configs

    def is_cdi_config(self, name, cache_enabled=True):
        if self.get_cdi_config(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_cdi_config(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        cdi_configs = self.get_cdi_configs(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if cdi_configs is None:
            return None

        if len(cdi_configs) == 1:
            return cdi_configs[0]

        return None
