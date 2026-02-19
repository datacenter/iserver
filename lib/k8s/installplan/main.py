from lib.k8s.installplan.api import K8sInstallplanApi
from lib.k8s.installplan.info import K8sInstallplanInfo


class K8sInstallplan(
        K8sInstallplanApi,
        K8sInstallplanInfo
        ):
    def __init__(self):
        K8sInstallplanApi.__init__(self)
        K8sInstallplanInfo.__init__(self)
