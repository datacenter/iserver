from lib.k8s.auth.api import K8sAuthApi
from lib.k8s.auth.info import K8sAuthInfo
from lib.k8s.auth.delete import K8sAuthDelete
from lib.k8s.auth.wait import K8sAuthWait


class K8sAuth(
        K8sAuthApi,
        K8sAuthInfo,
        K8sAuthDelete,
        K8sAuthWait
        ):
    def __init__(self):
        K8sAuthApi.__init__(self)
        K8sAuthInfo.__init__(self)
        K8sAuthDelete.__init__(self)
        K8sAuthWait.__init__(self)
