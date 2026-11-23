import json


class K8sAlertRuleOutput():
    def __init__(self):
        pass

    def print_alert_rules_state(self, info):
        for item in info:
            item['specT'] = json.dumps(item['spec'], indent=2).split('\n')

        self.my_output.my_table_ng(
            info,
            [
                ['Alert Rule', 'name'],
                ['Spec', 'specT']
            ]
        )