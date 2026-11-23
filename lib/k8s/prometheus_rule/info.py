from lib import filter_helper


class K8sPrometheusRuleInfo():
    def __init__(self):
        self.prometheus_rule = None

    def get_prometheus_rule_info(self, prometheus_rule_mo):
        if prometheus_rule_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        return info

    def get_prometheus_rules_info(self, cache_enabled=True):
        if cache_enabled:
            if self.prometheus_rule is not None:
                return self.prometheus_rule

        managed_objects = self.get_prometheus_rule_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.prometheus_rule = []
        for managed_object in managed_objects:
            prometheus_rule_info = {}
            prometheus_rule_info['info'] = self.get_prometheus_rule_info(
                managed_object
            )
            prometheus_rule_info['mo'] = managed_object
            self.prometheus_rule.append(
                prometheus_rule_info
            )

        return self.prometheus_rule

    def match_prometheus_rule(self, prometheus_rule_info, prometheus_rule_filter):
        if prometheus_rule_filter is None or len(prometheus_rule_filter) == 0:
            return True

        for ap_rule in prometheus_rule_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_prometheus_rule',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_prometheus_rules(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_prometheus_rules = self.get_prometheus_rules_info(cache_enabled=cache_enabled)
        if all_prometheus_rules is None:
            return None

        prometheus_rules = []

        for prometheus_rule_info in all_prometheus_rules:
            if not self.match_prometheus_rule(prometheus_rule_info['info'], object_filter):
                continue

            if return_mo:
                prometheus_rules.append(
                    prometheus_rule_info['mo']
                )
                continue

            prometheus_rules.append(
                prometheus_rule_info['info']
            )

        return prometheus_rules
