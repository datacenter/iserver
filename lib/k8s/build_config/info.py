from lib import filter_helper


class K8sBuildConfigInfo():
    def __init__(self):
        self.build_config = None

    def get_build_config_info(self, build_config_mo):
        if build_config_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            build_config_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(build_config_mo, 'spec')
        info['status'] = self.get(build_config_mo, 'status')
        info['type'] = self.get(build_config_mo, 'spec:source:type')
        info['ref'] = self.get(build_config_mo, 'spec:source:git:ref')
        info['uri'] = self.get(build_config_mo, 'spec:source:git:uri')
        return info

    def get_build_configs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.build_config is not None:
                return self.build_config

        managed_objects = self.get_build_config_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.build_config = []
        for managed_object in managed_objects:
            build_config_info = {}
            build_config_info['info'] = self.get_build_config_info(
                managed_object
            )
            build_config_info['mo'] = managed_object
            self.build_config.append(
                build_config_info
            )

        return self.build_config

    def match_build_config(self, build_config_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, build_config_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, build_config_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_build_config',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_build_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_build_configs = self.get_build_configs_info(cache_enabled=cache_enabled)
        if all_build_configs is None:
            return None

        build_configs = []

        for build_config_info in all_build_configs:
            if not self.match_build_config(build_config_info['info'], object_filter):
                continue

            if return_mo:
                build_configs.append(
                    build_config_info['mo']
                )
                continue

            build_configs.append(
                build_config_info['info']
            )

        return build_configs

    def is_build_config(self, namespace, name, cache_enabled=True):
        if self.get_build_config(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_build_config(self, cache_enabled=True):
        policies = self.get_build_configs(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_build_config(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        build_configs = self.get_build_configs(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if build_configs is None:
            return None

        if len(build_configs) == 1:
            return build_configs[0]

        return None
