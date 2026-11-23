from lib.k8s.ceph_cluster.api import K8sCephClusterApi
from lib.k8s.ceph_cluster.info import K8sCephClusterInfo
from lib.k8s.ceph_cluster.wait import K8sCephClusterWait


class K8sCephCluster(
        K8sCephClusterApi,
        K8sCephClusterInfo,
        K8sCephClusterWait
        ):
    def __init__(self):
        K8sCephClusterApi.__init__(self)
        K8sCephClusterInfo.__init__(self)
        K8sCephClusterWait.__init__(self)
