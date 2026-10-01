from lib import filter_helper
from lib import ip_helper


class K8sBgpSessionStateMatch():
    def __init__(self):
        pass

    def match_bgp_session_state(self, info, filter_rules):
        if filter_rules is None or len(filter_rules) == 0:
            return True

        for ap_rule in filter_rules:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key in self.get_common_match():
                key_found = True
                continue

            if key == 'node':
                key_found = True
                if not filter_helper.match_string(value, info['status']['node']):
                    return False

            if key == 'nodes':
                key_found = True
                value_found = False
                for name in value.split(','):
                    if filter_helper.match_string(name, info['status']['node']):
                        value_found = True
                        break

                if not value_found:
                    return False

            if key == 'peer':
                key_found = True
                if not filter_helper.match_string(value, info['status']['peer']):
                    return False

            if key == 'peers':
                key_found = True
                value_found = False
                for name in value.split(','):
                    if filter_helper.match_string(name, info['status']['peer']):
                        value_found = True
                        break

                if not value_found:
                    return False
                                
            if not key_found:
                self.log.error(
                    'match_bgp_session_state',
                    'Unsupported key: %s' % (key)
                )

        return True