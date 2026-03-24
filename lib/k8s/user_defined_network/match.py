from lib import filter_helper


class K8sUserDefinedNetworkMatch():
    def __init__(self):
        pass

    def match_user_defined_network(self, info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            key_found = False

            if key in self.get_common_match():
                key_found = True
                continue

            if key == 'topology':
                key_found = True
                if value.lower() == 'l2':
                    if info['topology'] != 'Layer2':
                        return False

                if value.lower() == 'l3':
                    if info['topology'] != 'Layer3':
                        return False
                    
            if not key_found:
                self.log.error(
                    'match_group',
                    'Unsupported key: %s' % (key)
                )

        return True
