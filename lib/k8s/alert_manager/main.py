from lib.k8s.alert_manager.api import K8sAlertManagerApi
from lib.k8s.alert_manager.info import K8sAlertManagerInfo


class K8sAlertManager(
        K8sAlertManagerApi,
        K8sAlertManagerInfo
        ):
    def __init__(self):
        K8sAlertManagerApi.__init__(self)
        K8sAlertManagerInfo.__init__(self)
