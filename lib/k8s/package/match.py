from lib import filter_helper


class K8sPackageMatch():
    def __init__(self):
        pass

    def match_package(self, package_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            key_found = False

            if key in self.get_common_match():
                key_found = True
                continue

            if key == 'catalog':
                key_found = True
                if not filter_helper.match_string(value, package_info['catalog']):
                    return False

            if not key_found:
                self.log.error(
                    'match_package',
                    'Unsupported key: %s' % (key)
                )

        return True