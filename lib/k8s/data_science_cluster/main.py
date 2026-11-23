from lib.k8s.data_science_cluster.api import K8sDataScienceClusterApi
from lib.k8s.data_science_cluster.info import K8sDataScienceClusterInfo
from lib.k8s.data_science_cluster.create import K8sDataScienceClusterCreate
from lib.k8s.data_science_cluster.delete import K8sDataScienceClusterDelete
from lib.k8s.data_science_cluster.wait import K8sDataScienceClusterWait


class K8sDataScienceCluster(
        K8sDataScienceClusterApi,
        K8sDataScienceClusterInfo,
        K8sDataScienceClusterCreate,
        K8sDataScienceClusterDelete,
        K8sDataScienceClusterWait
        ):
    def __init__(self):
        K8sDataScienceClusterApi.__init__(self)
        K8sDataScienceClusterInfo.__init__(self)
        K8sDataScienceClusterCreate.__init__(self)
        K8sDataScienceClusterDelete.__init__(self)
        K8sDataScienceClusterWait.__init__(self)
