from lib.k8s.grafana.api import K8sGrafanaApi
from lib.k8s.grafana.info import K8sGrafanaInfo
from lib.k8s.grafana.create import K8sGrafanaCreate
from lib.k8s.grafana.delete import K8sGrafanaDelete
from lib.k8s.grafana.wait import K8sGrafanaWait


class K8sGrafana(
        K8sGrafanaApi,
        K8sGrafanaInfo,
        K8sGrafanaCreate,
        K8sGrafanaDelete,
        K8sGrafanaWait
        ):
    def __init__(self):
        K8sGrafanaApi.__init__(self)
        K8sGrafanaInfo.__init__(self)
        K8sGrafanaCreate.__init__(self)
        K8sGrafanaDelete.__init__(self)
        K8sGrafanaWait.__init__(self)
