from lib.k8s.issuer.api import K8sIssuerApi
from lib.k8s.issuer.info import K8sIssuerInfo


class K8sIssuer(
        K8sIssuerApi,
        K8sIssuerInfo
        ):
    def __init__(self):
        K8sIssuerApi.__init__(self)
        K8sIssuerInfo.__init__(self)
