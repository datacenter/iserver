from lib.k8s.grafana_contact_point.api import K8sGrafanaContactPointApi
from lib.k8s.grafana_contact_point.info import K8sGrafanaContactPointInfo


class K8sGrafanaContactPoint(
        K8sGrafanaContactPointApi,
        K8sGrafanaContactPointInfo
        ):
    def __init__(self):
        K8sGrafanaContactPointApi.__init__(self)
        K8sGrafanaContactPointInfo.__init__(self)
