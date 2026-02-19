from lib.k8s.grafana_notification_template.api import K8sGrafanaNotificationTemplateApi
from lib.k8s.grafana_notification_template.info import K8sGrafanaNotificationTemplateInfo


class K8sGrafanaNotificationTemplate(
        K8sGrafanaNotificationTemplateApi,
        K8sGrafanaNotificationTemplateInfo
        ):
    def __init__(self):
        K8sGrafanaNotificationTemplateApi.__init__(self)
        K8sGrafanaNotificationTemplateInfo.__init__(self)
