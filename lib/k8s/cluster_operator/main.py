from lib.k8s.cluster_operator.api import K8sClusterOperatorApi
from lib.k8s.cluster_operator.info import K8sClusterOperatorInfo
from lib.k8s.cluster_operator.deployment import K8sClusterOperatorDeployment
from lib.k8s.cluster_operator.wait import K8sClusterOperatorWait


class K8sClusterOperator(
        K8sClusterOperatorApi,
        K8sClusterOperatorInfo,
        K8sClusterOperatorDeployment,
        K8sClusterOperatorWait
        ):
    def __init__(self):
        K8sClusterOperatorApi.__init__(self)
        K8sClusterOperatorInfo.__init__(self)
        K8sClusterOperatorDeployment.__init__(self)
        K8sClusterOperatorWait.__init__(self)
