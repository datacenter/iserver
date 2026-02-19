from lib.k8s.grafana_datasource.api import K8sGrafanaDatasourceApi
from lib.k8s.grafana_datasource.info import K8sGrafanaDatasourceInfo
from lib.k8s.grafana_datasource.create import K8sGrafanaDatasourceCreate
from lib.k8s.grafana_datasource.delete import K8sGrafanaDatasourceDelete
from lib.k8s.grafana_datasource.wait import K8sGrafanaDatasourceWait


class K8sGrafanaDatasource(
        K8sGrafanaDatasourceApi,
        K8sGrafanaDatasourceInfo,
        K8sGrafanaDatasourceCreate,
        K8sGrafanaDatasourceDelete,
        K8sGrafanaDatasourceWait
        ):
    def __init__(self):
        K8sGrafanaDatasourceApi.__init__(self)
        K8sGrafanaDatasourceInfo.__init__(self)
        K8sGrafanaDatasourceCreate.__init__(self)
        K8sGrafanaDatasourceDelete.__init__(self)
        K8sGrafanaDatasourceWait.__init__(self)
