from lib.k8s.node.api import K8sNodeApi
from lib.k8s.node.info import K8sNodeInfo
from lib.k8s.node.task import K8sNodeTask


class K8sNode(
        K8sNodeApi,
        K8sNodeInfo,
        K8sNodeTask
        ):
    def __init__(self):
        K8sNodeApi.__init__(self)
        K8sNodeInfo.__init__(self)
        K8sNodeTask.__init__(self)
