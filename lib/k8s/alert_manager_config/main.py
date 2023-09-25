from lib.k8s.alert_manager_config.api import K8sAlertManagerConfigApi
from lib.k8s.alert_manager_config.info import K8sAlertManagerConfigInfo


class K8sAlertManagerConfig(
        K8sAlertManagerConfigApi,
        K8sAlertManagerConfigInfo
        ):
    def __init__(self):
        K8sAlertManagerConfigApi.__init__(self)
        K8sAlertManagerConfigInfo.__init__(self)
