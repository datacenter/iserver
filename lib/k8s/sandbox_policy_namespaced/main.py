from lib.k8s.sandbox_policy_namespaced.api import K8sSandboxPolicyNamespacedApi
from lib.k8s.sandbox_policy_namespaced.info import K8sSandboxPolicyNamespacedInfo


class K8sSandboxPolicyNamespaced(
        K8sSandboxPolicyNamespacedApi,
        K8sSandboxPolicyNamespacedInfo
        ):
    def __init__(self):
        K8sSandboxPolicyNamespacedApi.__init__(self)
        K8sSandboxPolicyNamespacedInfo.__init__(self)
