from lib.k8s.data_science_cluster_initialization.api import K8sDataScienceClusterInitializationApi
from lib.k8s.data_science_cluster_initialization.info import K8sDataScienceClusterInitializationInfo
from lib.k8s.data_science_cluster_initialization.delete import K8sDataScienceClusterInitializationDelete
from lib.k8s.data_science_cluster_initialization.wait import K8sDataScienceClusterInitializationWait


class K8sDataScienceClusterInitialization(
        K8sDataScienceClusterInitializationApi,
        K8sDataScienceClusterInitializationInfo,
        K8sDataScienceClusterInitializationDelete,
        K8sDataScienceClusterInitializationWait
        ):
    def __init__(self):
        K8sDataScienceClusterInitializationApi.__init__(self)
        K8sDataScienceClusterInitializationInfo.__init__(self)
        K8sDataScienceClusterInitializationDelete.__init__(self)
        K8sDataScienceClusterInitializationWait.__init__(self)
