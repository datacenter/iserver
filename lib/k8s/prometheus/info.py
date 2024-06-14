from lib import filter_helper


class K8sPrometheusInfo():
    def __init__(self):
        self.prometheus = None

    def get_prometheus_info(self, prometheus_mo):
        if prometheus_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        return info

    def get_prometheuss_info(self, cache_enabled=True):
        if cache_enabled:
            if self.prometheus is not None:
                return self.prometheus

        managed_objects = self.get_prometheus_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.prometheus = []
        for managed_object in managed_objects:
            prometheus_info = {}
            prometheus_info['info'] = self.get_prometheus_info(
                managed_object
            )
            prometheus_info['mo'] = managed_object
            self.prometheus.append(
                prometheus_info
            )

        return self.prometheus

    def match_prometheus(self, prometheus_info, prometheus_filter):
        if prometheus_filter is None or len(prometheus_filter) == 0:
            return True

        for ap_rule in prometheus_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_prometheus',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_prometheuss(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_prometheuss = self.get_prometheuss_info(cache_enabled=cache_enabled)
        if all_prometheuss is None:
            return None

        prometheuss = []

        for prometheus_info in all_prometheuss:
            if not self.match_prometheus(prometheus_info['info'], object_filter):
                continue

            if return_mo:
                prometheuss.append(
                    prometheus_info['mo']
                )
                continue

            prometheuss.append(
                prometheus_info['info']
            )

        return prometheuss
