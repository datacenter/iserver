from lib.k8s.cluster_issuer.api import K8sClusterIssuerApi
from lib.k8s.cluster_issuer.info import K8sClusterIssuerInfo
from lib.k8s.cluster_issuer.create import K8sClusterIssuerCreate
from lib.k8s.cluster_issuer.delete import K8sClusterIssuerDelete
from lib.k8s.cluster_issuer.wait import K8sClusterIssuerWait


class K8sClusterIssuer(
        K8sClusterIssuerApi,
        K8sClusterIssuerInfo,
        K8sClusterIssuerCreate,
        K8sClusterIssuerDelete,
        K8sClusterIssuerWait
        ):
    def __init__(self):
        K8sClusterIssuerApi.__init__(self)
        K8sClusterIssuerInfo.__init__(self)
        K8sClusterIssuerCreate.__init__(self)
        K8sClusterIssuerDelete.__init__(self)
        K8sClusterIssuerWait.__init__(self)