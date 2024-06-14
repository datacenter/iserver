from lib import filter_helper


class K8sLimitInfo():
    def __init__(self):
        self.limit = None

    def get_limit_info(self, limit_mo):
        if limit_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        return info

    def get_limits_info(self, cache_enabled=True):
        if cache_enabled:
            if self.limit is not None:
                return self.limit

        managed_objects = self.get_limit_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.limit = []
        for managed_object in managed_objects:
            limit_info = {}
            limit_info['info'] = self.get_limit_info(
                managed_object
            )
            limit_info['mo'] = managed_object
            self.limit.append(
                limit_info
            )

        return self.limit

    def match_limit(self, limit_info, limit_filter):
        if limit_filter is None or len(limit_filter) == 0:
            return True

        for ap_rule in limit_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_limit',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_limits(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_limits = self.get_limits_info(cache_enabled=cache_enabled)
        if all_limits is None:
            return None

        limits = []

        for limit_info in all_limits:
            if not self.match_limit(limit_info['info'], object_filter):
                continue

            if return_mo:
                limits.append(
                    limit_info['mo']
                )
                continue

            limits.append(
                limit_info['info']
            )

        return limits
