from lib.k8s.tracing_policy_namespaced.api import K8sTracingPolicyNamespacedApi
from lib.k8s.tracing_policy_namespaced.info import K8sTracingPolicyNamespacedInfo


class K8sTracingPolicyNamespaced(
        K8sTracingPolicyNamespacedApi,
        K8sTracingPolicyNamespacedInfo
        ):
    def __init__(self):
        K8sTracingPolicyNamespacedApi.__init__(self)
        K8sTracingPolicyNamespacedInfo.__init__(self)
