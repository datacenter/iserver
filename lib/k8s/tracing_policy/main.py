from lib.k8s.tracing_policy.api import K8sTracingPolicyApi
from lib.k8s.tracing_policy.info import K8sTracingPolicyInfo
from lib.k8s.tracing_policy.create import K8sTracingPolicyCreate
from lib.k8s.tracing_policy.delete import K8sTracingPolicyDelete
from lib.k8s.tracing_policy.wait import K8sTracingPolicyWait


class K8sTracingPolicy(
        K8sTracingPolicyApi,
        K8sTracingPolicyInfo,
        K8sTracingPolicyCreate,
        K8sTracingPolicyDelete,
        K8sTracingPolicyWait
        ):
    def __init__(self):
        K8sTracingPolicyApi.__init__(self)
        K8sTracingPolicyInfo.__init__(self)
        K8sTracingPolicyCreate.__init__(self)
        K8sTracingPolicyDelete.__init__(self)
        K8sTracingPolicyWait.__init__(self)
