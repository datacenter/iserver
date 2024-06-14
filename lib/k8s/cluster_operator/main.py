from lib.k8s.cluster_operator.api import K8sClusterOperatorApi
from lib.k8s.cluster_operator.info import K8sClusterOperatorInfo


class K8sClusterOperator(
        K8sClusterOperatorApi,
        K8sClusterOperatorInfo
        ):
    def __init__(self):
        K8sClusterOperatorApi.__init__(self)
        K8sClusterOperatorInfo.__init__(self)
