from lib import filter_helper


class K8sSubscriptionMatch():
    def __init__(self):
        pass

    def match_subscription(self, subscription_info, subscription_filter):
        if subscription_filter is None or len(subscription_filter) == 0:
            return True

        for ap_rule in subscription_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key in self.get_common_match():
                key_found = True
                continue

            if key == 'package':
                key_found = True
                if not filter_helper.match_string(value, subscription_info['package']):
                    return False

            if not key_found:
                self.log.error(
                    'match_subscription',
                    'Unsupported key: %s' % (key)
                )

        return True