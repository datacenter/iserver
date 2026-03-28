from lib.k8s.cluster_user_defined_network.api import K8sClusterUserDefinedNetworkApi
from lib.k8s.cluster_user_defined_network.info import K8sClusterUserDefinedNetworkInfo
from lib.k8s.cluster_user_defined_network.delete import K8sClusterUserDefinedNetworkDelete
from lib.k8s.cluster_user_defined_network.l2 import K8sClusterUserDefinedNetworkL2
from lib.k8s.cluster_user_defined_network.l3 import K8sClusterUserDefinedNetworkL3
from lib.k8s.cluster_user_defined_network.localnet import K8sClusterUserDefinedNetworkLocalnet
from lib.k8s.cluster_user_defined_network.match import K8sClusterUserDefinedNetworkMatch
from lib.k8s.cluster_user_defined_network.namespace import K8sClusterUserDefinedNetworkNamespace
from lib.k8s.cluster_user_defined_network.wait import K8sClusterUserDefinedNetworkWait


class K8sClusterUserDefinedNetwork(
        K8sClusterUserDefinedNetworkApi,
        K8sClusterUserDefinedNetworkInfo,
        K8sClusterUserDefinedNetworkDelete,
        K8sClusterUserDefinedNetworkL2,
        K8sClusterUserDefinedNetworkL3,
        K8sClusterUserDefinedNetworkLocalnet,
        K8sClusterUserDefinedNetworkMatch,
        K8sClusterUserDefinedNetworkNamespace,
        K8sClusterUserDefinedNetworkWait
        ):
    def __init__(self):
        K8sClusterUserDefinedNetworkApi.__init__(self)
        K8sClusterUserDefinedNetworkInfo.__init__(self)
        K8sClusterUserDefinedNetworkDelete.__init__(self)
        K8sClusterUserDefinedNetworkL2.__init__(self)
        K8sClusterUserDefinedNetworkL3.__init__(self)
        K8sClusterUserDefinedNetworkLocalnet.__init__(self)
        K8sClusterUserDefinedNetworkMatch.__init__(self)
        K8sClusterUserDefinedNetworkNamespace.__init__(self)
        K8sClusterUserDefinedNetworkWait.__init__(self)
