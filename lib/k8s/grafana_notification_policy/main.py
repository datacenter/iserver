from lib.k8s.grafana_notification_policy.api import K8sGrafanaNotificationPolicyApi
from lib.k8s.grafana_notification_policy.info import K8sGrafanaNotificationPolicyInfo


class K8sGrafanaNotificationPolicy(
        K8sGrafanaNotificationPolicyApi,
        K8sGrafanaNotificationPolicyInfo
        ):
    def __init__(self):
        K8sGrafanaNotificationPolicyApi.__init__(self)
        K8sGrafanaNotificationPolicyInfo.__init__(self)
