class K8sAlertRuleInfo():
    def __init__(self):
        self.alert_rule = None

    def get_alert_rule_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_alert_rules(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'alert_rule', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_alert_rule(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'alert_rule', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_alert_rule(self, name, cache_enabled=True, optimized=True):
        if self.get_alert_rule(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True
    
    def is_any_alert_rule(self, cache_enabled=True):
        infos = self.get_alert_rules(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True