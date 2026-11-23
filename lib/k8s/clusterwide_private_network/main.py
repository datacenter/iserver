from lib.k8s.clusterwide_private_network.api import K8sClusterwidePrivateNetworkApi
from lib.k8s.clusterwide_private_network.info import K8sClusterwidePrivateNetworkInfo
from lib.k8s.clusterwide_private_network.create import K8sClusterwidePrivateNetworkCreate
from lib.k8s.clusterwide_private_network.delete import K8sClusterwidePrivateNetworkDelete
from lib.k8s.clusterwide_private_network.db import K8sClusterwidePrivateNetworkDb
from lib.k8s.clusterwide_private_network.pod import K8sClusterwidePrivateNetworkPod
from lib.k8s.clusterwide_private_network.state import K8sClusterwidePrivateNetworkState
from lib.k8s.clusterwide_private_network.wait import K8sClusterwidePrivateNetworkWait


class K8sClusterwidePrivateNetwork(
        K8sClusterwidePrivateNetworkApi,
        K8sClusterwidePrivateNetworkInfo,
        K8sClusterwidePrivateNetworkCreate,
        K8sClusterwidePrivateNetworkDelete,
        K8sClusterwidePrivateNetworkDb,
        K8sClusterwidePrivateNetworkPod,
        K8sClusterwidePrivateNetworkState,
        K8sClusterwidePrivateNetworkWait
        ):
    def __init__(self):
        K8sClusterwidePrivateNetworkApi.__init__(self)
        K8sClusterwidePrivateNetworkInfo.__init__(self)
        K8sClusterwidePrivateNetworkCreate.__init__(self)
        K8sClusterwidePrivateNetworkDelete.__init__(self)
        K8sClusterwidePrivateNetworkDb.__init__(self)
        K8sClusterwidePrivateNetworkPod.__init__(self)
        K8sClusterwidePrivateNetworkState.__init__(self)
        K8sClusterwidePrivateNetworkWait.__init__(self)
