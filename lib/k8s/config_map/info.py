from lib import filter_helper


class K8sConfigMapInfo():
    def __init__(self):
        self.config_map = None

    def get_config_map_info(self, config_map_mo):
        if config_map_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            config_map_mo
        )
        info.update(metadata_info)

        info['namespace'] = self.get(config_map_mo, 'metadata:namespace')
        info['name'] = self.get(config_map_mo, 'metadata:name')

        info['data'] = self.get(config_map_mo, 'data', on_error={}, on_none={})
        info['dataCount'] = len(info['data'])

        return info

    def get_config_maps_info(self, cache_enabled=True):
        if cache_enabled:
            if self.config_map is not None:
                return self.config_map

        managed_objects = self.get_config_map_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.config_map = []
        for managed_object in managed_objects:
            config_map_info = {}
            config_map_info['info'] = self.get_config_map_info(
                managed_object
            )
            config_map_info['mo'] = managed_object
            self.config_map.append(
                config_map_info
            )

        return self.config_map

    def match_config_map(self, config_map_info, config_map_filter):
        if config_map_filter is None or len(config_map_filter) == 0:
            return True

        for ap_rule in config_map_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, config_map_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (config_map_info['namespace'], config_map_info['name'])):
                    return False

            if key == 'cm-name':
                key_found = True
                found = False
                for key in config_map_info['data']:
                    if filter_helper.match_string(value, key):
                        found = True

                if not found:
                    return False

            if key == 'cm-data':
                key_found = True
                found = False
                for key in config_map_info['data']:
                    if filter_helper.match_string(value, config_map_info['data'][key]):
                        found = True

                if not found:
                    return False

            if not key_found:
                self.log.error(
                    'match_config_map',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_config_maps(self, object_filter=None, pod_info=False, return_mo=False, cache_enabled=True):
        all_config_maps = self.get_config_maps_info(cache_enabled=cache_enabled)
        if all_config_maps is None:
            return None

        config_maps = []

        for config_map_info in all_config_maps:
            if not self.match_config_map(config_map_info['info'], object_filter):
                continue

            if return_mo:
                config_maps.append(
                    config_map_info['mo']
                )
                continue

            if pod_info:
                config_map_info['info']['pod'] = []
                pods_info = self.get_pods(
                    object_filter=[
                        'cm:%s:%s' % (
                            config_map_info['info']['namespace'],
                            config_map_info['info']['name']
                        )
                    ]
                )
                if pods_info is not None:
                    for pod in pods_info:
                        cm_pod_info = {}
                        cm_pod_info['namespace'] = pod['namespace']
                        cm_pod_info['name'] = pod['name']
                        config_map_info['info']['pod'].append(
                            cm_pod_info
                        )

            config_maps.append(
                config_map_info['info']
            )

        if not return_mo:
            config_maps = sorted(
                config_maps,
                key=lambda i: (
                    i['namespace'],
                    i['name']
                )
            )

        return config_maps

    def get_config_map(self, namespace, name):
        config_map_filter = []
        config_map_filter.append('namespace:%s' % (namespace))
        config_map_filter.append('name:%s' % (name))

        config_maps = self.get_config_maps(
            object_filter=config_map_filter
        )

        if config_maps is None or len(config_maps) != 1:
            return None

        return config_maps[0]
