from lib.k8s.tracing_policy_namespaced.api import K8sTracingPolicyNamespacedApi
from lib.k8s.tracing_policy_namespaced.info import K8sTracingPolicyNamespacedInfo
from lib.k8s.tracing_policy_namespaced.create import K8sTracingPolicyNamespacedCreate
from lib.k8s.tracing_policy_namespaced.delete import K8sTracingPolicyNamespacedDelete
from lib.k8s.tracing_policy_namespaced.wait import K8sTracingPolicyNamespacedWait


class K8sTracingPolicyNamespaced(
        K8sTracingPolicyNamespacedApi,
        K8sTracingPolicyNamespacedInfo,
        K8sTracingPolicyNamespacedCreate,
        K8sTracingPolicyNamespacedDelete,
        K8sTracingPolicyNamespacedWait
        ):
    def __init__(self):
        K8sTracingPolicyNamespacedApi.__init__(self)
        K8sTracingPolicyNamespacedInfo.__init__(self)
        K8sTracingPolicyNamespacedCreate.__init__(self)
        K8sTracingPolicyNamespacedDelete.__init__(self)
        K8sTracingPolicyNamespacedWait.__init__(self)