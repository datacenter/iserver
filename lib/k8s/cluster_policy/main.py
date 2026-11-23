from lib.k8s.cluster_policy.api import K8sClusterPolicyApi
from lib.k8s.cluster_policy.info import K8sClusterPolicyInfo
from lib.k8s.cluster_policy.create import K8sClusterPolicyCreate
from lib.k8s.cluster_policy.delete import K8sClusterPolicyDelete
from lib.k8s.cluster_policy.wait import K8sClusterPolicyWait


class K8sClusterPolicy(
        K8sClusterPolicyApi,
        K8sClusterPolicyInfo,
        K8sClusterPolicyCreate,
        K8sClusterPolicyDelete,
        K8sClusterPolicyWait
        ):
    def __init__(self):
        K8sClusterPolicyApi.__init__(self)
        K8sClusterPolicyInfo.__init__(self)
        K8sClusterPolicyCreate.__init__(self)
        K8sClusterPolicyDelete.__init__(self)
        K8sClusterPolicyWait.__init__(self)
