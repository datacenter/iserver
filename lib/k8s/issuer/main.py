from lib.k8s.issuer.api import K8sIssuerApi
from lib.k8s.issuer.info import K8sIssuerInfo
from lib.k8s.issuer.create import K8sIssuerCreate
from lib.k8s.issuer.delete import K8sIssuerDelete
from lib.k8s.issuer.wait import K8sIssuerWait


class K8sIssuer(
        K8sIssuerApi,
        K8sIssuerInfo,
        K8sIssuerCreate,
        K8sIssuerDelete,
        K8sIssuerWait
        ):
    def __init__(self):
        K8sIssuerApi.__init__(self)
        K8sIssuerInfo.__init__(self)
        K8sIssuerCreate.__init__(self)
        K8sIssuerDelete.__init__(self)
        K8sIssuerWait.__init__(self)