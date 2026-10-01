class K8sAlertRuleCreate():
    def __init__(self):
        pass

    def create_alert_rule(self, body, confirmation=False, my_output=None, wait=True):
        success = self.create_resource_and_wait(
            body, 
            'alert_rule', 
            wait=wait,
            my_output=my_output, 
            confirmation=confirmation
        )
        return success