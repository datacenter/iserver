from lib.k8s.authentication.api import K8sAuthenticationApi
from lib.k8s.authentication.info import K8sAuthenticationInfo
from lib.k8s.authentication.update import K8sAuthenticationUpdate


class K8sAuthentication(
        K8sAuthenticationApi,
        K8sAuthenticationInfo,
        K8sAuthenticationUpdate
        ):
    def __init__(self):
        K8sAuthenticationApi.__init__(self)
        K8sAuthenticationInfo.__init__(self)
        K8sAuthenticationUpdate.__init__(self)
