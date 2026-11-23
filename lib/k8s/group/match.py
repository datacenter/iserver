from lib import filter_helper


class K8sGroupMatch():
    def __init__(self):
        pass

    def match_group(self, info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            key_found = False

            if key in self.get_common_match():
                key_found = True
                continue

            if key == 'ldap_host':
                key_found = True
                if not filter_helper.match_string(value, self.get(info, 'ldap')):
                    return False

            if key == 'ldap':
                key_found = True
                if value.lower() == 'true' and not info['isLdap']:
                    return False
                if value.lower() == 'false' and info['isLdap']:
                    return False

            if not key_found:
                self.log.error(
                    'match_group',
                    'Unsupported key: %s' % (key)
                )

        return True
