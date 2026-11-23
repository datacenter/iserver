from lib.k8s.grafana_notification_policy_route.api import K8sGrafanaNotificationPolicyRouteApi
from lib.k8s.grafana_notification_policy_route.info import K8sGrafanaNotificationPolicyRouteInfo


class K8sGrafanaNotificationPolicyRoute(
        K8sGrafanaNotificationPolicyRouteApi,
        K8sGrafanaNotificationPolicyRouteInfo
        ):
    def __init__(self):
        K8sGrafanaNotificationPolicyRouteApi.__init__(self)
        K8sGrafanaNotificationPolicyRouteInfo.__init__(self)
