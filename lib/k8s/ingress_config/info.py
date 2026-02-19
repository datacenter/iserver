from lib import filter_helper


class K8sIngressConfigInfo():
    def __init__(self):
        self.ingress_config = None

    def get_ingress_config_info(self, ingress_config_mo):
        if ingress_config_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            ingress_config_mo
        )
        info.update(metadata_info)

        info['spec'] = ingress_config_mo['spec']
        info['status'] = ingress_config_mo['status']
        info['info'] = {}
        info['info']['domain'] = filter_helper.get_attr(ingress_config_mo, 'spec:domain')

        return info

    def get_ingress_configs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.ingress_config is not None:
                return self.ingress_config

        managed_objects = self.get_ingress_config_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.ingress_config = []
        for managed_object in managed_objects:
            ingress_config_info = {}
            ingress_config_info['info'] = self.get_ingress_config_info(
                managed_object
            )
            ingress_config_info['mo'] = managed_object
            self.ingress_config.append(
                ingress_config_info
            )

        return self.ingress_config

    def match_ingress_config(self, ingress_config_info, ingress_config_filter):
        if ingress_config_filter is None or len(ingress_config_filter) == 0:
            return True

        for ap_rule in ingress_config_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, ingress_config_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_ingress_config',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_ingress_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_ingress_configs = self.get_ingress_configs_info(cache_enabled=cache_enabled)
        if all_ingress_configs is None:
            return None

        ingress_configs = []

        for ingress_config_info in all_ingress_configs:
            if not self.match_ingress_config(ingress_config_info['info'], object_filter):
                continue

            if return_mo:
                ingress_configs.append(
                    ingress_config_info['mo']
                )
                continue

            ingress_configs.append(
                ingress_config_info['info']
            )

        return ingress_configs

    def get_ingress_config(self, name='cluster', return_mo=False, cache_enabled=True):
        object_filter=['name:%s' % (name)]
        configs = self.get_ingress_configs(object_filter=object_filter, return_mo=return_mo, cache_enabled=cache_enabled)
        if configs is None or len(configs) != 1:
            return None
        return configs[0]
