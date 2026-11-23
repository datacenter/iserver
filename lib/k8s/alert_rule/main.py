from lib.k8s.alert_rule.api import K8sAlertRuleApi
from lib.k8s.alert_rule.info import K8sAlertRuleInfo
from lib.k8s.alert_rule.create import K8sAlertRuleCreate
from lib.k8s.alert_rule.delete import K8sAlertRuleDelete
from lib.k8s.alert_rule.wait import K8sAlertRuleWait


class K8sAlertRule(
        K8sAlertRuleApi,
        K8sAlertRuleInfo,
        K8sAlertRuleCreate,
        K8sAlertRuleDelete,
        K8sAlertRuleWait
        ):
    def __init__(self):
        K8sAlertRuleApi.__init__(self)
        K8sAlertRuleInfo.__init__(self)
        K8sAlertRuleCreate.__init__(self)
        K8sAlertRuleDelete.__init__(self)
        K8sAlertRuleWait.__init__(self)
