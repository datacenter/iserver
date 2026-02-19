from lib.k8s.alert_rule.api import K8sAlertRuleApi
from lib.k8s.alert_rule.info import K8sAlertRuleInfo


class K8sAlertRule(
        K8sAlertRuleApi,
        K8sAlertRuleInfo
        ):
    def __init__(self):
        K8sAlertRuleApi.__init__(self)
        K8sAlertRuleInfo.__init__(self)
