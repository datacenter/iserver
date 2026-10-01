from lib.k8s.sandbox_policy_namespaced.api import K8sSandboxPolicyNamespacedApi
from lib.k8s.sandbox_policy_namespaced.info import K8sSandboxPolicyNamespacedInfo
from lib.k8s.sandbox_policy_namespaced.create import K8sSandboxPolicyNamespacedCreate
from lib.k8s.sandbox_policy_namespaced.delete import K8sSandboxPolicyNamespacedDelete
from lib.k8s.sandbox_policy_namespaced.wait import K8sSandboxPolicyNamespacedWait


class K8sSandboxPolicyNamespaced(
        K8sSandboxPolicyNamespacedApi,
        K8sSandboxPolicyNamespacedInfo,
        K8sSandboxPolicyNamespacedCreate,
        K8sSandboxPolicyNamespacedDelete,
        K8sSandboxPolicyNamespacedWait
        ):
    def __init__(self):
        K8sSandboxPolicyNamespacedApi.__init__(self)
        K8sSandboxPolicyNamespacedInfo.__init__(self)
        K8sSandboxPolicyNamespacedCreate.__init__(self)
        K8sSandboxPolicyNamespacedDelete.__init__(self)
        K8sSandboxPolicyNamespacedWait.__init__(self)