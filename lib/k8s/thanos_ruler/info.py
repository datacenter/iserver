from lib import filter_helper


class K8sThanosRulerInfo():
    def __init__(self):
        self.thanos_ruler = None

    def get_thanos_ruler_info(self, thanos_ruler_mo):
        if thanos_ruler_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        return info

    def get_thanos_rulers_info(self, cache_enabled=True):
        if cache_enabled:
            if self.thanos_ruler is not None:
                return self.thanos_ruler

        managed_objects = self.get_thanos_ruler_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.thanos_ruler = []
        for managed_object in managed_objects:
            thanos_ruler_info = {}
            thanos_ruler_info['info'] = self.get_thanos_ruler_info(
                managed_object
            )
            thanos_ruler_info['mo'] = managed_object
            self.thanos_ruler.append(
                thanos_ruler_info
            )

        return self.thanos_ruler

    def match_thanos_ruler(self, thanos_ruler_info, thanos_ruler_filter):
        if thanos_ruler_filter is None or len(thanos_ruler_filter) == 0:
            return True

        for ap_rule in thanos_ruler_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_thanos_ruler',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_thanos_rulers(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_thanos_rulers = self.get_thanos_rulers_info(cache_enabled=cache_enabled)
        if all_thanos_rulers is None:
            return None

        thanos_rulers = []

        for thanos_ruler_info in all_thanos_rulers:
            if not self.match_thanos_ruler(thanos_ruler_info['info'], object_filter):
                continue

            if return_mo:
                thanos_rulers.append(
                    thanos_ruler_info['mo']
                )
                continue

            thanos_rulers.append(
                thanos_ruler_info['info']
            )

        return thanos_rulers
