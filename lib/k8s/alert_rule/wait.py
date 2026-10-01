class K8sAlertRuleWait():
    def __init__(self):
        pass

    def wait_alert_rule(self, name, match_properties={}, break_properties={}, my_output=None, prompt='AlertRule', max_time=60):
        return self.wait_managed_object(
            'alert_rule',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_alert_rule(self, name, my_output=None, prompt='AlertRule', max_time=60):
        return self.wait_no_managed_object(
            'alert_rule',
            name,
            my_output=my_output,
            prompt='Wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )