class K8sAlertRuleDelete():
    def __init__(self):
        pass

    def delete_alert_rule(self, name, my_output=None, wait=True):
        success = self.delete_resource_and_wait(
            'AlertRule', 
            'cilium.io/v1alpha1',
            name, 
            'alert_rule',
            wait=wait, 
            max_time=60, 
            my_output=my_output
        )
        return success
    
    def delete_alert_rules(self, my_output=None, wait=True):
        items = self.get_alert_rules(
            cache_enabled=False
        )
        if items is None:
            if my_output is not None:
                my_output.error('Failed to get alert rules')
            return False
        
        for item in items:
            success = self.delete_alert_rule(
                item['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False

        return True