from lib.k8s.grafana_alert_rule_group.api import K8sGrafanaAlertRuleGroupApi
from lib.k8s.grafana_alert_rule_group.info import K8sGrafanaAlertRuleGroupInfo


class K8sGrafanaAlertRuleGroup(
        K8sGrafanaAlertRuleGroupApi,
        K8sGrafanaAlertRuleGroupInfo
        ):
    def __init__(self):
        K8sGrafanaAlertRuleGroupApi.__init__(self)
        K8sGrafanaAlertRuleGroupInfo.__init__(self)
