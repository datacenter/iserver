class K8sAlertRuleApi():
    def __init__(self):
        self.alert_rule_mo = None

    def get_alert_rule_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.alert_rule_mo
        )
        if cache_hit:
            return response

        response, self.alert_rule_mo = self.get_resources(
            'AlertRule', 
            'cilium.io/v1alpha1', 
            self.alert_rule_mo,
            name=name
        )

        return response