from lib.k8s.grafana_library_panel.api import K8sGrafanaLibraryPanelApi
from lib.k8s.grafana_library_panel.info import K8sGrafanaLibraryPanelInfo


class K8sGrafanaLibraryPanel(
        K8sGrafanaLibraryPanelApi,
        K8sGrafanaLibraryPanelInfo
        ):
    def __init__(self):
        K8sGrafanaLibraryPanelApi.__init__(self)
        K8sGrafanaLibraryPanelInfo.__init__(self)
