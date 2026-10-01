from lib.k8s.tetragon_network_policy.api import K8sTetragonNetworkPolicyApi
from lib.k8s.tetragon_network_policy.info import K8sTetragonNetworkPolicyInfo
from lib.k8s.tetragon_network_policy.create import K8sTetragonNetworkPolicyCreate
from lib.k8s.tetragon_network_policy.delete import K8sTetragonNetworkPolicyDelete
from lib.k8s.tetragon_network_policy.wait import K8sTetragonNetworkPolicyWait


class K8sTetragonNetworkPolicy(
        K8sTetragonNetworkPolicyApi,
        K8sTetragonNetworkPolicyInfo,
        K8sTetragonNetworkPolicyCreate,
        K8sTetragonNetworkPolicyDelete,
        K8sTetragonNetworkPolicyWait
        ):
    def __init__(self):
        K8sTetragonNetworkPolicyApi.__init__(self)
        K8sTetragonNetworkPolicyInfo.__init__(self)
        K8sTetragonNetworkPolicyCreate.__init__(self)
        K8sTetragonNetworkPolicyDelete.__init__(self)
        K8sTetragonNetworkPolicyWait.__init__(self)