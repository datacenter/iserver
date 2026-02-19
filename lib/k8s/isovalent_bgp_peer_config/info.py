from lib import filter_helper


class K8sIsovalentBGPPeerConfigInfo():
    def __init__(self):
        self.isovalent_bgp_peer_config = None

    def get_isovalent_bgp_peer_config_info(self, isovalent_bgp_peer_config_mo):
        if isovalent_bgp_peer_config_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            isovalent_bgp_peer_config_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(isovalent_bgp_peer_config_mo, 'spec')
        return info

    def get_isovalent_bgp_peer_configs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.isovalent_bgp_peer_config is not None:
                return self.isovalent_bgp_peer_config

        managed_objects = self.get_isovalent_bgp_peer_config_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.isovalent_bgp_peer_config = []
        for managed_object in managed_objects:
            isovalent_bgp_peer_config_info = {}
            isovalent_bgp_peer_config_info['info'] = self.get_isovalent_bgp_peer_config_info(
                managed_object
            )
            isovalent_bgp_peer_config_info['mo'] = managed_object
            self.isovalent_bgp_peer_config.append(
                isovalent_bgp_peer_config_info
            )

        return self.isovalent_bgp_peer_config

    def match_isovalent_bgp_peer_config(self, isovalent_bgp_peer_config_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, isovalent_bgp_peer_config_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_isovalent_bgp_peer_config',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_isovalent_bgp_peer_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_isovalent_bgp_peer_configs = self.get_isovalent_bgp_peer_configs_info(cache_enabled=cache_enabled)
        if all_isovalent_bgp_peer_configs is None:
            return None

        isovalent_bgp_peer_configs = []

        for isovalent_bgp_peer_config_info in all_isovalent_bgp_peer_configs:
            if not self.match_isovalent_bgp_peer_config(isovalent_bgp_peer_config_info['info'], object_filter):
                continue

            if return_mo:
                isovalent_bgp_peer_configs.append(
                    isovalent_bgp_peer_config_info['mo']
                )
                continue

            isovalent_bgp_peer_configs.append(
                isovalent_bgp_peer_config_info['info']
            )

        return isovalent_bgp_peer_configs

    def is_isovalent_bgp_peer_config(self, name, cache_enabled=True):
        if self.get_isovalent_bgp_peer_config(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_isovalent_bgp_peer_config(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        isovalent_bgp_peer_configs = self.get_isovalent_bgp_peer_configs(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if isovalent_bgp_peer_configs is None:
            return None

        if len(isovalent_bgp_peer_configs) == 1:
            return isovalent_bgp_peer_configs[0]

        return None
