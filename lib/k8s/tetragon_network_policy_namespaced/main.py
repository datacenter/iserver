from lib.k8s.tetragon_network_policy_namespaced.api import K8sTetragonNetworkPolicyNamespacedApi
from lib.k8s.tetragon_network_policy_namespaced.info import K8sTetragonNetworkPolicyNamespacedInfo
from lib.k8s.tetragon_network_policy_namespaced.create import K8sTetragonNetworkPolicyNamespacedCreate
from lib.k8s.tetragon_network_policy_namespaced.delete import K8sTetragonNetworkPolicyNamespacedDelete
from lib.k8s.tetragon_network_policy_namespaced.wait import K8sTetragonNetworkPolicyNamespacedWait


class K8sTetragonNetworkPolicyNamespaced(
        K8sTetragonNetworkPolicyNamespacedApi,
        K8sTetragonNetworkPolicyNamespacedInfo,
        K8sTetragonNetworkPolicyNamespacedCreate,
        K8sTetragonNetworkPolicyNamespacedDelete,
        K8sTetragonNetworkPolicyNamespacedWait
        ):
    def __init__(self):
        K8sTetragonNetworkPolicyNamespacedApi.__init__(self)
        K8sTetragonNetworkPolicyNamespacedInfo.__init__(self)
        K8sTetragonNetworkPolicyNamespacedCreate.__init__(self)
        K8sTetragonNetworkPolicyNamespacedDelete.__init__(self)
        K8sTetragonNetworkPolicyNamespacedWait.__init__(self)