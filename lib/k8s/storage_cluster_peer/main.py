from lib.k8s.storage_cluster_peer.api import K8sStorageClusterPeerApi
from lib.k8s.storage_cluster_peer.info import K8sStorageClusterPeerInfo


class K8sStorageClusterPeer(
        K8sStorageClusterPeerApi,
        K8sStorageClusterPeerInfo
        ):
    def __init__(self):
        K8sStorageClusterPeerApi.__init__(self)
        K8sStorageClusterPeerInfo.__init__(self)
