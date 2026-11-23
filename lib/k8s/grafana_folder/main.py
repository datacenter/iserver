from lib.k8s.grafana_folder.api import K8sGrafanaFolderApi
from lib.k8s.grafana_folder.info import K8sGrafanaFolderInfo


class K8sGrafanaFolder(
        K8sGrafanaFolderApi,
        K8sGrafanaFolderInfo
        ):
    def __init__(self):
        K8sGrafanaFolderApi.__init__(self)
        K8sGrafanaFolderInfo.__init__(self)
