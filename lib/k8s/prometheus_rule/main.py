from lib.k8s.prometheus_rule.api import K8sPrometheusRuleApi
from lib.k8s.prometheus_rule.info import K8sPrometheusRuleInfo


class K8sPrometheusRule(
        K8sPrometheusRuleApi,
        K8sPrometheusRuleInfo
        ):
    def __init__(self):
        K8sPrometheusRuleApi.__init__(self)
        K8sPrometheusRuleInfo.__init__(self)
