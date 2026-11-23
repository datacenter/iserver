from lib import filter_helper


class K8sUserMatch():
    def __init__(self):
        pass

    def match_user(self, info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            key_found = False

            if key in self.get_common_match():
                key_found = True
                continue

            if key == 'group':
                key_found = True
                found = False
                for item in info['groups']:
                    if filter_helper.match_string(value, item):
                        found = True
                        break

                if not found:
                    return False

            if key == 'provider':
                if 'identityT' in info:
                    key_found = True
                    found = False
                    for item in info['identityT']:
                        if filter_helper.match_string(value, item['provider_name']):
                            found = True
                            break

                    if not found:
                        return False

            if not key_found:
                self.log.error(
                    'match_user',
                    'Unsupported key: %s' % (key)
                )

        return True
