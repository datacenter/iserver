from lib.k8s.grafana_dashboard.api import K8sGrafanaDashboardApi
from lib.k8s.grafana_dashboard.info import K8sGrafanaDashboardInfo
from lib.k8s.grafana_dashboard.create import K8sGrafanaDashboardCreate
from lib.k8s.grafana_dashboard.delete import K8sGrafanaDashboardDelete
from lib.k8s.grafana_dashboard.wait import K8sGrafanaDashboardWait


class K8sGrafanaDashboard(
        K8sGrafanaDashboardApi,
        K8sGrafanaDashboardInfo,
        K8sGrafanaDashboardCreate,
        K8sGrafanaDashboardDelete,
        K8sGrafanaDashboardWait
        ):
    def __init__(self):
        K8sGrafanaDashboardApi.__init__(self)
        K8sGrafanaDashboardInfo.__init__(self)
        K8sGrafanaDashboardCreate.__init__(self)
        K8sGrafanaDashboardDelete.__init__(self)
        K8sGrafanaDashboardWait.__init__(self)
    