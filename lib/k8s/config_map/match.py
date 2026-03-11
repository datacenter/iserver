from lib import filter_helper


class K8sConfigMapMatch():
    def __init__(self):
        pass

    def match_config_map(self, config_map_info, config_map_filter):
        if config_map_filter is None or len(config_map_filter) == 0:
            return True

        for ap_rule in config_map_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key in self.get_common_match():
                key_found = True
                continue

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
