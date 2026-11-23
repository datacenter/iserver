from lib.k8s.vast_cluster.api import K8sVastClusterApi
from lib.k8s.vast_cluster.info import K8sVastClusterInfo
from lib.k8s.vast_cluster.create import K8sVastClusterCreate
from lib.k8s.vast_cluster.delete import K8sVastClusterDelete
from lib.k8s.vast_cluster.wait import K8sVastClusterWait


class K8sVastCluster(
        K8sVastClusterApi,
        K8sVastClusterInfo,
        K8sVastClusterCreate,
        K8sVastClusterDelete,
        K8sVastClusterWait
        ):
    def __init__(self):
        K8sVastClusterApi.__init__(self)
        K8sVastClusterInfo.__init__(self)
        K8sVastClusterCreate.__init__(self)
        K8sVastClusterDelete.__init__(self)
        K8sVastClusterWait.__init__(self)
