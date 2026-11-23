from lib.k8s.installplan.api import K8sInstallplanApi
from lib.k8s.installplan.info import K8sInstallplanInfo
from lib.k8s.installplan.approve import K8sInstallplanApprove
from lib.k8s.installplan.wait import K8sInstallplanWait


class K8sInstallplan(
        K8sInstallplanApi,
        K8sInstallplanInfo,
        K8sInstallplanApprove,
        K8sInstallplanWait
        ):
    def __init__(self):
        K8sInstallplanApi.__init__(self)
        K8sInstallplanInfo.__init__(self)
        K8sInstallplanApprove.__init__(self)
        K8sInstallplanWait.__init__(self)
